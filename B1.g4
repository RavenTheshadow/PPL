grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}
// Use ANTLR to write regular expressions describing 
// Pascal strings are made up of a sequence of characters between single quotes: 'string'. 
// The single quote itself can appear as two single quotes back to back in a string: 'isn''t'.

program:   EOF;

REG : [a-z]+ [a-z0-9]*;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: . {raise ErrorToken(self.text)};
ILLEGAL_ESCAPE: . {raise ErrorToken(self.text)};