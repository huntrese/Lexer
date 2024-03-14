import unittest
from Tokenizer import * 
from Parser import *

class TokenizerTests(unittest.TestCase):
    def test_number(self):
        tokenizer = Tokenizer("123;")
        token = tokenizer.getNextToken()
        self.assertEqual(token['type'], 'NUMBER')
        self.assertEqual(token['value'], '123')

    def test_tokenizer(self):
        code = "42;\n10;"
        tokenizer = Tokenizer(code)
        while tokenizer.hasMoreTokens():
            token = tokenizer.getNextToken()
            print(token)

    
class ParserTests(unittest.TestCase):
    def test_numeric_literal(self):
        parser = Parser()
        program = parser.parse("123;")
        self.assertEqual(program, {
            'type': 'Program',
            'body': {
                'type': 'NumericLiteral',
                'value': 123
            }
        })


if __name__ == '__main__':
    unittest.main()
