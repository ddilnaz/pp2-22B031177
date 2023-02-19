class CycleIterator():
    def __init__(self,data,max_time):
        self.data = data 
        self.max_time = max_time
        self.cnt = 0

    def __next__(self):
        if self.cnt >= self.max_time:
            raise StopIteration
        value = self.data[self.cnt % len(self.data)]
        self.cnt +=1
        return value

class Cycle():
    def __init__ (self , data , max_time):
        self.data = data 
        self.max_time = max_time

    def __iter__ (self):
        return CycleIterator(self.data , self.max_time)

c = Cycle("ooo", 10)
print (list(c))