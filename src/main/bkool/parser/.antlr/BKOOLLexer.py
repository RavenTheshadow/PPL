# Generated from d:/HK242/PPL/CODE/initial/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,4,25,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,11,8,0,11,
        0,12,0,12,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,0,0,4,1,1,
        3,2,5,3,7,4,1,0,1,3,0,9,10,13,13,32,32,25,0,1,1,0,0,0,0,3,1,0,0,
        0,0,5,1,0,0,0,0,7,1,0,0,0,1,10,1,0,0,0,3,16,1,0,0,0,5,19,1,0,0,0,
        7,22,1,0,0,0,9,11,7,0,0,0,10,9,1,0,0,0,11,12,1,0,0,0,12,10,1,0,0,
        0,12,13,1,0,0,0,13,14,1,0,0,0,14,15,6,0,0,0,15,2,1,0,0,0,16,17,9,
        0,0,0,17,18,6,1,1,0,18,4,1,0,0,0,19,20,9,0,0,0,20,21,6,2,2,0,21,
        6,1,0,0,0,22,23,9,0,0,0,23,24,6,3,3,0,24,8,1,0,0,0,2,0,12,4,6,0,
        0,1,1,0,1,2,1,1,3,2
    ]

class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    ERROR_CHAR = 2
    UNCLOSE_STRING = 3
    ILLEGAL_ESCAPE = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[1] = self.ERROR_CHAR_action 
            actions[2] = self.UNCLOSE_STRING_action 
            actions[3] = self.ILLEGAL_ESCAPE_action 
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
     


