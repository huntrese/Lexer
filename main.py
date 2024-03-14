from Parser import *
import json
parser = Parser()
code = '''
# This is comment

42; 10;
'''
result = parser.parse(code)

print(json.dumps(result, indent=2)) 