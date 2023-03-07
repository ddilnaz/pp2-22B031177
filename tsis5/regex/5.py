import re 

text = input()
pattern = r'a.*b$'
matches = re.search(pattern, text)
if matches is not None :
    print(matches)
else :
    print("does not match in pattern")