""""
Program: Prime Range Calculator
Author: Jacob Dimoff
Date:12/11/22
filename: primeRange.py
Purpose: To Caluclate all prime numbers in a range of 1 to 100
"""

# defining starting number and number it's divided by
num = 1

div = 1

# define a range of 1-100 so the num in the for loop will go up to 100
numran = range(1, 101)

# define the control variable. 1 is added to the variable every time output is equal to an int
primcon = 0

# user input to start program
input("This program will calculate all numbers from 1 to 100. Press enter to run the program.")

# The forloop
for num in numran:
    primcon = 0
    divran = (range(1, num + 1))
    for div in divran:
        output = ((num) / (div))
        if output == int(output):
            primcon +=1

# this condition states that if the prime control variable is exactly 2, then the number is printed.
# since prime numbers can only be divided by 1 and it's self, this loop checks all possible numbers
# a number can be divided by. If it only finds two, it prints the num which is prime.
    if primcon == 2:
        print(num)

print("All Done")
