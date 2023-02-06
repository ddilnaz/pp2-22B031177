class Shape: 
    def __init__(self) -> None: 
        pass 
    def area(self): 
        return 0 
class sqare(Shape): 
    def __init__(self,length) -> None: 
        super().__init__() 
        self.l = length 
    def area(self): 
        return self.l * self.l 
x = int(input()) 
p = sqare(x) 
print(p.area())