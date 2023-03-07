def squares_generator(N):
    for i in range(N):
        yield i ** 2
san = int(input())
for k in squares_generator(san):
    print(k)