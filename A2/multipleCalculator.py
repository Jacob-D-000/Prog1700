"""
Program: Multiple Calcuator
Author: Jacob Dimoff
Date:10/11/22
filename: multipleCalculator.py
Purpose: To determine the multiples of a user inputed number
"""

# user input for variable num
num = int(input("Pick a number: "))

# create a range using num + 1 as and endpoint, run in reverse so the printed answer will be correct
numran = reversed(range(1, (num + 1)))

# define a division varible each num varible will be divided by.
div = 1


print(f"The multiples of {num} are:")

for div in numran:
    output = ((num) / (div))
    if output == int(output):
        print(int(output))
        div += 1


print("All Done!")
