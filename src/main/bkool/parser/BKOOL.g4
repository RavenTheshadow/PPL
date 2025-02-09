grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: (vardecl ';' | funcdecl)+ EOF;

vardecl:  ('int' | 'float') ID (',' ID)*;
funcdecl: ('int' | 'float') ID '(' vardecl (';' vardecl)* ')' 'body';



body: 'body';

ID: [a-zA-Z]+;

WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: . {raise ErrorToken(self.text)};
ILLEGAL_ESCAPE: . {raise ErrorToken(self.text)};