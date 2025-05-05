#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 1
if number > 0:
    last_digit = number % 10
else:
    sign = -1
    last_digit = (number * sign) % 10
print(f"Last digit of {number} is ", end="")
if last_digit > 5:
    print(f"{last_digit * sign} and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print(f"{last_digit * sign} and is less than 6 and not 0")
else:
    print("0 and is 0")
