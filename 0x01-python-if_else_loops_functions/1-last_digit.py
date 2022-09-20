#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last_digit = int(str(number)[-1])
else:
    last_digit = int(str(number)[-1])
    last_digit = -last_digit
msg = f"Last digit of {number:d} is {last_digit:d} "
if last_digit > 5:
    print(msg + "and is greater than 5")
elif last_digit == 0:
    print(msg + "and is 0")
elif last_digit < 6 and last_digit != 0:
    print(msg + "and is less than 6 and not 0")
