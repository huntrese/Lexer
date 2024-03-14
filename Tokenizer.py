class Tokenizer:    
    def __init__(self, string):
        self._string = string
        self._coursor = 0
    
    def hasMoreTokens(self):
        return self._coursor < len(self._string)
    
    def isEOF(self):
        return self._coursor == len(self._string)
    
    def getNextToken(self):
        if not self.hasMoreTokens():
            return None
        
        curr_string = self._string[self._coursor:]

        if curr_string.isdigit():
            number = ""
            while self.hasMoreTokens() and curr_string[self._coursor].isdigit():
                number += curr_string[self._coursor]
                self._coursor += 1

            return {
                "type": "NUMBER",
                "value": int(number)
            }
        
        if curr_string[0] == '"':
            string = ""
            while True:
                print(string)
                self._coursor += 1
                if self.isEOF() or curr_string[self._coursor] == '"':
                    break
                string += curr_string[self._coursor]

            return {
                "type": "STRING",
                "value": str(string)
            }



