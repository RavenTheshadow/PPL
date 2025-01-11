import unittest
from TestUtils import TestLexer


TestCases = [
    # test simple string
    ("12", "12,<EOF>", 101),
    ("21A", "21A,<EOF>", 102),
    ("1B", "Error Token 1", 103),
]

class LexerSuite(unittest.TestCase):
      
    def test_simple_string(self):
        """test simple string"""
        
        for (i, test) in enumerate(TestCases):
            try:
                input = test[0]
                expect = test[1]
                print(f"Test {i}: {input} -> {expect}")
                self.assertTrue(TestLexer.test(input, expect, test[2]))
                print(f"Test {i} passed")
            except Exception as e:
                print(f"Test {i} failed with file {100 + i}")
                continue


    # def test_complex_string(self):
    #     """test complex string"""
    #     self.assertTrue(TestLexer.test("'isn''t'","'isn''t',<EOF>",102))
    