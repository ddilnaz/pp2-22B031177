import math 
class Point: 
    def __init__(self, x ,y ): 
        self.x = x 
        self.y = y 
    def move(self, z , z1): 
        self.x = self.x + z 
        self.y = self.y + z1  
    def __str__(self): 
        return f"({self.x};{self.y})" 
    def dic(self, x , y): 
        z = self.x - x 
        z1 = self.y - y 
        print((math.sqrt((z)**2 + (z1)**2))) 
print("Coordinates of first point") 
x1 = int(input()) 
y1 = int(input()) 
print("x =" , x1 , "y =" , y1) 
print("Coordinates of second point") 
x2 = int(input()) 
y2 = int(input()) 
print("x = " , x2 , "y = " , y2) 
p1 = Point(x1 , y1) 
p2 = Point(x2,y2) 
print("Distance between the first and second points:") 
p1.dic(x2 , y2) 
print("Moving along X at the first point") 
movep1x = int(input())  
print("Moving along Y at the first point") 
movep1y = int(input())  
print("Moving along X at the second point") 
movep2x = int(input())  
print("Moving along Y at the second point") 
movep2y = int(input())  
p1.move(movep1x,movep1y) 
p2.move(movep2x,movep2y) 
print("First point coordinates") 
print(p1) 
print("Second point coordinates") 
print(p2)