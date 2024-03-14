from Parser import *
parser = Parser()
result = parser.parse("'42'")

print(json.dumps(result, indent=2)) 