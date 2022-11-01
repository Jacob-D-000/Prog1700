"""
Program Larger Number
Author: Jacob Dimoff
Date 1/11/22
Filename:LargerNmber.py
Purpose: get two numbers as input and demo the various math operators
"""

grade = int(input("What Grade did you get?: "))

if grade >= 90:
    print("Your letter mark is an A!")
elif grade < 90 and grade >= 80:
    print("Your letter mark is an B")
elif grade < 80 and grade >= 70:
    print("Your letter mark is an C")
elif grade < 70 and grade >= 60:
    print("Your letter mark is an D")
else:
    print("Your letter mark is an F")