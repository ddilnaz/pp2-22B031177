
import random

name = input("Hello! What is your name?\n")
print("Well, %s, I am thinking of a number between 1 and 20." % name)

secret = int(random.randint(1, 20))
input = int(input("Take a guess.\n"))
count = 1

while input != secret:
    if input < secret:
        print("Your guess is too low.")
    elif input > secret:
        print ("Your guess is too high.")
    input == int(input("Take a guess.\n"))
    count += 1

print ("Good job, %s! You guessed my number in %d guesses!" % (name, count))
