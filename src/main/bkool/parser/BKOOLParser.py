# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write(".\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\6\2")
        buf.write("\17\n\2\r\2\16\2\20\3\2\3\2\3\3\3\3\3\3\3\3\7\3\31\n\3")
        buf.write("\f\3\16\3\34\13\3\3\4\3\4\3\4\3\4\3\4\3\4\7\4$\n\4\f\4")
        buf.write("\16\4\'\13\4\3\4\3\4\3\4\3\5\3\5\3\5\2\2\6\2\4\6\b\2\3")
        buf.write("\3\2\4\5\2-\2\16\3\2\2\2\4\24\3\2\2\2\6\35\3\2\2\2\b+")
        buf.write("\3\2\2\2\n\13\5\4\3\2\13\f\7\3\2\2\f\17\3\2\2\2\r\17\5")
        buf.write("\6\4\2\16\n\3\2\2\2\16\r\3\2\2\2\17\20\3\2\2\2\20\16\3")
        buf.write("\2\2\2\20\21\3\2\2\2\21\22\3\2\2\2\22\23\7\2\2\3\23\3")
        buf.write("\3\2\2\2\24\25\t\2\2\2\25\32\7\n\2\2\26\27\7\6\2\2\27")
        buf.write("\31\7\n\2\2\30\26\3\2\2\2\31\34\3\2\2\2\32\30\3\2\2\2")
        buf.write("\32\33\3\2\2\2\33\5\3\2\2\2\34\32\3\2\2\2\35\36\t\2\2")
        buf.write("\2\36\37\7\n\2\2\37 \7\7\2\2 %\5\4\3\2!\"\7\3\2\2\"$\5")
        buf.write("\4\3\2#!\3\2\2\2$\'\3\2\2\2%#\3\2\2\2%&\3\2\2\2&(\3\2")
        buf.write("\2\2\'%\3\2\2\2()\7\b\2\2)*\7\t\2\2*\7\3\2\2\2+,\7\t\2")
        buf.write("\2,\t\3\2\2\2\6\16\20\32%")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'int'", "'float'", "','", "'('", 
                     "')'", "'body'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_vardecl = 1
    RULE_funcdecl = 2
    RULE_body = 3

    ruleNames =  [ "program", "vardecl", "funcdecl", "body" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    ID=8
    WS=9
    ERROR_CHAR=10
    UNCLOSE_STRING=11
    ILLEGAL_ESCAPE=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.VardeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.VardeclContext,i)


        def funcdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.FuncdeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.FuncdeclContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 8
                    self.vardecl()
                    self.state = 9
                    self.match(BKOOLParser.T__0)
                    pass

                elif la_ == 2:
                    self.state = 11
                    self.funcdecl()
                    pass


                self.state = 14 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.T__1 or _la==BKOOLParser.T__2):
                    break

            self.state = 16
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = BKOOLParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.T__1 or _la==BKOOLParser.T__2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 19
            self.match(BKOOLParser.ID)
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.T__3:
                self.state = 20
                self.match(BKOOLParser.T__3)
                self.state = 21
                self.match(BKOOLParser.ID)
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.VardeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.VardeclContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = BKOOLParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.T__1 or _la==BKOOLParser.T__2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 28
            self.match(BKOOLParser.ID)
            self.state = 29
            self.match(BKOOLParser.T__4)
            self.state = 30
            self.vardecl()
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.T__0:
                self.state = 31
                self.match(BKOOLParser.T__0)
                self.state = 32
                self.vardecl()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.match(BKOOLParser.T__5)
            self.state = 39
            self.match(BKOOLParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKOOLParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BKOOLParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(BKOOLParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





