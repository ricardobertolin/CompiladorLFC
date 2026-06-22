# Generated from Compilador.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,46,181,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,4,0,30,8,0,11,0,12,0,31,1,0,5,0,35,8,0,10,0,12,0,38,9,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,52,8,1,10,1,12,1,
        55,9,1,1,1,1,1,1,1,1,1,3,1,61,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,
        2,70,8,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,78,8,2,1,3,1,3,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,3,5,134,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,143,8,6,1,6,1,6,
        1,6,5,6,148,8,6,10,6,12,6,151,9,6,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,
        9,3,9,161,8,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,13,
        1,13,5,13,174,8,13,10,13,12,13,177,9,13,1,13,1,13,1,13,0,1,12,14,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,6,1,0,28,31,2,0,33,35,38,
        38,2,0,12,12,46,46,2,0,10,11,13,13,1,0,2,6,4,0,6,6,10,11,13,13,46,
        46,192,0,29,1,0,0,0,2,60,1,0,0,0,4,77,1,0,0,0,6,79,1,0,0,0,8,85,
        1,0,0,0,10,133,1,0,0,0,12,142,1,0,0,0,14,152,1,0,0,0,16,156,1,0,
        0,0,18,160,1,0,0,0,20,162,1,0,0,0,22,167,1,0,0,0,24,169,1,0,0,0,
        26,171,1,0,0,0,28,30,3,2,1,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,
        0,0,0,31,32,1,0,0,0,32,36,1,0,0,0,33,35,5,45,0,0,34,33,1,0,0,0,35,
        38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,1,1,0,0,0,38,36,1,0,0,
        0,39,61,3,4,2,0,40,61,3,6,3,0,41,61,3,8,4,0,42,61,3,20,10,0,43,61,
        3,14,7,0,44,61,3,10,5,0,45,61,3,12,6,0,46,61,5,13,0,0,47,48,5,40,
        0,0,48,53,3,2,1,0,49,50,5,44,0,0,50,52,3,2,1,0,51,49,1,0,0,0,52,
        55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,53,1,0,0,
        0,56,57,5,41,0,0,57,61,1,0,0,0,58,61,5,6,0,0,59,61,5,9,0,0,60,39,
        1,0,0,0,60,40,1,0,0,0,60,41,1,0,0,0,60,42,1,0,0,0,60,43,1,0,0,0,
        60,44,1,0,0,0,60,45,1,0,0,0,60,46,1,0,0,0,60,47,1,0,0,0,60,58,1,
        0,0,0,60,59,1,0,0,0,61,3,1,0,0,0,62,63,5,21,0,0,63,64,5,40,0,0,64,
        65,3,18,9,0,65,66,5,41,0,0,66,69,3,26,13,0,67,68,5,22,0,0,68,70,
        3,26,13,0,69,67,1,0,0,0,69,70,1,0,0,0,70,78,1,0,0,0,71,72,5,21,0,
        0,72,73,5,40,0,0,73,74,3,18,9,0,74,75,5,41,0,0,75,76,5,1,0,0,76,
        78,1,0,0,0,77,62,1,0,0,0,77,71,1,0,0,0,78,5,1,0,0,0,79,80,5,24,0,
        0,80,81,5,40,0,0,81,82,3,18,9,0,82,83,5,41,0,0,83,84,3,26,13,0,84,
        7,1,0,0,0,85,86,5,23,0,0,86,87,3,26,13,0,87,88,5,24,0,0,88,89,5,
        40,0,0,89,90,3,18,9,0,90,91,5,41,0,0,91,9,1,0,0,0,92,93,5,14,0,0,
        93,94,5,40,0,0,94,95,3,2,1,0,95,96,5,41,0,0,96,134,1,0,0,0,97,98,
        5,15,0,0,98,99,5,40,0,0,99,100,3,2,1,0,100,101,5,44,0,0,101,102,
        3,2,1,0,102,103,5,41,0,0,103,134,1,0,0,0,104,105,5,16,0,0,105,106,
        5,40,0,0,106,107,3,2,1,0,107,108,5,41,0,0,108,134,1,0,0,0,109,110,
        5,17,0,0,110,111,5,40,0,0,111,112,3,2,1,0,112,113,5,44,0,0,113,114,
        3,2,1,0,114,115,5,41,0,0,115,134,1,0,0,0,116,117,5,19,0,0,117,118,
        5,40,0,0,118,119,3,2,1,0,119,120,5,41,0,0,120,134,1,0,0,0,121,122,
        5,18,0,0,122,123,5,40,0,0,123,124,3,2,1,0,124,125,5,44,0,0,125,126,
        5,20,0,0,126,127,5,41,0,0,127,134,1,0,0,0,128,129,5,26,0,0,129,130,
        5,40,0,0,130,131,3,2,1,0,131,132,5,41,0,0,132,134,1,0,0,0,133,92,
        1,0,0,0,133,97,1,0,0,0,133,104,1,0,0,0,133,109,1,0,0,0,133,116,1,
        0,0,0,133,121,1,0,0,0,133,128,1,0,0,0,134,11,1,0,0,0,135,136,6,6,
        -1,0,136,143,5,10,0,0,137,143,5,11,0,0,138,139,5,40,0,0,139,140,
        3,12,6,0,140,141,5,41,0,0,141,143,1,0,0,0,142,135,1,0,0,0,142,137,
        1,0,0,0,142,138,1,0,0,0,143,149,1,0,0,0,144,145,10,4,0,0,145,146,
        7,0,0,0,146,148,3,12,6,5,147,144,1,0,0,0,148,151,1,0,0,0,149,147,
        1,0,0,0,149,150,1,0,0,0,150,13,1,0,0,0,151,149,1,0,0,0,152,153,5,
        46,0,0,153,154,3,16,8,0,154,155,3,18,9,0,155,15,1,0,0,0,156,157,
        7,1,0,0,157,17,1,0,0,0,158,161,3,14,7,0,159,161,3,24,12,0,160,158,
        1,0,0,0,160,159,1,0,0,0,161,19,1,0,0,0,162,163,3,22,11,0,163,164,
        7,2,0,0,164,165,5,32,0,0,165,166,7,3,0,0,166,21,1,0,0,0,167,168,
        7,4,0,0,168,23,1,0,0,0,169,170,7,5,0,0,170,25,1,0,0,0,171,175,5,
        42,0,0,172,174,3,2,1,0,173,172,1,0,0,0,174,177,1,0,0,0,175,173,1,
        0,0,0,175,176,1,0,0,0,176,178,1,0,0,0,177,175,1,0,0,0,178,179,5,
        43,0,0,179,27,1,0,0,0,11,31,36,53,60,69,77,133,142,149,160,175
    ]

