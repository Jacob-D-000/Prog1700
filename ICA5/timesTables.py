"""
Program: Times Tables
Author: Jacob Dimoff
Date: 8/11/22
filename:timesTables.py
Purpose: Dipslay a number and its suqare
"""

ran = range(1,4)

print("This fuction prints out a 3 * 3 times tables")

for x in ran:
    for y in ran:
        ans = (x * y)
        print(f"{x} * {y} = {ans}") 
