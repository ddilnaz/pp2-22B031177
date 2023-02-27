import re


text = input()

def snake_to_camel(txt):
    pattern = re.findall("[a-z]+",text)
    help = ""
    for i in pattern:
        help+=i[0].upper()+i[1:len(i)]
    return help
print(snake_to_camel(text))