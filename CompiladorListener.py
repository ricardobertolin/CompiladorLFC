# Generated from Compilador.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CompiladorParser import CompiladorParser
else:
    from CompiladorParser import CompiladorParser

# This class defines a complete listener for a parse tree produced by CompiladorParser.
class CompiladorListener(ParseTreeListener):

    # Enter a parse tree produced by CompiladorParser#prog.
    def enterProg(self, ctx:CompiladorParser.ProgContext):
        pass

    # Exit a parse tree produced by CompiladorParser#prog.
    def exitProg(self, ctx:CompiladorParser.ProgContext):
        pass


    # Enter a parse tree produced by CompiladorParser#stmt.
    def enterStmt(self, ctx:CompiladorParser.StmtContext):
        pass

    # Exit a parse tree produced by CompiladorParser#stmt.
    def exitStmt(self, ctx:CompiladorParser.StmtContext):
        pass


    # Enter a parse tree produced by CompiladorParser#if_stmt.
    def enterIf_stmt(self, ctx:CompiladorParser.If_stmtContext):
        pass

    # Exit a parse tree produced by CompiladorParser#if_stmt.
    def exitIf_stmt(self, ctx:CompiladorParser.If_stmtContext):
        pass


    # Enter a parse tree produced by CompiladorParser#while_stmt.
    def enterWhile_stmt(self, ctx:CompiladorParser.While_stmtContext):
        pass

    # Exit a parse tree produced by CompiladorParser#while_stmt.
    def exitWhile_stmt(self, ctx:CompiladorParser.While_stmtContext):
        pass


    # Enter a parse tree produced by CompiladorParser#do_while_stmt.
    def enterDo_while_stmt(self, ctx:CompiladorParser.Do_while_stmtContext):
        pass

    # Exit a parse tree produced by CompiladorParser#do_while_stmt.
    def exitDo_while_stmt(self, ctx:CompiladorParser.Do_while_stmtContext):
        pass


    # Enter a parse tree produced by CompiladorParser#stmt_2.
    def enterStmt_2(self, ctx:CompiladorParser.Stmt_2Context):
        pass

    # Exit a parse tree produced by CompiladorParser#stmt_2.
    def exitStmt_2(self, ctx:CompiladorParser.Stmt_2Context):
        pass


    # Enter a parse tree produced by CompiladorParser#expr_arithmetic.
    def enterExpr_arithmetic(self, ctx:CompiladorParser.Expr_arithmeticContext):
        pass

    # Exit a parse tree produced by CompiladorParser#expr_arithmetic.
    def exitExpr_arithmetic(self, ctx:CompiladorParser.Expr_arithmeticContext):
        pass


    # Enter a parse tree produced by CompiladorParser#comparison_expr.
    def enterComparison_expr(self, ctx:CompiladorParser.Comparison_exprContext):
        pass

    # Exit a parse tree produced by CompiladorParser#comparison_expr.
    def exitComparison_expr(self, ctx:CompiladorParser.Comparison_exprContext):
        pass


    # Enter a parse tree produced by CompiladorParser#comparison_operator.
    def enterComparison_operator(self, ctx:CompiladorParser.Comparison_operatorContext):
        pass

    # Exit a parse tree produced by CompiladorParser#comparison_operator.
    def exitComparison_operator(self, ctx:CompiladorParser.Comparison_operatorContext):
        pass


    # Enter a parse tree produced by CompiladorParser#expr.
    def enterExpr(self, ctx:CompiladorParser.ExprContext):
        pass

    # Exit a parse tree produced by CompiladorParser#expr.
    def exitExpr(self, ctx:CompiladorParser.ExprContext):
        pass


    # Enter a parse tree produced by CompiladorParser#variable_declaration.
    def enterVariable_declaration(self, ctx:CompiladorParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by CompiladorParser#variable_declaration.
    def exitVariable_declaration(self, ctx:CompiladorParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by CompiladorParser#type.
    def enterType(self, ctx:CompiladorParser.TypeContext):
        pass

    # Exit a parse tree produced by CompiladorParser#type.
    def exitType(self, ctx:CompiladorParser.TypeContext):
        pass


    # Enter a parse tree produced by CompiladorParser#id_expr.
    def enterId_expr(self, ctx:CompiladorParser.Id_exprContext):
        pass

    # Exit a parse tree produced by CompiladorParser#id_expr.
    def exitId_expr(self, ctx:CompiladorParser.Id_exprContext):
        pass


    # Enter a parse tree produced by CompiladorParser#block.
    def enterBlock(self, ctx:CompiladorParser.BlockContext):
        pass

    # Exit a parse tree produced by CompiladorParser#block.
    def exitBlock(self, ctx:CompiladorParser.BlockContext):
        pass



del CompiladorParser