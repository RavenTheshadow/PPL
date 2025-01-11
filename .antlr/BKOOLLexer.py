# Generated from d:/HK242/PPL/CODE/initial/EXTRA4.g4 by ANTLR 4.13.1
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
        4,0,5,52,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,13,
        8,0,11,0,12,0,14,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,5,0,24,8,0,
        10,0,12,0,27,9,0,1,0,5,0,30,8,0,10,0,12,0,33,9,0,1,0,1,0,1,1,4,1,
        38,8,1,11,1,12,1,39,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,
        0,0,5,1,1,3,2,5,3,7,4,9,5,1,0,4,1,0,48,57,1,0,97,102,1,0,65,70,3,
        0,9,10,13,13,32,32,56,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,
        0,0,0,0,9,1,0,0,0,1,12,1,0,0,0,3,37,1,0,0,0,5,43,1,0,0,0,7,46,1,
        0,0,0,9,49,1,0,0,0,11,13,7,0,0,0,12,11,1,0,0,0,13,14,1,0,0,0,14,
        12,1,0,0,0,14,15,1,0,0,0,15,19,1,0,0,0,16,18,7,1,0,0,17,16,1,0,0,
        0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,25,1,0,0,0,21,19,
        1,0,0,0,22,24,7,2,0,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,
        25,26,1,0,0,0,26,31,1,0,0,0,27,25,1,0,0,0,28,30,7,0,0,0,29,28,1,
        0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,34,1,0,0,0,33,
        31,1,0,0,0,34,35,6,0,0,0,35,2,1,0,0,0,36,38,7,3,0,0,37,36,1,0,0,
        0,38,39,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,41,1,0,0,0,41,42,
        6,1,1,0,42,4,1,0,0,0,43,44,9,0,0,0,44,45,6,2,2,0,45,6,1,0,0,0,46,
        47,9,0,0,0,47,48,6,3,3,0,48,8,1,0,0,0,49,50,9,0,0,0,50,51,6,4,4,
        0,51,10,1,0,0,0,6,0,14,19,25,31,39,5,1,0,0,6,0,0,1,2,1,1,3,2,1,4,
        3
    ]

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

    grammarFileName = "EXTRA4.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
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

            		if int(self.text, 16) % 2 == 0:
            			return True
            		else:
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
     


