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
    for row in range(rowcon):
        sqrlst.append([])
        for col in range(colcon):
            # valapp = string.punctuation("*")
            sqrlst[row].append[valapp]
    return sqrlst
    


# def pattern_tri(x):


def main():
    star = get_input()
    sqr =  pattern_sqr(star)
    print(sqr)


main()
