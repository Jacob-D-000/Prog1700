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

# print fuctions to add flow to output
print(f"The multiples of {num} are:")

# start of the for loop the condtional. The loop will finish when the div number has gone through
# the whole range. This will simulate dividing the equation by every number 
for div in numran:
    # Output could equal a factor
    output = ((num) / (div))
    # This condtional will test if the output is an integer or not
    if output == int(output):
        # if the if state statement is true then output is printed as a integer
        print(int(output))


print("All Done!")
