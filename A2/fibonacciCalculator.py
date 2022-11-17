""""
Program: Fibonacci Calculator
Author: Jacob Dimoff
Date:11/11/22
filename: fibonacciCalculator.py
Purpose: To calculate the Fibonacci sequence in a range of 1 to 100
"""

import time

input("This program will print the Fibonacci Numbers from 1 to 100. Press enter to run the Program: ")

# variable one is
x = 0

# variable two is
y = 1

# Defining the varible that will be printed

z = x + y
while x < 100 and y < 100:
    if z < 100:
        print(z)
        z = x + y
        x = y
        y = z
        time.sleep(1)


print("All done")
