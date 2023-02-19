def squares_generator(N):
    for i in range(N):
        yield i ** 2

for square in squares_generator(10):
    print(square)