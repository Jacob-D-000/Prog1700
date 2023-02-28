"""
Program: Random Numebers
Author: Jacob Dimoff
Date:1/11/22
filename: RandomNumber.py
Purpose: Generate Random Number
"""

import random

# generator ramdom #
num1 = random.randint(0, 9) 
num2 = random.randint(0, 9)
# user anwser
anwser = int(input("what is " + str(num1) + " + " + str(num2) + " ?"))
# display result
print(str(num1) + " + " + str(num2) + " = " + str(anwser) + " is " +
      str((num1 + num2 == anwser)))
