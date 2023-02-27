import re 

text = input()
pattern = r'^[A-Z]?[a-z]+$'

match = re.search(pattern, text)

if match is not None:
    print("cool")
else :
    print("one more time")