class CompiladorParser ( Parser ):

    grammarFileName = "Compilador.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'int'", "'float'", "'void'", "'string'", 
                     "<INVALID>", "'TRUE'", "'FALSE'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'DIGITAL_READ'", 
                     "'DIGITAL_WRITE'", "'ANALOG_READ'", "'ANALOG_WRITE'", 
                     "'PIN_MODE'", "'PIN_TYPE'", "<INVALID>", "'IF'", "'ELSE'", 
                     "'DO'", "'WHILE'", "'EQEQ'", "'DELAY'", "'BREAK'", 
                     "'*'", "'/'", "'+'", "'-'", "'='", "'=='", "'!='", 
                     "'<='", "'<'", "'>'", "'>='", "'\"'", "'('", "')'", 
                     "'{'", "'}'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "INT", "FLOAT16", "VOID", 
                      "STRING", "BOOL", "TRUE", "FALSE", "WS", "TYPE_INT", 
                      "TYPE_REAL", "TYPE_CHAR", "TYPE_STRING", "DIGITAL_READ", 
                      "DIGITAL_WRITE", "ANALOG_READ", "ANALOG_WRITE", "PIN_MODE", 
                      "PIN_TYPE", "PIN_TYPE_", "IF", "ELSE", "DO", "WHILE", 
                      "EQEQ", "DELAY", "BREAK", "ASTERISK", "SLASH", "PLUS", 
                      "MINUS", "ATT", "EQUAL", "NOTEQUAL", "LESSTHENOP", 
                      "LESS", "BIGGER", "BIGGERTHENOP", "QUOTATION_MARKS", 
                      "LBRACE", "RBRACE", "LBRACE_P", "RBRACE_P", "COMMA", 
                      "NEWLINE", "ID" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_if_stmt = 2
    RULE_while_stmt = 3
    RULE_do_while_stmt = 4
    RULE_stmt_2 = 5
    RULE_expr_arithmetic = 6
    RULE_comparison_expr = 7
    RULE_comparison_operator = 8
    RULE_expr = 9
    RULE_variable_declaration = 10
    RULE_type = 11
    RULE_id_expr = 12
    RULE_block = 13

    ruleNames =  [ "prog", "stmt", "if_stmt", "while_stmt", "do_while_stmt", 
                   "stmt_2", "expr_arithmetic", "comparison_expr", "comparison_operator", 
                   "expr", "variable_declaration", "type", "id_expr", "block" ]

    EOF = Token.EOF
    T__0=1
    INT=2
    FLOAT16=3
    VOID=4
    STRING=5
    BOOL=6
    TRUE=7
    FALSE=8
    WS=9
    TYPE_INT=10
    TYPE_REAL=11
    TYPE_CHAR=12
    TYPE_STRING=13
    DIGITAL_READ=14
    DIGITAL_WRITE=15
    ANALOG_READ=16
    ANALOG_WRITE=17
    PIN_MODE=18
    PIN_TYPE=19
    PIN_TYPE_=20
    IF=21
    ELSE=22
    DO=23
    WHILE=24
    EQEQ=25
    DELAY=26
    BREAK=27
    ASTERISK=28
    SLASH=29
    PLUS=30
    MINUS=31
    ATT=32
    EQUAL=33
    NOTEQUAL=34
    LESSTHENOP=35
    LESS=36
    BIGGER=37
    BIGGERTHENOP=38
    QUOTATION_MARKS=39
    LBRACE=40
    RBRACE=41
    LBRACE_P=42
    RBRACE_P=43
    COMMA=44
    NEWLINE=45
    ID=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.StmtContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.StmtContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(CompiladorParser.NEWLINE)
            else:
                return self.getToken(CompiladorParser.NEWLINE, i)

        def getRuleIndex(self):
            return CompiladorParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = CompiladorParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.stmt()
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 71468351221372) != 0)):
                    break

            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 33
                self.match(CompiladorParser.NEWLINE)
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt(self):
            return self.getTypedRuleContext(CompiladorParser.If_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(CompiladorParser.While_stmtContext,0)


        def do_while_stmt(self):
            return self.getTypedRuleContext(CompiladorParser.Do_while_stmtContext,0)


        def variable_declaration(self):
            return self.getTypedRuleContext(CompiladorParser.Variable_declarationContext,0)


        def comparison_expr(self):
            return self.getTypedRuleContext(CompiladorParser.Comparison_exprContext,0)


        def stmt_2(self):
            return self.getTypedRuleContext(CompiladorParser.Stmt_2Context,0)


        def expr_arithmetic(self):
            return self.getTypedRuleContext(CompiladorParser.Expr_arithmeticContext,0)


        def TYPE_STRING(self):
            return self.getToken(CompiladorParser.TYPE_STRING, 0)

        def LBRACE(self):
            return self.getToken(CompiladorParser.LBRACE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.StmtContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.StmtContext,i)


        def RBRACE(self):
            return self.getToken(CompiladorParser.RBRACE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CompiladorParser.COMMA)
            else:
                return self.getToken(CompiladorParser.COMMA, i)

        def BOOL(self):
            return self.getToken(CompiladorParser.BOOL, 0)

        def WS(self):
            return self.getToken(CompiladorParser.WS, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = CompiladorParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.if_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.while_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.do_while_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 42
                self.variable_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 43
                self.comparison_expr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 44
                self.stmt_2()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 45
                self.expr_arithmetic(0)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 46
                self.match(CompiladorParser.TYPE_STRING)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 47
                self.match(CompiladorParser.LBRACE)
                self.state = 48
                self.stmt()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==44:
                    self.state = 49
                    self.match(CompiladorParser.COMMA)
                    self.state = 50
                    self.stmt()
                    self.state = 55
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 56
                self.match(CompiladorParser.RBRACE)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 58
                self.match(CompiladorParser.BOOL)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 59
                self.match(CompiladorParser.WS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CompiladorParser.IF, 0)

        def LBRACE(self):
            return self.getToken(CompiladorParser.LBRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(CompiladorParser.ExprContext,0)


        def RBRACE(self):
            return self.getToken(CompiladorParser.RBRACE, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.BlockContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(CompiladorParser.ELSE, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)




    def if_stmt(self):

        localctx = CompiladorParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.match(CompiladorParser.IF)
                self.state = 63
                self.match(CompiladorParser.LBRACE)
                self.state = 64
                self.expr()
                self.state = 65
                self.match(CompiladorParser.RBRACE)
                self.state = 66
                self.block()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==22:
                    self.state = 67
                    self.match(CompiladorParser.ELSE)
                    self.state = 68
                    self.block()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.match(CompiladorParser.IF)
                self.state = 72
                self.match(CompiladorParser.LBRACE)
                self.state = 73
                self.expr()
                self.state = 74
                self.match(CompiladorParser.RBRACE)
                self.state = 75
                self.match(CompiladorParser.T__0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(CompiladorParser.WHILE, 0)

        def LBRACE(self):
            return self.getToken(CompiladorParser.LBRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(CompiladorParser.ExprContext,0)


        def RBRACE(self):
            return self.getToken(CompiladorParser.RBRACE, 0)

        def block(self):
            return self.getTypedRuleContext(CompiladorParser.BlockContext,0)


        def getRuleIndex(self):
            return CompiladorParser.RULE_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stmt" ):
                listener.enterWhile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stmt" ):
                listener.exitWhile_stmt(self)




    def while_stmt(self):

        localctx = CompiladorParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(CompiladorParser.WHILE)
            self.state = 80
            self.match(CompiladorParser.LBRACE)
            self.state = 81
            self.expr()
            self.state = 82
            self.match(CompiladorParser.RBRACE)
            self.state = 83
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(CompiladorParser.DO, 0)

        def block(self):
            return self.getTypedRuleContext(CompiladorParser.BlockContext,0)


        def WHILE(self):
            return self.getToken(CompiladorParser.WHILE, 0)

        def LBRACE(self):
            return self.getToken(CompiladorParser.LBRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(CompiladorParser.ExprContext,0)


        def RBRACE(self):
            return self.getToken(CompiladorParser.RBRACE, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_do_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDo_while_stmt" ):
                listener.enterDo_while_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDo_while_stmt" ):
                listener.exitDo_while_stmt(self)




    def do_while_stmt(self):

        localctx = CompiladorParser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(CompiladorParser.DO)
            self.state = 86
            self.block()
            self.state = 87
            self.match(CompiladorParser.WHILE)
            self.state = 88
            self.match(CompiladorParser.LBRACE)
            self.state = 89
            self.expr()
            self.state = 90
            self.match(CompiladorParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGITAL_READ(self):
            return self.getToken(CompiladorParser.DIGITAL_READ, 0)

        def LBRACE(self):
            return self.getToken(CompiladorParser.LBRACE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.StmtContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.StmtContext,i)


        def RBRACE(self):
            return self.getToken(CompiladorParser.RBRACE, 0)

        def DIGITAL_WRITE(self):
            return self.getToken(CompiladorParser.DIGITAL_WRITE, 0)

        def COMMA(self):
            return self.getToken(CompiladorParser.COMMA, 0)

        def ANALOG_READ(self):
            return self.getToken(CompiladorParser.ANALOG_READ, 0)

        def ANALOG_WRITE(self):
            return self.getToken(CompiladorParser.ANALOG_WRITE, 0)

        def PIN_TYPE(self):
            return self.getToken(CompiladorParser.PIN_TYPE, 0)

        def PIN_MODE(self):
            return self.getToken(CompiladorParser.PIN_MODE, 0)

        def PIN_TYPE_(self):
            return self.getToken(CompiladorParser.PIN_TYPE_, 0)

        def DELAY(self):
            return self.getToken(CompiladorParser.DELAY, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_stmt_2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_2" ):
                listener.enterStmt_2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_2" ):
                listener.exitStmt_2(self)




    def stmt_2(self):

        localctx = CompiladorParser.Stmt_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stmt_2)
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(CompiladorParser.DIGITAL_READ)
                self.state = 93
                self.match(CompiladorParser.LBRACE)
                self.state = 94
                self.stmt()
                self.state = 95
                self.match(CompiladorParser.RBRACE)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.match(CompiladorParser.DIGITAL_WRITE)
                self.state = 98
                self.match(CompiladorParser.LBRACE)
                self.state = 99
                self.stmt()
                self.state = 100
                self.match(CompiladorParser.COMMA)
                self.state = 101
                self.stmt()
                self.state = 102
                self.match(CompiladorParser.RBRACE)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 104
                self.match(CompiladorParser.ANALOG_READ)
                self.state = 105
                self.match(CompiladorParser.LBRACE)
                self.state = 106
                self.stmt()
                self.state = 107
                self.match(CompiladorParser.RBRACE)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 109
                self.match(CompiladorParser.ANALOG_WRITE)
                self.state = 110
                self.match(CompiladorParser.LBRACE)
                self.state = 111
                self.stmt()
                self.state = 112
                self.match(CompiladorParser.COMMA)
                self.state = 113
                self.stmt()
                self.state = 114
                self.match(CompiladorParser.RBRACE)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 5)
                self.state = 116
                self.match(CompiladorParser.PIN_TYPE)
                self.state = 117
                self.match(CompiladorParser.LBRACE)
                self.state = 118
                self.stmt()
                self.state = 119
                self.match(CompiladorParser.RBRACE)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 6)
                self.state = 121
                self.match(CompiladorParser.PIN_MODE)
                self.state = 122
                self.match(CompiladorParser.LBRACE)
                self.state = 123
                self.stmt()
                self.state = 124
                self.match(CompiladorParser.COMMA)
                self.state = 125
                self.match(CompiladorParser.PIN_TYPE_)
                self.state = 126
                self.match(CompiladorParser.RBRACE)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 7)
                self.state = 128
                self.match(CompiladorParser.DELAY)
                self.state = 129
                self.match(CompiladorParser.LBRACE)
                self.state = 130
                self.stmt()
                self.state = 131
                self.match(CompiladorParser.RBRACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_arithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_INT(self):
            return self.getToken(CompiladorParser.TYPE_INT, 0)

        def TYPE_REAL(self):
            return self.getToken(CompiladorParser.TYPE_REAL, 0)

        def LBRACE(self):
            return self.getToken(CompiladorParser.LBRACE, 0)

        def expr_arithmetic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.Expr_arithmeticContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.Expr_arithmeticContext,i)


        def RBRACE(self):
            return self.getToken(CompiladorParser.RBRACE, 0)

        def PLUS(self):
            return self.getToken(CompiladorParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(CompiladorParser.MINUS, 0)

        def ASTERISK(self):
            return self.getToken(CompiladorParser.ASTERISK, 0)

        def SLASH(self):
            return self.getToken(CompiladorParser.SLASH, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_expr_arithmetic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_arithmetic" ):
                listener.enterExpr_arithmetic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_arithmetic" ):
                listener.exitExpr_arithmetic(self)



    def expr_arithmetic(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CompiladorParser.Expr_arithmeticContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr_arithmetic, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 136
                self.match(CompiladorParser.TYPE_INT)
                pass
            elif token in [11]:
                self.state = 137
                self.match(CompiladorParser.TYPE_REAL)
                pass
            elif token in [40]:
                self.state = 138
                self.match(CompiladorParser.LBRACE)
                self.state = 139
                self.expr_arithmetic(0)
                self.state = 140
                self.match(CompiladorParser.RBRACE)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 149
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CompiladorParser.Expr_arithmeticContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_arithmetic)
                    self.state = 144
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 145
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4026531840) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 146
                    self.expr_arithmetic(5) 
                self.state = 151
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Comparison_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CompiladorParser.ID, 0)

        def comparison_operator(self):
            return self.getTypedRuleContext(CompiladorParser.Comparison_operatorContext,0)


        def expr(self):
            return self.getTypedRuleContext(CompiladorParser.ExprContext,0)


        def getRuleIndex(self):
            return CompiladorParser.RULE_comparison_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison_expr" ):
                listener.enterComparison_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison_expr" ):
                listener.exitComparison_expr(self)




    def comparison_expr(self):

        localctx = CompiladorParser.Comparison_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comparison_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(CompiladorParser.ID)
            self.state = 153
            self.comparison_operator()
            self.state = 154
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comparison_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(CompiladorParser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(CompiladorParser.NOTEQUAL, 0)

        def LESSTHENOP(self):
            return self.getToken(CompiladorParser.LESSTHENOP, 0)

        def BIGGERTHENOP(self):
            return self.getToken(CompiladorParser.BIGGERTHENOP, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_comparison_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison_operator" ):
                listener.enterComparison_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison_operator" ):
                listener.exitComparison_operator(self)




    def comparison_operator(self):

        localctx = CompiladorParser.Comparison_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comparison_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 335007449088) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison_expr(self):
            return self.getTypedRuleContext(CompiladorParser.Comparison_exprContext,0)


        def id_expr(self):
            return self.getTypedRuleContext(CompiladorParser.Id_exprContext,0)


        def getRuleIndex(self):
            return CompiladorParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = CompiladorParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.comparison_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.id_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(CompiladorParser.TypeContext,0)


        def ATT(self):
            return self.getToken(CompiladorParser.ATT, 0)

        def ID(self):
            return self.getToken(CompiladorParser.ID, 0)

        def TYPE_CHAR(self):
            return self.getToken(CompiladorParser.TYPE_CHAR, 0)

        def TYPE_STRING(self):
            return self.getToken(CompiladorParser.TYPE_STRING, 0)

        def TYPE_INT(self):
            return self.getToken(CompiladorParser.TYPE_INT, 0)

        def TYPE_REAL(self):
            return self.getToken(CompiladorParser.TYPE_REAL, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declaration" ):
                listener.enterVariable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declaration" ):
                listener.exitVariable_declaration(self)




    def variable_declaration(self):

        localctx = CompiladorParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_variable_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.type_()
            self.state = 163
            _la = self._input.LA(1)
            if not(_la==12 or _la==46):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 164
            self.match(CompiladorParser.ATT)
            self.state = 165
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 11264) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CompiladorParser.INT, 0)

        def FLOAT16(self):
            return self.getToken(CompiladorParser.FLOAT16, 0)

        def BOOL(self):
            return self.getToken(CompiladorParser.BOOL, 0)

        def VOID(self):
            return self.getToken(CompiladorParser.VOID, 0)

        def STRING(self):
            return self.getToken(CompiladorParser.STRING, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = CompiladorParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 124) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CompiladorParser.ID, 0)

        def TYPE_INT(self):
            return self.getToken(CompiladorParser.TYPE_INT, 0)

        def TYPE_REAL(self):
            return self.getToken(CompiladorParser.TYPE_REAL, 0)

        def BOOL(self):
            return self.getToken(CompiladorParser.BOOL, 0)

        def TYPE_STRING(self):
            return self.getToken(CompiladorParser.TYPE_STRING, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_id_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_expr" ):
                listener.enterId_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_expr" ):
                listener.exitId_expr(self)




    def id_expr(self):

        localctx = CompiladorParser.Id_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_id_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 70368744188992) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE_P(self):
            return self.getToken(CompiladorParser.LBRACE_P, 0)

        def RBRACE_P(self):
            return self.getToken(CompiladorParser.RBRACE_P, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.StmtContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.StmtContext,i)


        def getRuleIndex(self):
            return CompiladorParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = CompiladorParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(CompiladorParser.LBRACE_P)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 71468351221372) != 0):
                self.state = 172
                self.stmt()
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 178
            self.match(CompiladorParser.RBRACE_P)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_arithmetic_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_arithmetic_sempred(self, localctx:Expr_arithmeticContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         




