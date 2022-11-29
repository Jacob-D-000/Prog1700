"""
Program:Pennies for Pay
Author: Jacob Dimoff
Date: 28/11/22
filename: Pennies fo Pay
Purpose: Caluate exponeitenal pay with pennies
"""

def Penny_Cal():
    dollst = [0]
    pen = 0.5
    days = int(input("How many days have you worked: "))
    dayran = range(days)
    for days in dayran:
        calpen = pen * 2
        caldol = float(calpen) * 0.01
        dollst.append(caldol)
        pen = calpen
    return dollst

def Print_Table(x):
    lstran = range(len(x))
    for idx in lstran:
        valst = x[idx]
        print(f"{idx: <20}  ${valst}")
    

def Sum_Print(x):
    dollst_sum = sum(x)
    print(f"After {(len(x) - 1)} days of work, you would make ${dollst_sum}")

def main():
    dollst = Penny_Cal()
    Print_Table(dollst)
    Sum_Print(dollst)


main()