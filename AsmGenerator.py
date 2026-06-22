"""
AsmGenerator
============
Generates ATmega2560 (Arduino Mega) assembly from the LFC AST.

Architecture notes
------------------
* R16 is always the scratch/LDI register (AVR only supports LDI on R16-R31).
* R0..R15 are used as persistent variable storage (MOV from R16 after LDI).
* R17 is secondary scratch; R18/R19 are condition scratch registers.
* 8-bit variables occupy one register; 16-bit variables occupy two (lo, hi).
* Values are resolved at compile time (constant folding). Runtime expression
  evaluation is only emitted when needed (comparisons, DO-WHILE).

Supported constructs
--------------------
  int variable declarations      → register allocation + LDI/MOV
  PIN_MODE(pin, OUTPUT|INPUT)    → OUT DDRx, mask
  DIGITAL_WRITE(pin, val)        → SBI/CBI PORTx, bit
  DIGITAL_READ(pin)              → IN + ANDI
  ANALOG_WRITE(pin, val)         → STS OCRnA (simplified)
  ANALOG_READ(pin)               → ADMUX + ADCSRA setup
  DELAY(ms)                      → RCALL DELAY / DELAY_255_PLUS
  WHILE(TRUE) {}                 → label + RJMP (infinite loop)
  WHILE(cond) {}                 → label + branch + RJMP
  DO {} WHILE(cond)              → label + body + branch back
  IF(cond) {}                    → branch over block
  IF(cond) {} ELSE {}            → branch + RJMP over else block
"""

# ── Arduino Mega (ATmega2560) digital pin → (PORT_reg, DDR_reg, bit) ──────
MEGA_PIN_MAP = {
    # Port B  – PWM-capable pins
    10: ('PORTB', 'DDRB', 4),
    11: ('PORTB', 'DDRB', 5),
    12: ('PORTB', 'DDRB', 6),
    13: ('PORTB', 'DDRB', 7),
    # Port H
     6: ('PORTH', 'DDRH', 3),
     7: ('PORTH', 'DDRH', 4),
     8: ('PORTH', 'DDRH', 5),
     9: ('PORTH', 'DDRH', 6),
    # Port A  – pins 22-29
    22: ('PORTA', 'DDRA', 0),
    23: ('PORTA', 'DDRA', 1),
    24: ('PORTA', 'DDRA', 2),
    25: ('PORTA', 'DDRA', 3),
    26: ('PORTA', 'DDRA', 4),
    27: ('PORTA', 'DDRA', 5),
    28: ('PORTA', 'DDRA', 6),
    29: ('PORTA', 'DDRA', 7),
    # Port C  – pins 30-37 (reverse bit order on Mega)
    37: ('PORTC', 'DDRC', 0),
    36: ('PORTC', 'DDRC', 1),
    35: ('PORTC', 'DDRC', 2),
    34: ('PORTC', 'DDRC', 3),
    33: ('PORTC', 'DDRC', 4),
    32: ('PORTC', 'DDRC', 5),
    31: ('PORTC', 'DDRC', 6),
    30: ('PORTC', 'DDRC', 7),
    # Port L  – pins 42-49
    42: ('PORTL', 'DDRL', 7),
    43: ('PORTL', 'DDRL', 6),
    44: ('PORTL', 'DDRL', 5),
    45: ('PORTL', 'DDRL', 4),
    46: ('PORTL', 'DDRL', 3),
    47: ('PORTL', 'DDRL', 2),
    48: ('PORTL', 'DDRL', 1),
    49: ('PORTL', 'DDRL', 0),
}

