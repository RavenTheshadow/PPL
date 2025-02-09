grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: (vardecl | funcdecl)+ EOF;

vardecl: 'vardecl' ;

funcdecl: 'funcdecl' ;

WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: . {raise ErrorToken(self.text)};
ILLEGAL_ESCAPE: . {raise ErrorToken(self.text)};