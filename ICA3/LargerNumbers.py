"""
Program Larger Number
Author: Jacob Dimoff
Date 3/11/22
Filename:LargerNumbers.py
Purpose: get two numbers as input and demo the various math operators
"""


num1 = int(input("Choose one Number: "))
num2 = int(input("Choose a different Number: "))

if num1 > num2:
    print(f'{num1} is larger then {num2}.')
else:
    print(f'{num2} is larger then {num1}.')