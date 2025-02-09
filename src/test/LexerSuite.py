import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
      
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int a, b,c;
float foo(int a; float c, d) body
float goo (float a, b) body"""
        expect = "successful"
        self.assertTrue(TestLexer.test(input,expect,101))


    # def test_complex_string(self):
    #     """test complex string"""
    #     self.assertTrue(TestLexer.test("'isn''t'","'isn''t',<EOF>",102))
    