def is_prime(number):
    for i in range(2, sqrt(number) + 1):
        if number % i == 0:
            return False

    return number > 1