import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """float foo(int a, float c, d) body"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))