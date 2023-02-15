def is_prime(i): 
    if i<2: 
        return False 
    else: 
        for x in range(2, i): 
            if i % x == 0: 
                return False 
        return True 
 
listt=[x for x in range(100)] 
listt=list(filter(lambda x: is_prime(x), listt)) 
print(listt)