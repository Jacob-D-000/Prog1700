"""
Program Average Class Grade
Author: Jacob Dimoff
Date:7/11/22
filename: sentinalAvgGrade.py
Purpose: To Create a Guessing Game
"""

total_grade = 0
count = 0
inpgrd = 0

inpgrd = int(input("Please enter a grade or input -1 to finish inputing grades: "))

while inpgrd != -1:
    total_grade += inpgrd 
    count += 1
    inpgrd = int(input("Please enter another grade or input -1 to finish inputing grades: "))

avegrd = total_grade / count

print(f'the classes average grade is {avegrd}. ')