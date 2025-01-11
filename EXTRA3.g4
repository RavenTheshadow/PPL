grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

// Use ANTLR to write regular expressions describing PHP's
// integers (in decimal) which is a sequence of digits (0-9)
// starting with a non-zero digit or only a zero. Integer literals
// may contain underscores (_) between digits, for better readability
// of literals but these underscores are removed by PHP's scanner.
program:   EOF;

FILTER: [1-9] [0-9]* UNDERSCORE* {self.text = self.text.replace('_', '')};
fragment UNDERSCORE: '_' | [0-9];

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: . {raise ErrorToken(self.text)};
ILLEGAL_ESCAPE: . {raise ErrorToken(self.text)};