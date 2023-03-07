import os
print("Test a path exists or not:")
#C:\Users\Lenovo\Desktop\PP2 
path = input()
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))