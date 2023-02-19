def squares(a, b):
    for i in range(a, b+1):
        yield i**2

n=int(input())
m=int(input())
for num in squares(n, m):
    print(num)