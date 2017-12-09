# Brandon Coats
# 11/11/17
# CTI 110
# M6HW2

import random
import sys

def guessNumber():
    number=random.randint(1,1000)
    count=1
    guess= int(input("Enter a number between 1 and 1000: ") )

    while guess !=number:
        count+=1
        if guess > number:
            print("Too high try again!")
        elif guess < number:
            print("Too low try again!")

        guess = int(input("Try again! "))

    if guess == number:
        print("Great Job! You guessed the number in ", count, "tries!")

guessNumber()

again = str(input("Would you like to play again? (type y or n): "))
if again == "y":
    guessNumber()
else:
    sys.exit(0)
