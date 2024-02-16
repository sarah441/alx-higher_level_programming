#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10

description = ""  # Initialize an empty string to store the description

if last_digit > 5:
    description = "greater than 5"
elif last_digit == 0:
    description = "0"
else:
    description = "less than 6 and not 0"
print(f"Last digit of {number} is {last_digit} and is {description}")
