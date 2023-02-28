""""
Program: Prime Calculator
Author: Jacob Dimoff
Date:12/11/22
filename: primeCalculator.py
Purpose: To deterimine if an user inputed numebr is a prime number or not
"""

import sys

# User input to for the program. Caste as str for decimal check
num = str((input("Pick a number: ")))

# Decimal check
TF = str.isdecimal(num)

# If num is false, it's not a prime. State this and exit program prematurely, else continue.
if TF == False:
    sys.exit(print(f"{num} is not a prime number. \nAll done!")) 
#else statement caste the whole number string into an intiger for the rest of the fuction.
else:
    num = int(num)

# assigned value to a range for division
divran = reversed(range(1, (num + 1)))

# assigned div value to start the loop with
div = 1

# Prime conditional variable assigned 0
primcon = 0

# Beginning of for loop
for div in divran:
    output = ((num) / (div))
    if output == int(output):
        div += 1
        primcon += 1

# primcon counts everytime the output of the loop is a whole number. Since the only two multiples of a
# prime number are itself and 1, a prime number should whenever primcon is like 2
if primcon == 2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

print("All Done")
