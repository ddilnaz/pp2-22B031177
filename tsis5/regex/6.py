import re

text=input()

ans=re.sub("[ ,.]","|",text)
print(ans)