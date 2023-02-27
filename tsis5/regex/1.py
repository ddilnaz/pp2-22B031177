import re

pattern = r'ab*'

text = input()

match = re.search(pattern, text)

if match is not None :
    print(match)
else :
    print("does not match in pattern")