import re

text = input()

otvet = re.findall('[A-Z][^A-Z]*', text)
print(otvet)

