"""
ProgramL Number Square
Author: Jacob Dimoff
Date: 8/11/22
filename: numSq.py
Purpose: Dipslay a number and its suqare
"""

print('This is a list of numbers and its square from 1 to 10')

n = range(1,11)

print(
    "number    square \n"
    "----------------"
)

for x in n:
    sq = (x * x)
    print(f"{x}          {sq}")