# ── Delay subroutines appended to every output file ────────────────────────
# Each DELAY_INNER iteration ≈ 1 ms at 16 MHz (calibrated with NOPs).
# DELAY(R16)          : R16 = number of milliseconds (≤255)
# DELAY_255_PLUS(R16,R18): R16 = lo byte, R18 = hi byte (16-bit ms count)
_DELAY_FOOTER = """
; --- Delay subroutines -------------------------------------------
; DELAY: R16 = milliseconds (max 255)
DELAY:
\tCPI R16, 0
\tBREQ DELAY_END
\tLDI R17, 250
\tRCALL DELAY_INNER
\tDEC R16
\tRJMP DELAY
DELAY_END:
\tRET

; DELAY_255_PLUS: R16 = lo byte, R18 = hi byte of 16-bit ms count
DELAY_255_PLUS:
\tCPI R16, 0
\tBREQ D255_CHECK_HI
\tLDI R17, 255
\tRCALL DELAY_INNER
\tDEC R16
\tRJMP DELAY_255_PLUS
D255_CHECK_HI:
\tCPI R18, 0
\tBREQ D255_END
\tDEC R18
\tLDI R16, 0xFF
\tRJMP DELAY_255_PLUS
D255_END:
\tRET

; DELAY_INNER: R17 = inner loop count (~1 ms per 250 iterations at 16 MHz)
DELAY_INNER:
\tCPI R17, 0
\tBREQ INNER_END
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tNOP
\tDEC R17
\tRJMP DELAY_INNER
INNER_END:
\tRET
"""

# AVR branch mnemonics: branch if condition is FALSE (to skip a block)
_BRANCH_IF_NOT = {
    '==': 'BRNE',
    '!=': 'BREQ',
    '<':  'BRGE',   # not (a < b)  ↔ a >= b
    '<=': 'BRGT',   # not (a <= b) ↔ a > b  (no BRGT; use BRGE with swap)
    '>':  'BRLE',   # not (a > b)  ↔ a <= b (no BRLE; AVR uses BRSH/BRLO)
    '>=': 'BRLT',
}

# AVR branch if condition IS true (to loop back)
_BRANCH_IF_TRUE = {
    '==': 'BREQ',
    '!=': 'BRNE',
    '<':  'BRLT',
    '<=': 'BRLE',
    '>':  'BRGT',
    '>=': 'BRGE',
}


class CodegenError(Exception):
    pass


