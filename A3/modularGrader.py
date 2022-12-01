"""
Program: Modularized Grader Program
Author: Jacob Dimoff
Date: 29/11/22
filename: modularGrader.py
Purpose: Practice modularization of functions by writing a program to calculate grades
"""

import string

def displayInstructions():
    print("This Function can calculate an average grade out of 100%. This average could be for an an entire class or for a single individual.\nThis program will not accept letter grades or equations. \nIf you want to finish entering grades, type and enter exit. \nIf you need to see the rules of this function again, type -?.")

def classOrPerson():
    convar = 0
    cvp = input("First lets determine Whether or not you are calculating the average grade of an entire class or single person. \n\nIf the average is for entire class, enter 1. \n\nIf the average is for one person, enter 2.\n\nPlease Enter Here: ")
    while convar == 0:
        if cvp != "1" and cvp != "2": 
            cvp = input("Can't compute! Please enter 1 to calculate the class average, or 2 to calculate the individual average. \n\nPlease Enter Here: ")
        else:
            convar += 1 
    return cvp

def validateGrade(x):
    if x == "-?":
        print("This program will not accept letter grades or equations. If you want to finish entering grades, type and enter exit. If you \nneed to see the rules of this function again, type -?.")
        var = False
    elif x == "exit":
        print("Thanks for the input")
        var = False
    elif x.isalpha():
        print("Won't compute. Please input a grade. If you need help remembering the function's restrictions please enter -?.")
    elif x.isalpha() and x.isnumeric():
        print("Won't compute. Please input a grade. If you need help remembering the function's restrictions  please enter -?.")
        var = False
    elif (x.isalpha() and x.isnumeric()) or string.punctuation in x:
        print("Won't compute. Please input a grade. If you need help remembering the function's restrictions  please enter -?.")
        var = False
    elif "." in x and x.isnumeric():
        var = True
    else:
       print("Won't compute. Please input a grade. If you need help remembering the function's restrictions please enter -?.")
       var = False 
    return var

def ranCheck(x):
    if 0 < x < 100:
        var = True
    else:
        var = False
        print("Number is not in range of 0 - 100. Please input a number in the proper range")
    return var

def getGrades():
    grdlst = []
    grd = None
    while grd != "exit":
        grd = input("Input a Grade: ")
        ggbool = (validateGrade(grd))
        if ggbool:
            grd = float(grd)
            neobool = ranCheck(grd)
            if neobool:
                grdlst.append(grd)
    return grdlst

def calculateAvg(x):
    grdsum = sum(x)
    grdavg = grdsum / len(x)
    return grdavg
    
def resulType(x):
    if x == 1:
        print("The average for the enter class is: ")
    else:
         print("The average for this individual is: ")

def displayResults(x):
    print(x)

def convarLoop():
    yorn = input("Thanks for using. \n\nIf you would like to find another average, type yes. \n\nIf you would like to exit the program, type no \n\nEnter command here: ")
    if yorn == "yes":
        convar = 1
    elif yorn == "no":
        convar = 0
    else: 
       yorn = input("Won't compute! \n\nIf you would like to find another average, type yes. \n\nIf you would like to exit the program, type no \n\nEnter command here: ")
    return convar

def main():
    convar = 1
    displayInstructions()
    while convar == 1:
        print("\n\n")
        cvp = classOrPerson()
        grdlst = getGrades()
        grdavg = calculateAvg(grdlst)
        resulType(cvp)
        displayResults(grdavg)
        convar = convarLoop()
    print("Thanks for using the Program!")
    
main()