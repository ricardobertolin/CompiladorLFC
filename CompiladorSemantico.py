"""
CompiladorSemantico
===================
Semantic analysis over the dict-based AST produced by CompiladorVisitor.

Checks performed
----------------
1. Variable declared before use.
2. Variable not re-declared in the same scope.
3. Type compatibility: assignment, arithmetic, comparisons.
4. Hardware calls receive integer-typed pin / value arguments.
5. Control-flow conditions must be boolean or int (truthy).

Usage
-----
    analyzer = CompiladorSemantico()
    errors = analyzer.analyze(ast)   # returns list[str]; empty = OK
"""


class SymbolTable:
    def __init__(self):
        self._scopes = [{}]         # stack of {name: type_str}

    def push_scope(self):
        self._scopes.append({})

    def pop_scope(self):
        if len(self._scopes) > 1:
            self._scopes.pop()

    def declare(self, name, var_type):
        self._scopes[-1][name] = var_type

    def lookup(self, name):
        for scope in reversed(self._scopes):
            if name in scope:
                return scope[name]
        return None

    def declared_in_current_scope(self, name):
        return name in self._scopes[-1]


class CompiladorSemantico:

    def __init__(self):
        self.symbols = SymbolTable()
        self.errors: list = []

    def analyze(self, ast) -> list:
        self.errors = []
        self._visit(ast)
        return self.errors

    # ── dispatcher ─────────────────────────────────────────────────────────
    def _visit(self, node):
        if node is None:
            return 'unknown'
        kind = node.get('kind', '')
        handler = getattr(self, f'_check_{kind}', self._check_unknown)
        return handler(node)

    def _check_unknown(self, node):
        return 'unknown'

    # ── program ─────────────────────────────────────────────────────────────
    def _check_program(self, node):
        for stmt in node.get('stmts', []):
            self._visit(stmt)
        return 'void'

    # ── declarations ────────────────────────────────────────────────────────
    def _check_var_decl(self, node):
        name = node['name']
        vtype = node['var_type']

        if self.symbols.declared_in_current_scope(name):
            self.errors.append(
                f"Variable '{name}' already declared in this scope")
            return vtype

        if node['value'] is not None:
            val_type = self._visit(node['value'])
            if not self._assignable(vtype, val_type):
                self.errors.append(
                    f"Type mismatch: cannot assign {val_type} to "
                    f"'{name}' (declared as {vtype})")

        self.symbols.declare(name, vtype)
        return vtype

    # ── control flow ─────────────────────────────────────────────────────────
    def _check_if(self, node):
        self._require_bool_cond(node['cond'], 'IF')
        self.symbols.push_scope()
        for s in node.get('then', []):
            self._visit(s)
        self.symbols.pop_scope()
        return 'void'

    def _check_if_else(self, node):
        self._require_bool_cond(node['cond'], 'IF/ELSE')
        self.symbols.push_scope()
        for s in node.get('then', []):
            self._visit(s)
        self.symbols.pop_scope()
        self.symbols.push_scope()
        for s in node.get('else', []):
            self._visit(s)
        self.symbols.pop_scope()
        return 'void'

    def _check_while(self, node):
        self._require_bool_cond(node['cond'], 'WHILE')
        self.symbols.push_scope()
        for s in node.get('body', []):
            self._visit(s)
        self.symbols.pop_scope()
        return 'void'

    def _check_do_while(self, node):
        self.symbols.push_scope()
        for s in node.get('body', []):
            self._visit(s)
        self.symbols.pop_scope()
        self._require_bool_cond(node['cond'], 'DO-WHILE')
        return 'void'

    # ── hardware calls ───────────────────────────────────────────────────────
    def _check_digital_write(self, node):
        pin_t = self._visit(node['pin'])
        self._visit(node['value'])
        self._require_int(pin_t, 'DIGITAL_WRITE', 'pin')
        return 'void'

    def _check_digital_read(self, node):
        pin_t = self._visit(node['pin'])
        self._require_int(pin_t, 'DIGITAL_READ', 'pin')
        return 'int'

    def _check_analog_write(self, node):
        pin_t = self._visit(node['pin'])
        val_t = self._visit(node['value'])
        self._require_int(pin_t, 'ANALOG_WRITE', 'pin')
        self._require_int(val_t, 'ANALOG_WRITE', 'value')
        return 'void'

    def _check_analog_read(self, node):
        pin_t = self._visit(node['pin'])
        self._require_int(pin_t, 'ANALOG_READ', 'pin')
        return 'int'

    def _check_pin_mode(self, node):
        pin_t = self._visit(node['pin'])
        self._require_int(pin_t, 'PIN_MODE', 'pin')
        if node['mode'] not in ('INPUT', 'OUTPUT'):
            self.errors.append(
                f"PIN_MODE mode must be INPUT or OUTPUT, got '{node['mode']}'")
        return 'void'

    def _check_delay(self, node):
        time_t = self._visit(node['time'])
        self._require_int(time_t, 'DELAY', 'time')
        return 'void'

    # ── expressions ──────────────────────────────────────────────────────────
    def _check_id(self, node):
        name = node['name']
        t = self.symbols.lookup(name)
        if t is None:
            self.errors.append(f"Undeclared variable '{name}'")
            return 'unknown'
        return t

    def _check_int_lit(self, node):    return 'int'
    def _check_float_lit(self, node):  return 'float'
    def _check_bool_lit(self, node):   return 'bool'
    def _check_string_lit(self, node): return 'string'

    def _check_binop(self, node):
        lt = self._visit(node['left'])
        rt = self._visit(node['right'])
        numeric = ('int', 'float', 'unknown')
        if lt not in numeric or rt not in numeric:
            self.errors.append(
                f"Arithmetic operator '{node['op']}' requires numeric "
                f"operands, got {lt} and {rt}")
            return 'unknown'
        return 'float' if 'float' in (lt, rt) else 'int'

    def _check_compare(self, node):
        lt = self._visit(node['left'])
        rt = self._visit(node['right'])
        if not self._comparable(lt, rt):
            self.errors.append(
                f"Cannot compare {lt} with {rt} using '{node['op']}'")
        return 'bool'

    # ── helpers ─────────────────────────────────────────────────────────────
    def _assignable(self, target, source):
        if source in ('unknown', None):
            return True
        if target == source:
            return True
        if target == 'float' and source == 'int':
            return True             # implicit int-to-float widening
        return False

    def _comparable(self, a, b):
        if 'unknown' in (a, b):
            return True
        numeric = ('int', 'float')
        return (a in numeric and b in numeric) or a == b

    def _require_bool_cond(self, cond, context):
        cond_t = self._visit(cond)
        if cond_t not in ('bool', 'int', 'unknown'):
            self.errors.append(
                f"{context} condition must be boolean, got {cond_t}")

    def _require_int(self, actual_type, call_name, arg_name):
        if actual_type not in ('int', 'unknown'):
            self.errors.append(
                f"{call_name} {arg_name} must be int, got {actual_type}")
