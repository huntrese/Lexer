import re

code = ''';
  some code;
'''

comments = re.findall(r"^;" , code, flags=re.MULTILINE)
print(comments)