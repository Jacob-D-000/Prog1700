"""
Program Even Or odd
Author: Jacob Dimoff
Date 3/11/22
Filename:EvenOrOdd.py
Purpose: Determine whether a # is odd or even
"""
num = int(input("Choose a Number: "))

ans = num % 2

if ans == True:
    print(f'{num} is odd')
else:
    print(f'{num} is even')


    