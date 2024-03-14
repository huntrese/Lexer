from Parser import *
import json
parser = Parser()
code = '''
# This is comment
# Another comment
42; 
'Hi';
'''
result = parser.parse(code)

print(json.dumps(result, indent=2)) 