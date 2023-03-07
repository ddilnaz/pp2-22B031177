import re

text=input()

ans=re.sub(r"[ ,.]","|",text)
print(ans)