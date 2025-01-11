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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("\66\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6")
        buf.write("\2\17\n\2\r\2\16\2\20\3\2\7\2\24\n\2\f\2\16\2\27\13\2")
        buf.write("\3\2\7\2\32\n\2\f\2\16\2\35\13\2\3\2\7\2 \n\2\f\2\16\2")
        buf.write("#\13\2\3\2\3\2\3\3\6\3(\n\3\r\3\16\3)\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\6\3\6\3\6\2\2\7\3\3\5\4\7\5\t\6\13")
        buf.write("\7\3\2\6\3\2\62;\3\2ch\3\2CH\5\2\13\f\17\17\"\"\2:\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\3\16\3\2\2\2\5\'\3\2\2\2\7-\3\2\2\2\t\60\3\2\2\2")
        buf.write("\13\63\3\2\2\2\r\17\t\2\2\2\16\r\3\2\2\2\17\20\3\2\2\2")
        buf.write("\20\16\3\2\2\2\20\21\3\2\2\2\21\25\3\2\2\2\22\24\t\3\2")
        buf.write("\2\23\22\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2")
        buf.write("\2\2\26\33\3\2\2\2\27\25\3\2\2\2\30\32\t\4\2\2\31\30\3")
        buf.write("\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34!\3")
        buf.write("\2\2\2\35\33\3\2\2\2\36 \t\2\2\2\37\36\3\2\2\2 #\3\2\2")
        buf.write("\2!\37\3\2\2\2!\"\3\2\2\2\"$\3\2\2\2#!\3\2\2\2$%\b\2\2")
        buf.write("\2%\4\3\2\2\2&(\t\5\2\2\'&\3\2\2\2()\3\2\2\2)\'\3\2\2")
        buf.write("\2)*\3\2\2\2*+\3\2\2\2+,\b\3\3\2,\6\3\2\2\2-.\13\2\2\2")
        buf.write("./\b\4\4\2/\b\3\2\2\2\60\61\13\2\2\2\61\62\b\5\5\2\62")
        buf.write("\n\3\2\2\2\63\64\13\2\2\2\64\65\b\6\6\2\65\f\3\2\2\2\b")
        buf.write("\2\20\25\33!)\7\3\2\2\b\2\2\3\4\3\3\5\4\3\6\5")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    HEXA = 1
    WS = 2
    ERROR_CHAR = 3
    UNCLOSE_STRING = 4
    ILLEGAL_ESCAPE = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "HEXA", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "HEXA", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[0] = self.HEXA_action 
            actions[2] = self.ERROR_CHAR_action 
            actions[3] = self.UNCLOSE_STRING_action 
            actions[4] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def HEXA_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		if int(self.text, 16) % 2 != 0:
            			raise ErrorToken(self.text) 
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


