#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# remainder = number % 10
if number < 0:
    r = number % -10
else:
    r = number % 10
if (r != 0 and r < 6):
    print(f"Last digit of {number} is {r} and is less than 6 and not 0")
elif (r == 0):
    print(f"Last digit of {number} is 0 and is 0")
elif (r != 0 and r > 6):
    print(f"Last digit of {number} is {r} and is greater than 5")
