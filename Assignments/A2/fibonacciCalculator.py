""""
Program: Fibonacci Calculator
Author: Jacob Dimoff
Date:11/11/22
filename: fibonacciCalculator.py
Purpose: To calculate the Fibonacci sequence in a range of 1 to 100
"""

import time

# input that lets user start the function when they press enter
#input("This program will print the Fibonacci Numbers from 1 to 100. Press enter to run the Program: ")

# variable one is
x = 0
# Including a print for x as it is the first number in the sequence
print(x)
# variable two is
y = 1
# Including a print for y as it is the second number in the sequence
print(y)
# Defining the varible that will be printed
z = x + y


# begining of the while loop. This statement sets the loop to not go over 100
while z < 100:
    # this prints the first Z as well as well as well as the changed z in preiovus cycles of the loop
    print(z)
    # equation changes variable 
    z = x + y
    # changing the varible of x to be the same value as y for the next cycle
    x = y
    # changing the varible of y to be the same value as z for the next cycle
    y = z
    # time fuction for added flair
    time.sleep(1)


print("All done")
