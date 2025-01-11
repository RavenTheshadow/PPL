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

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

REAL : DIGIT + FRAC +  FIC? | DIGIT + FIC;
fragment DIGIT: [0-9]+;
fragment FRAC: '.' [0-9]+;
fragment FIC: ('e' | 'E') '-'? [0-9]+; 

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: . {raise ErrorToken(self.text)};
ILLEGAL_ESCAPE: . {raise ErrorToken(self.text)};