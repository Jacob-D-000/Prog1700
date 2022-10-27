"""
Program: Lake Travel
Author: Jacob Dimoff
Date:27/10/22
filename: Lake_Distane.py
Purpose: To calcuate the distance someone travels across the great lakes
"""
#This is a list of ways a user can input yes or no
lst_yes = ["yes" , "y", "Yes", "1"]
lst_no = ["no", "n", "NO", "No", "N", "0"]

name = input("Hello, What is you name: ")

# input for lake huron
Huron = input("Did you Go Across Lake Huron?: ")

if Huron in lst_yes:
    lake_1 = int(332)
elif Huron in lst_no:
    lake_1 = int(0)


# input for lake Erie
Erie = input("Did you Go Across Lake Erie?: ")

if Erie in lst_yes:
    lake_2 = int(388)
elif Erie in lst_no:
    lake_2 = int(0)

# input for lake Ontario
Ontario = input("Did you Go Across Lake Ontario?: ")

if Ontario in lst_yes:
    lake_3 = int(311)
elif Ontario in lst_no:
    lake_3 = int(0)

funk = lake_1 + lake_2 + lake_3

print(f"{name}, you travelled {funk}km!")