class AsmGenerator:
    # Registers reserved for scratch (must be in R16-R31 for LDI to work)
    SCRATCH  = 'R16'   # primary scratch / LDI target
    SCRATCH2 = 'R17'   # secondary scratch (used inside delay routines)
    COND_A   = 'R18'   # condition left operand / delay hi byte
    COND_B   = 'R19'   # condition right operand

    def __init__(self):
        # Variable table: name → {'kind':'8bit','reg':Rx,'value':v}
        #                     or {'kind':'16bit','reg_lo':Rx,'reg_hi':Ry,'value':v}
        self._vars: dict = {}
        self._next_reg: int = 0      # next free storage register (R0 upward)
        self._label_n: int  = 0      # unique label counter
        self._lines: list   = []     # all emitted assembly lines

    # ── public interface ────────────────────────────────────────────────────
    def generate(self, ast: dict) -> str:
        self._emit_header()
        for stmt in ast.get('stmts', []):
            self._gen(stmt)
        self._lines.append(_DELAY_FOOTER)
        return '\n'.join(self._lines)

    # ── emit helpers ────────────────────────────────────────────────────────
    def _emit(self, line: str):
        self._lines.append(line)

    def _label(self, prefix='L') -> str:
        self._label_n += 1
        return f'{prefix}_{self._label_n}'

    def _emit_header(self):
        self._emit('\n.ORG 0\n')
        self._emit(f'\tLDI {self.SCRATCH}, 0x08')
        self._emit(f'\tOUT SPH, {self.SCRATCH}')
        self._emit(f'\tLDI {self.SCRATCH}, 0xFF')
        self._emit(f'\tOUT SPL, {self.SCRATCH}')
        self._emit('')
        self._emit('SETUP:')

    # ── dispatcher ─────────────────────────────────────────────────────────
    def _gen(self, node):
        if node is None:
            return
        handler = getattr(self, f'_gen_{node["kind"]}', self._gen_noop)
        handler(node)

    def _gen_noop(self, node):
        self._emit(f'\t; [skipped: {node["kind"]}]')

    # ── variable declaration ────────────────────────────────────────────────
    def _gen_var_decl(self, node):
        if node['var_type'] not in ('int', 'float'):
            self._emit(f'\t; skipping non-numeric variable {node["name"]}')
            return
        value = self._eval(node.get('value'))
        if value is None:
            self._emit(f'\t; cannot evaluate {node["name"]} at compile time')
            return
        self._alloc(node['name'], int(value))

    def _alloc(self, name: str, value: int):
        """Allocate register(s) for a variable and emit load instructions."""
        if not (0 <= value <= 65535):
            raise CodegenError(f"Value {value} out of 16-bit range for '{name}'")
        if value > 255:
            reg_lo = f'R{self._next_reg}'; self._next_reg += 1
            reg_hi = f'R{self._next_reg}'; self._next_reg += 1
            self._vars[name] = {'kind': '16bit', 'reg_lo': reg_lo,
                                'reg_hi': reg_hi, 'value': value}
            b = format(value, '#018b')
            self._emit(f'\tLDI {self.SCRATCH}, LOW({b})')
            self._emit(f'\tMOV {reg_lo}, {self.SCRATCH}')
            self._emit(f'\tLDI {self.SCRATCH}, HIGH({b})')
            self._emit(f'\tMOV {reg_hi}, {self.SCRATCH}')
        else:
            reg = f'R{self._next_reg}'; self._next_reg += 1
            self._vars[name] = {'kind': '8bit', 'reg': reg, 'value': value}
            b = format(value, '#010b')
            self._emit(f'\tLDI {self.SCRATCH}, {b}')
            self._emit(f'\tMOV {reg}, {self.SCRATCH}')

    # ── hardware calls ───────────────────────────────────────────────────────
    def _gen_pin_mode(self, node):
        pin = self._resolve_pin(node['pin'])
        info = MEGA_PIN_MAP.get(pin)
        if info is None:
            self._emit(f'\t; PIN_MODE: pin {pin} not in supported pin map')
            return
        port, ddr, bit = info
        mask = 1 << bit
        b = format(mask, '#010b')
        if node['mode'] == 'OUTPUT':
            self._emit(f'\tLDI {self.SCRATCH}, {b}')
            self._emit(f'\tOUT {ddr}, {self.SCRATCH}')
        else:                                         # INPUT
            clr = format((~mask) & 0xFF, '#010b')
            self._emit(f'\tLDI {self.SCRATCH}, {clr}')
            self._emit(f'\tOUT {ddr}, {self.SCRATCH}')

    def _gen_digital_write(self, node):
        pin = self._resolve_pin(node['pin'])
        val = self._resolve_value(node['value'])
        info = MEGA_PIN_MAP.get(pin)
        if info is None:
            self._emit(f'\t; DIGITAL_WRITE: pin {pin} not in supported pin map')
            return
        port, ddr, bit = info
        if val == 0:
            self._emit(f'\tCBI {port}, {bit}')
        else:
            self._emit(f'\tSBI {port}, {bit}')

    def _gen_digital_read(self, node):
        pin = self._resolve_pin(node['pin'])
        info = MEGA_PIN_MAP.get(pin)
        if info is None:
            self._emit(f'\t; DIGITAL_READ: pin {pin} not in supported pin map')
            return
        port, ddr, bit = info
        pin_reg = port.replace('PORT', 'PIN')
        mask = format(1 << bit, '#010b')
        self._emit(f'\tIN {self.SCRATCH}, {pin_reg}')
        self._emit(f'\tANDI {self.SCRATCH}, {mask}')

    def _gen_analog_read(self, node):
        pin = self._resolve_pin(node['pin'])
        ch = pin if pin is not None else 0
        self._emit(f'\t; ANALOG_READ on ADC channel {ch}')
        self._emit(f'\tLDI {self.SCRATCH}, {ch & 0x07}')
        self._emit(f'\tSTS ADMUX, {self.SCRATCH}')
        self._emit(f'\tLDS {self.SCRATCH}, ADCSRA')
        self._emit(f'\tORI {self.SCRATCH}, 0b01000000')
        self._emit(f'\tSTS ADCSRA, {self.SCRATCH}')

    def _gen_analog_write(self, node):
        pin = self._resolve_pin(node['pin'])
        val = self._resolve_value(node['value'])
        self._emit(f'\t; ANALOG_WRITE (PWM) pin {pin}, value {val}')
        if val is not None:
            b = format(val & 0xFF, '#010b')
            self._emit(f'\tLDI {self.SCRATCH}, {b}')
            self._emit(f'\tSTS OCR1A, {self.SCRATCH}')

    def _gen_delay(self, node):
        ms = self._eval(node['time'])
        if ms is None:
            # Try resolving from variable register
            t = node['time']
            if t and t['kind'] == 'id':
                info = self._vars.get(t['name'])
                if info:
                    ms = info['value']
        if ms is None:
            self._emit('\t; DELAY: cannot resolve time value')
            return
        ms = int(ms)
        if ms > 255:
            # 16-bit delay: R16=lo, R18=hi
            lo = ms & 0xFF
            hi = (ms >> 8) & 0xFF
            t = node['time']
            if t and t['kind'] == 'id':
                info = self._vars.get(t['name'])
                if info and info['kind'] == '16bit':
                    self._emit(f'\tMOV {self.SCRATCH}, {info["reg_lo"]}')
                    self._emit(f'\tMOV {self.COND_A}, {info["reg_hi"]}')
                else:
                    self._emit(f'\tLDI {self.SCRATCH}, {format(lo, "#010b")}')
                    self._emit(f'\tLDI {self.COND_A}, {format(hi, "#010b")}')
            else:
                self._emit(f'\tLDI {self.SCRATCH}, {format(lo, "#010b")}')
                self._emit(f'\tLDI {self.COND_A}, {format(hi, "#010b")}')
            self._emit(f'\tRCALL DELAY_255_PLUS')
        else:
            b = format(ms, '#010b')
            self._emit(f'\tLDI {self.SCRATCH}, {b}')
            self._emit(f'\tRCALL DELAY')

    # ── control flow ─────────────────────────────────────────────────────────
    def _gen_while(self, node):
        cond = node['cond']
        body = node.get('body', [])

        # Special-case WHILE (TRUE) → infinite loop
        if cond and cond['kind'] == 'bool_lit' and cond['value']:
            lbl = self._label('WHILE')
            self._emit(f'\n{lbl}:')
            for stmt in body:
                self._gen(stmt)
            self._emit(f'\tRJMP {lbl}')
            return

        loop_lbl = self._label('WHILE')
        end_lbl  = self._label('END_WHILE')
        self._emit(f'\n{loop_lbl}:')
        self._emit_branch_if_false(cond, end_lbl)
        for stmt in body:
            self._gen(stmt)
        self._emit(f'\tRJMP {loop_lbl}')
        self._emit(f'{end_lbl}:')

    def _gen_do_while(self, node):
        body = node.get('body', [])
        cond = node['cond']
        loop_lbl = self._label('DO_WHILE')
        self._emit(f'\n{loop_lbl}:')
        for stmt in body:
            self._gen(stmt)
        self._emit_branch_if_true(cond, loop_lbl)

    def _gen_if(self, node):
        end_lbl = self._label('END_IF')
        self._emit_branch_if_false(node['cond'], end_lbl)
        for stmt in node.get('then', []):
            self._gen(stmt)
        self._emit(f'{end_lbl}:')

    def _gen_if_else(self, node):
        else_lbl = self._label('ELSE')
        end_lbl  = self._label('END_IF')
        self._emit_branch_if_false(node['cond'], else_lbl)
        for stmt in node.get('then', []):
            self._gen(stmt)
        self._emit(f'\tRJMP {end_lbl}')
        self._emit(f'{else_lbl}:')
        for stmt in node.get('else', []):
            self._gen(stmt)
        self._emit(f'{end_lbl}:')

    # ── branch helpers ───────────────────────────────────────────────────────
    def _emit_branch_if_false(self, cond, target_label: str):
        """Jump to target_label when condition is false."""
        if cond is None:
            return
        if cond['kind'] == 'bool_lit':
            if not cond['value']:
                self._emit(f'\tRJMP {target_label}')
            return
        if cond['kind'] == 'id':
            info = self._vars.get(cond['name'])
            if info:
                reg = info.get('reg') or info.get('reg_lo')
                self._emit(f'\tTST {reg}')
                self._emit(f'\tBREQ {target_label}')
            return
        if cond['kind'] == 'compare':
            self._load_to(cond['left'], self.COND_A)
            self._load_to(cond['right'], self.COND_B)
            self._emit(f'\tCP {self.COND_A}, {self.COND_B}')
            branch = _BRANCH_IF_NOT.get(cond['op'], 'BRNE')
            self._emit(f'\t{branch} {target_label}')

    def _emit_branch_if_true(self, cond, target_label: str):
        """Jump to target_label when condition is true (used for do-while back edge)."""
        if cond is None:
            return
        if cond['kind'] == 'bool_lit':
            if cond['value']:
                self._emit(f'\tRJMP {target_label}')
            return
        if cond['kind'] == 'id':
            info = self._vars.get(cond['name'])
            if info:
                reg = info.get('reg') or info.get('reg_lo')
                self._emit(f'\tTST {reg}')
                self._emit(f'\tBRNE {target_label}')
            return
        if cond['kind'] == 'compare':
            self._load_to(cond['left'], self.COND_A)
            self._load_to(cond['right'], self.COND_B)
            self._emit(f'\tCP {self.COND_A}, {self.COND_B}')
            branch = _BRANCH_IF_TRUE.get(cond['op'], 'BREQ')
            self._emit(f'\t{branch} {target_label}')

    def _load_to(self, node, dest_reg: str):
        """Load an 8-bit expression value into dest_reg."""
        val = self._eval(node)
        if val is not None:
            b = format(int(val) & 0xFF, '#010b')
            self._emit(f'\tLDI {self.SCRATCH}, {b}')
            if dest_reg != self.SCRATCH:
                self._emit(f'\tMOV {dest_reg}, {self.SCRATCH}')
        elif node and node['kind'] == 'id':
            info = self._vars.get(node['name'])
            if info:
                src = info.get('reg') or info.get('reg_lo')
                if src != dest_reg:
                    self._emit(f'\tMOV {dest_reg}, {src}')

    # ── expression evaluation (compile-time) ─────────────────────────────────
    def _eval(self, node) -> int | None:
        """Try to evaluate an AST expression to a Python integer at compile time."""
        if node is None:
            return None
        k = node['kind']
        if k == 'int_lit':
            return int(node['value'])
        if k == 'float_lit':
            return int(node['value'])
        if k == 'bool_lit':
            return 1 if node['value'] else 0
        if k == 'id':
            info = self._vars.get(node['name'])
            return info['value'] if info else None
        if k == 'binop':
            l = self._eval(node['left'])
            r = self._eval(node['right'])
            if l is None or r is None:
                return None
            op = node['op']
            if op == '+': return l + r
            if op == '-': return l - r
            if op == '*': return l * r
            if op == '/' and r != 0: return l // r
        return None

    def _resolve_pin(self, node) -> int | None:
        """Resolve a pin expression to an integer pin number."""
        return self._eval(node)

    def _resolve_value(self, node) -> int | None:
        """Resolve a value expression (HIGH/LOW/int/var) to an integer."""
        if node is None:
            return None
        if node['kind'] == 'id':
            name = node['name']
            if name == 'HIGH': return 1
            if name == 'LOW':  return 0
        return self._eval(node)
