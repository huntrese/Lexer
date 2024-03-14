import json

class Parser:
    def parse(self, string):
        self.string = string

        return self.Program()
    
    def Program(self):
        return self.NumericLiteral()
    
    def NumericLiteral(self):
        return {
            "type": "NumericLiteral",
            "value": int(self.string)
        }

