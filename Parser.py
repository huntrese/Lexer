import json
from Tokenizer import *

class Parser:
    def parse(self, string):
        self._string = string
        self._tokenizer = Tokenizer(string)

        self._lookahead = self._tokenizer.getNextToken()

        return self.Program()
    
    def Program(self):
        return {
            "type": "Program",
            "body": self.Literal()
        }
    
    def NumericLiteral(self):
        token = self._eat("NUMBER")
        return {
            "type": "NumericLiteral",
            "value": int(token["value"])
        }
    
    def StringLiteral(self):
        token = self._eat("STRING")
        return {
            "type": "StringLiteral",
            "value": token["value"]
        }
    
    def Literal(self):
        match self._lookahead["type"]:
            case "STRING": return self.StringLiteral()
            case "NUMBER": return self.NumericLiteral()
      
    
    def _eat(self, tokenType):
        token = self._lookahead

        if token == None:
            raise SyntaxError(f"Unexpected end of input, expected {tokenType}.") 
    
        if token["type"] != tokenType:
            val = token["value"]
            raise SyntaxError(f"Unexpected token {val}, expected {tokenType}.")
        
        self._lookahead = self._tokenizer.getNextToken()

        return token

