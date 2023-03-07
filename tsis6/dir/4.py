filename = input()  # replace with your file name
#C:\Users\Lenovo\Desktop\PP2\tsis6\dir\4.py 
with open(filename, "r") as file:
    count = 0
    for line in file:
        count += 1

print("The number of lines in path is: ", {count})