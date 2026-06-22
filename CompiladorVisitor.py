"""
CompiladorVisitor
=================
Walks the ANTLR4 parse tree produced by CompiladorParser and returns a
Python-dict AST.  Each node is a dict with at least a 'kind' key.

Node catalogue
--------------
program        {'kind':'program', 'stmts':[...]}
var_decl       {'kind':'var_decl', 'var_type':str, 'name':str, 'value':node|None}
if             {'kind':'if',      'cond':node, 'then':[...]}
if_else        {'kind':'if_else', 'cond':node, 'then':[...], 'else':[...]}
while          {'kind':'while',   'cond':node, 'body':[...]}
do_while       {'kind':'do_while','body':[...], 'cond':node}
digital_write  {'kind':'digital_write', 'pin':node, 'value':node}
digital_read   {'kind':'digital_read',  'pin':node}
analog_write   {'kind':'analog_write',  'pin':node, 'value':node}
analog_read    {'kind':'analog_read',   'pin':node}
pin_mode       {'kind':'pin_mode',      'pin':node, 'mode':str}
delay          {'kind':'delay',         'time':node}
binop          {'kind':'binop', 'op':str, 'left':node, 'right':node}
compare        {'kind':'compare','op':str, 'left':node, 'right':node}
id             {'kind':'id',      'name':str}
int_lit        {'kind':'int_lit', 'value':int}
float_lit      {'kind':'float_lit','value':float}
bool_lit       {'kind':'bool_lit','value':bool}
string_lit     {'kind':'string_lit','value':str}
"""

from antlr4 import TerminalNode
from CompiladorParser import CompiladorParser


