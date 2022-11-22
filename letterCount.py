"""
Program:
Author: Jacob Dimoff
Date: 21/11/22
filename: letterCount.py
Purpose:
"""

def getinput():
    charinput = input("Type something: ")
    return charinput

def getlist(x):
    str = x
    charlst = []
    for x in str:
        charlst.append(x)
    return charlst

def countloop(z):
    luran = range(0, len(z)) 
    for x in luran:
        idx = z[x]
        couidx = z.count(idx)
        if couidx == 1:
            print(f"{z[x]} was only found once in this string")
        else:
            print(f"{z[x]} was found {z.count(idx)} times in this string")

def main(): 
    charinput = getinput()
    charlst = getlist(charinput)
    countloop(charlst)

    
main()

