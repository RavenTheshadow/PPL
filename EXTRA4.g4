grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

//Hãy dùng ANTLR để viết biểu thức chính qui cho token SHEXA mô tả các chuỗi số thập lục phân thoả mãn tất cả các yêu cầu sau:

//không rỗng tương ứng với một số nguyên chẵn có ký tự đầu tiên chỉ gồm các ký tự số không phân biệt
// chữ thường và hoa không sử dụng action khi viết biểu thức chính qui cho SHEXA Ví dụ: các chuỗi
// hợp lệ với SHEXA: 12, 21A, 3dC, 2

//Các chuỗi không hợp lệ với SHEXA: A12 (ký tự đầu tiên là chữ), 1B (ứng với 27 không phải là số nguyên chẵn)
program: EOF;

HEXA:
	[0-9]+ [a-f]* [A-F]* [0-9]* {
		if int(self.text, 16) % 2 == 0:
			return True
		else:
			raise ErrorToken(self.text)
	};

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: . {raise ErrorToken(self.text)};
ILLEGAL_ESCAPE: . {raise ErrorToken(self.text)};