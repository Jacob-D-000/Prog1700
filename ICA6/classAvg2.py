"""
Program: Class Average 2
Author: Jacob Dimoff
Date: 15/11/22
filename: classAvg2.py
Purpose: Use a list to calculate a class average
"""

# count = 5
grades =[80,90,100]
# grades.append(object) = int(input("Enter a grade [0-100]"))
# grade2 = int(input("Enter a grade [0-100]"))
# grade3 = int(input("Enter a grade [0-100]"))
# grade4 = int(input("Enter a grade [0-100]"))
# grade5 = int(input("Enter a grade [0-100]"))
# total = grade1 + grade2 + grade3 + grade4 + grade5
total = grades[0] + grades[1] + grades[2]
count = len(grades)
avg = total/count
print(f"The class average is {avg}")