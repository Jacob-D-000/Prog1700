"""
Program: Letter Counter
Author: Jacob Dimoff
Date: 24/11/22
filename: letterCounter.py
Purpose: To Count the Letters found in a String
"""

def getinput():
    convar =0
    charinput = (input(("Type a string: ")))
    charinput = charinput.replace(" ", "")
    while convar == 0:
        if not charinput.isalpha():
            charinput = (input(("This fuction does not accept numbers please type a string: ")))
        else:
            convar += 1
    charinput = charinput.upper()
    return charinput

def listinput(x):
    charlst = list(x)
    print(charlst)
    unilist = [0] * 26
    for i in range(0, len(charlst)):
        idx = charlst[i]
        numchar = (ord(idx) - 65)
        if 0 <= numchar <= 65:
            unilist[numchar] += 1
    return unilist

def disinput(x):
    for i in range(0, len(x)):
        if x[i] > 0:
            char = i + 65
            oldchar = chr(char)
            print(f"{oldchar} was found in the string {x[i]} times")
    

def main():
    charinput = getinput()
    unilist = listinput(charinput)
    disinput(unilist)
    print("All Done")
    

main()
