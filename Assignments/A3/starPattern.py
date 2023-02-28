"""
Program: Star Pattern
Author: Jacob Dimoff
Date: 28/11/22
filename: starPattern.py
Purpose: To draw a pattern of stars based on user input
"""
import string

def get_input():
    con = 0
    star = input("Choose a number between 1 and 10: ")
    while con == 0:
        if not star.isnumeric():
            star = input("Won't compute! Input a number from 1 and 10: ")
        elif int(star) < 1 or int(star) > 10:
            star = input("Won't compute! Input a number from 1 and 10: ")
        else:
            con += 1
    return int(star)

def pattern_sqr(x):
    sqrlst = []
    rowcon = (x)
    colcon = (x)
    valcol = str("*")
    for row in range(rowcon):
        sqrlst.append([])
        for col in range(colcon):
            sqrlst[row].append(valcol)
    return sqrlst

def pattern_tri(x):
    trilst = []
    rowcon = (x)
    valcol = str("*")
    conranvar = 0 
    for row in range(rowcon):
        trilst.append([])
        conranvar += 1
        for col in range(conranvar):
            (trilst[row].append(valcol))
    return trilst
    

def print_function(x):
    for row in x:
        for prtValue in row:
            print(prtValue, end = " ")
        print()

def main():
    star = get_input()
    sqr =  pattern_sqr(star)
    print("This is a Square pattern!")
    print_function(sqr)
    tri = pattern_tri(star)
    print("This is a Triangle pattern!")
    print_function(tri)
    print("All Done")

main()