import re
pattern = r'ab*'
text = str(input())
match = re.search(pattern, text)
if match is not None :
    print("GOOD JOB")
else :
    print("NO CONNECTON")