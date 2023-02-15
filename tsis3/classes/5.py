class Account: 
    def __init__(self, owner, balance = 0): 
        self.o = owner 
        self.b = balance    
    def __str__(self): 
        return ("Account owner: {} \nAccount balance: {}").format(self.o, self.b ) 
    def deposit(self, deposit): 
        self.b = self.b + deposit 
        print("+ {} \nYour current balance is {} tenge from AO KBTU".format(deposit,self.b)) 
    def withdraw(self, w): 
            if w > self.b: 
                print("Error, insufficient funds \nYour current balance is {}".format(self.b)) 
            else: 
                self.b = self.b - w 
                print("Withdrawal Accepted \nYour current balance is {}".format(self.b)) 
p = Account("DILNAZ") 
print(p) 
p.deposit(36660) 
x = int(input()) 
p.withdraw(x)