class CompiladorVisitor:

    # ── dispatcher ─────────────────────────────────────────────────────────
    def visit(self, ctx):
        if ctx is None:
            return None
        name = type(ctx).__name__
        handler = getattr(self, f'visit_{name}', self._generic)
        return handler(ctx)

    def _generic(self, ctx):
        if isinstance(ctx, TerminalNode):
            return ctx.getText()
        children = [self.visit(ctx.getChild(i))
                    for i in range(ctx.getChildCount())]
        children = [c for c in children if c is not None]
        if not children:
            return None
        return children[0] if len(children) == 1 else children

    # ── top-level ───────────────────────────────────────────────────────────
    def visit_ProgContext(self, ctx):
        stmts = [self.visit(s) for s in ctx.stmt()]
        return {'kind': 'program', 'stmts': [s for s in stmts if s is not None]}

    # ── statements ──────────────────────────────────────────────────────────
    def visit_StmtContext(self, ctx):
        for attr in ('if_stmt', 'while_stmt', 'do_while_stmt',
                     'variable_declaration', 'comparison_expr',
                     'stmt_2', 'expr_arithmetic'):
            sub = getattr(ctx, attr)()
            if sub is not None:
                return self.visit(sub)
        if ctx.BOOL():
            return {'kind': 'bool_lit', 'value': ctx.BOOL().getText() == 'TRUE'}
        if ctx.TYPE_STRING():
            text = ctx.TYPE_STRING().getText()
            return {'kind': 'string_lit', 'value': text[1:-1]}
        return None

    def visit_If_stmtContext(self, ctx):
        cond = self.visit(ctx.expr())
        blocks = ctx.block()
        then_b = self.visit(blocks[0]) if blocks else []
        else_b = self.visit(blocks[1]) if len(blocks) > 1 else None
        if else_b is not None:
            return {'kind': 'if_else', 'cond': cond,
                    'then': then_b or [], 'else': else_b or []}
        return {'kind': 'if', 'cond': cond, 'then': then_b or []}

    def visit_While_stmtContext(self, ctx):
        return {
            'kind': 'while',
            'cond': self.visit(ctx.expr()),
            'body': self.visit(ctx.block()) or [],
        }

    def visit_Do_while_stmtContext(self, ctx):
        return {
            'kind': 'do_while',
            'body': self.visit(ctx.block()) or [],
            'cond': self.visit(ctx.expr()),
        }

    def visit_Variable_declarationContext(self, ctx):
        var_type = self.visit(ctx.type_())          # type_() avoids Python builtin
        name = (ctx.ID().getText() if ctx.ID()
                else ctx.TYPE_CHAR().getText() if ctx.TYPE_CHAR()
                else None)
        value = None
        if ctx.TYPE_STRING():
            text = ctx.TYPE_STRING().getText()
            value = {'kind': 'string_lit', 'value': text[1:-1]}
        elif ctx.TYPE_INT():
            value = {'kind': 'int_lit', 'value': int(ctx.TYPE_INT().getText())}
        elif ctx.TYPE_REAL():
            value = {'kind': 'float_lit', 'value': float(ctx.TYPE_REAL().getText())}
        return {'kind': 'var_decl', 'var_type': var_type, 'name': name, 'value': value}

    def visit_TypeContext(self, ctx):
        for label, tok_fn in (('int',   ctx.INT),
                              ('float', ctx.FLOAT16),
                              ('bool',  ctx.BOOL),
                              ('void',  ctx.VOID),
                              ('string',ctx.STRING)):
            if tok_fn():
                return label
        return 'unknown'

    # ── hardware calls ───────────────────────────────────────────────────────
    def visit_Stmt_2Context(self, ctx):
        s = ctx.stmt          # callable: s(i) returns i-th stmt child
        if ctx.DIGITAL_READ():
            return {'kind': 'digital_read', 'pin': self.visit(s(0))}
        if ctx.DIGITAL_WRITE():
            return {'kind': 'digital_write',
                    'pin': self.visit(s(0)), 'value': self.visit(s(1))}
        if ctx.ANALOG_READ():
            return {'kind': 'analog_read', 'pin': self.visit(s(0))}
        if ctx.ANALOG_WRITE():
            return {'kind': 'analog_write',
                    'pin': self.visit(s(0)), 'value': self.visit(s(1))}
        if ctx.PIN_MODE():
            return {'kind': 'pin_mode',
                    'pin': self.visit(s(0)),
                    'mode': ctx.PIN_TYPE_().getText()}
        if ctx.DELAY():
            return {'kind': 'delay', 'time': self.visit(s(0))}
        return None

    # ── expressions ─────────────────────────────────────────────────────────
    def visit_Expr_arithmeticContext(self, ctx):
        if ctx.TYPE_INT():
            return {'kind': 'int_lit', 'value': int(ctx.TYPE_INT().getText())}
        if ctx.TYPE_REAL():
            return {'kind': 'float_lit', 'value': float(ctx.TYPE_REAL().getText())}
        subs = ctx.expr_arithmetic()
        if len(subs) == 2:
            op = ('+' if ctx.PLUS()     else
                  '-' if ctx.MINUS()    else
                  '*' if ctx.ASTERISK() else '/')
            return {'kind': 'binop', 'op': op,
                    'left': self.visit(subs[0]), 'right': self.visit(subs[1])}
        if len(subs) == 1:                          # parenthesised sub-expression
            return self.visit(subs[0])
        return None

    def visit_Comparison_exprContext(self, ctx):
        op = ctx.comparison_operator().getChild(0).getText()
        return {
            'kind': 'compare', 'op': op,
            'left':  {'kind': 'id', 'name': ctx.ID().getText()},
            'right': self.visit(ctx.expr()),
        }

    def visit_ExprContext(self, ctx):
        if ctx.comparison_expr():
            return self.visit(ctx.comparison_expr())
        if ctx.id_expr():
            return self.visit(ctx.id_expr())
        return None

    def visit_Id_exprContext(self, ctx):
        if ctx.ID():
            return {'kind': 'id', 'name': ctx.ID().getText()}
        if ctx.TYPE_INT():
            return {'kind': 'int_lit', 'value': int(ctx.TYPE_INT().getText())}
        if ctx.TYPE_REAL():
            return {'kind': 'float_lit', 'value': float(ctx.TYPE_REAL().getText())}
        if ctx.BOOL():
            return {'kind': 'bool_lit', 'value': ctx.BOOL().getText() == 'TRUE'}
        if ctx.TYPE_STRING():
            text = ctx.TYPE_STRING().getText()
            return {'kind': 'string_lit', 'value': text[1:-1]}
        return None

    def visit_BlockContext(self, ctx):
        return [s for s in (self.visit(st) for st in ctx.stmt()) if s is not None]
