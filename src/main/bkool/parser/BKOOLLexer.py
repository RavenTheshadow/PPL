# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("D\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\6\t\64\n\t\r\t")
        buf.write("\16\t\65\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\3\2\4\4\2C\\c|\5\2\13\f\17\17\"\"")
        buf.write("\2D\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3")
        buf.write("\2\2\2\5\35\3\2\2\2\7!\3\2\2\2\t\'\3\2\2\2\13)\3\2\2\2")
        buf.write("\r+\3\2\2\2\17-\3\2\2\2\21\63\3\2\2\2\23\67\3\2\2\2\25")
        buf.write(";\3\2\2\2\27>\3\2\2\2\31A\3\2\2\2\33\34\7=\2\2\34\4\3")
        buf.write("\2\2\2\35\36\7k\2\2\36\37\7p\2\2\37 \7v\2\2 \6\3\2\2\2")
        buf.write("!\"\7h\2\2\"#\7n\2\2#$\7q\2\2$%\7c\2\2%&\7v\2\2&\b\3\2")
        buf.write("\2\2\'(\7.\2\2(\n\3\2\2\2)*\7*\2\2*\f\3\2\2\2+,\7+\2\2")
        buf.write(",\16\3\2\2\2-.\7d\2\2./\7q\2\2/\60\7f\2\2\60\61\7{\2\2")
        buf.write("\61\20\3\2\2\2\62\64\t\2\2\2\63\62\3\2\2\2\64\65\3\2\2")
        buf.write("\2\65\63\3\2\2\2\65\66\3\2\2\2\66\22\3\2\2\2\678\t\3\2")
        buf.write("\289\3\2\2\29:\b\n\2\2:\24\3\2\2\2;<\13\2\2\2<=\b\13\3")
        buf.write("\2=\26\3\2\2\2>?\13\2\2\2?@\b\f\4\2@\30\3\2\2\2AB\13\2")
        buf.write("\2\2BC\b\r\5\2C\32\3\2\2\2\4\2\65\6\b\2\2\3\13\2\3\f\3")
        buf.write("\3\r\4")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    ID = 8
    WS = 9
    ERROR_CHAR = 10
    UNCLOSE_STRING = 11
    ILLEGAL_ESCAPE = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'int'", "'float'", "','", "'('", "')'", "'body'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[9] = self.ERROR_CHAR_action 
            actions[10] = self.UNCLOSE_STRING_action 
            actions[11] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     


