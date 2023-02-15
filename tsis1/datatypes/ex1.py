x = 5
print(type(x))

x=9.9
print(type(x)) 

x = 1j
print(x)
print(type(x)) 

x = ["apple", "banana", "cherry"]
print(x)
print(type(x))
#list

x = ("apple", "banana", "cherry")
print(x)
print(type(x)) 
#tuple

x = range(6)
print(x)
print(type(x)) 
#range

x = {"name" : "John", "age" : 36}
print(x)
print(type(x)) 
#dict

x = {"apple", "banana", "cherry"}
print(x)
print(type(x)) 
#set

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x)) 
#frozenset

x = True
print(x)
print(type(x))
#bool 

x = b"Hello"
print(x)
print(type(x)) 
#bytes

x = bytearray(5)
print(x)
print(type(x)) 
#bytes

x = memoryview(bytes(5))
print(x)
print(type(x)) 
#memoryview

x = None
print(x)
print(type(x)) 
#NoneType

x = str("Hello World")
print(x)
print(type(x)) 
#str