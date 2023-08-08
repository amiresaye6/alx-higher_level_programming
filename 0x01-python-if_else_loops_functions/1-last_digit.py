#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number % 10
if number < 0:
    nn = (-1 * number) % 10
    print(f"Last digit of {number} is {-nn} and is less than 6 and not 0")
else:
    if n > 5:
        print(f"Last digit of {number} is {n} and is greater than 5")
    elif n == 0:
        print(f"Last digit of {number} is {n} and is 0")
    elif n < 6:
        print(f"Last digit of {number} is {n} and is less than 6 and not 0")
