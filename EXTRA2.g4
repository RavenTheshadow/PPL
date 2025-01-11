grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

// Use ANTLR to write regular expressions describing a valid IPv4 address.
// It consists of exact 4 strings, whose length is from 1 to 3, of digits (0-9) but not starting with 0
// unless the string is 0. The strings are separated by one dot (.). 

program:   EOF;

IPV4: OCTET '.' OCTET '.' OCTET '.' OCTET;

fragment OCTET: '0' | [1] [0-9]? [0-9]? | [1-9] [0-9]? | [2] [0-4] [0-9] | '25' [0-5];

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: . {raise ErrorToken(self.text)};
ILLEGAL_ESCAPE: . {raise ErrorToken(self.text)};