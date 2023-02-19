def div_by_3_and_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
            
n = int(input())
for num in div_by_3_and_4(n):
    print(num)
