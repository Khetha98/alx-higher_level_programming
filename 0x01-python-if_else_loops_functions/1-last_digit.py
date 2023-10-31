#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
remainder = number % 10
if (remainder != 0 and remainder < 6):
    print(f"Last digit of {number} is {remainder} and is less than 6 and not 0")
elif (remainder == 0):
    print(f"Last digit of {number} is 0 and is 0")
elif (remainder != 0 and remainder > 6):
    print(f"Last digit of {number} is {remainder} and is greater than 5")

