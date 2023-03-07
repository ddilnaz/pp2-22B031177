import string

for letter in string.ascii_uppercase:
    filename = letter + ".txt"
    with open(filename, "w") as file:
        print( filename)