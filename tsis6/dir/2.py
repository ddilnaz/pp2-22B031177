import os
#"C:\Users\Lenovo\Desktop\PP2"
path = input()
#path exists
print(os.access(path, os.F_OK))
#is Readable
print(os.access(path, os.R_OK))
#is Wriable
print(os.access(path, os.W_OK))
#is Execuatble выполнить
print(os.access(path, os.X_OK))