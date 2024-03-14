from Parser import *
import json
parser = Parser()
code = '''
# This is comment
# This is comment
'HI'
'''
result = parser.parse(code)

print(json.dumps(result, indent=2)) 