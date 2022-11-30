"""
Program: Modularized Grader Program
Author: Jacob Dimoff
Date: 29/11/22
filename: modularGrader.py
Purpose: Practice modularization of fuctions by writing a program to calculate grades
"""

# def displayInstructions():

# def validateGrade(x):
#     if x == A or a:
        
#     elif x == B or b:

#     elif x == C or c:

#     elif x == D or d:
#     elif x == F or f:          

def instructions():
    print("This Fuction can calculate an average grade out of 100%. This average could be for an an entire class or for a single indivdual.\nThis program will not accpet letter grades or equations. \n\nIf you want to finsih entering grades, type and enter exit. \nIf you need to see the rules of this fuction again, type -?.")

def classorperson():
    convar = 0
    cvp = input("First lets determine Whether or not you are calculating the average grade of an entire class or single person. \n\nIf the average is for entire class, enter 1. \n\nIf the average is for one person, enter 2.\n\nPlease Enter Here: ")
    while convar == 0:
        if cvp != "1" and cvp != "2": 
            cvp = input("Can't compute! Please enter 1 to calculate the class average, or 2 to calculate the indivdual average. \n\nPlease Enter Here: ")
        else:
            convar += 1 
        # :
        #     cvp = input("Can't compute! Please enter 1 to calculate the class average, or 2 to calculate the indivdual average. \n\nPlease Enter Here: ") 
        # elif cvp == "2":
    return cvp

def getGrades():
    grdlst = []
    grd = 0
    # oplst = ["+","-" ,"*" ,"/", "."]
    while grd != -1:
        grd = (input("Please input a grade: "))
        bf = grd.() 
        bi = bool(int(grd))
        if grd == "-?":
            print( "This program will not accpet letter grades or equations. If you want to finsih entering grades, type and enter exit. If you \nneed to see the rules of this fuction again, type -?.")
            # grd = input("Please input a grade: ")
        # elif grd != float(grd) or grd != int(grd):
        elif False == bf and  False == bi:
            print("Won't compute. Please input a grade. If you need help remebering the fuction's restrictions please enter -?.")
        # for grd in grd.split():
            # if grd in ["+","-" ,"*" ,"/", "."] or grd.isnumeric():
            #     neogrd = eval(grd)
            #     grdlst.append(neogrd)
            # elif grd.isalpha():
            #     grd
        elif True == bf or True == bi:
            grd = float(grd)
            grdlst.append(grd)
    return grdlst

def calculateAvg(x):
    grdsum = sum(x)
    grdavg = grdsum / len(x)
    return grdavg
    
def resultype(x):
    if x == 1:
        print("The average for the enter class is: ")
    else:
         print("The average for this indvidual is: ")

def displayResults(x):
    print(x)

def main():
    instructions()
    print("\n\n")
    cvp = classorperson()
    grdlst = getGrades()
    grdavg = calculateAvg(grdlst)
    resultype(cvp)
    displayResults(grdavg)

main()