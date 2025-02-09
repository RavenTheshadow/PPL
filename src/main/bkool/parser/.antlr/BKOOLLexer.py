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
        4,0,12,63,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,
        6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,
        1,11,1,11,1,11,0,0,12,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,
        10,21,11,23,12,1,0,2,2,0,65,90,97,122,3,0,9,10,13,13,32,32,62,0,
        1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,
        0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,
        0,0,0,0,23,1,0,0,0,1,25,1,0,0,0,3,29,1,0,0,0,5,35,1,0,0,0,7,37,1,
        0,0,0,9,39,1,0,0,0,11,41,1,0,0,0,13,43,1,0,0,0,15,48,1,0,0,0,17,
        50,1,0,0,0,19,54,1,0,0,0,21,57,1,0,0,0,23,60,1,0,0,0,25,26,5,105,
        0,0,26,27,5,110,0,0,27,28,5,116,0,0,28,2,1,0,0,0,29,30,5,102,0,0,
        30,31,5,108,0,0,31,32,5,111,0,0,32,33,5,97,0,0,33,34,5,116,0,0,34,
        4,1,0,0,0,35,36,5,44,0,0,36,6,1,0,0,0,37,38,5,59,0,0,38,8,1,0,0,
        0,39,40,5,40,0,0,40,10,1,0,0,0,41,42,5,41,0,0,42,12,1,0,0,0,43,44,
        5,98,0,0,44,45,5,111,0,0,45,46,5,100,0,0,46,47,5,121,0,0,47,14,1,
        0,0,0,48,49,7,0,0,0,49,16,1,0,0,0,50,51,7,1,0,0,51,52,1,0,0,0,52,
        53,6,8,0,0,53,18,1,0,0,0,54,55,9,0,0,0,55,56,6,9,1,0,56,20,1,0,0,
        0,57,58,9,0,0,0,58,59,6,10,2,0,59,22,1,0,0,0,60,61,9,0,0,0,61,62,
        6,11,3,0,62,24,1,0,0,0,1,0,4,6,0,0,1,9,0,1,10,1,1,11,2
    ]

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
            "'int'", "'float'", "','", "';'", "'('", "')'", "'body'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
     


