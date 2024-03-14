import re

code = '''"""This is a multiline comment
or a docstring"""
print("Hello there")
'''

multi_line_comments = re.findall(r'^\""".*?"""', code, flags=re.DOTALL)

print(multi_line_comments)
# Output: ['"""This is a multiline comment\nor a docstring"""']
