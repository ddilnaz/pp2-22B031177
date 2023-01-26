txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

txt = "banana"
x = txt.center(20,"p")
print(x)

txt = "qwerty asd zxc"
a = txt.count("asd")
print (a)

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)

txt = "My name is Ståle"
x = txt.encode()
print(x)

txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)

txt = "Hello my friends"
x = txt.upper()
print(x)

txt = "welcome to the jungle"
x = txt.split()
print(x)