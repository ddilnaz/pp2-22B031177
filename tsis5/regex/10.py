import re


text = input()

def camel_to_snake(text):
        str1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', str1).lower()
print(camel_to_snake(text))