import math
def area(h,a1,a2):
    return 0.5 *h*(a1+a2)
hei = int(input())
a1 = int(input())
a2 = int(input())
s = area(hei,a1,a2)
print("Height : ", hei)
print("Base, first value:" , a1)
print("Base, second value:" , a2)
print("Expected Output:" , s)