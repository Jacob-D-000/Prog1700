"""
Program: List Passing
Author: Jacob Dimoff
Date: 21/11/22
filename: listPassing.py
Purpose: 
"""

def add(x, list=[]):
    if x not in list:
        list.append(x)
        print(f"List inside {id(list)}")
    return list

def main():
    list1 = add(1) 
    print(list1)
    list2 = add(2) 
    print(list2)
    list3 = add(3, [5, 6, 7, 8])
    print(list3)
    list4 = add(4)
    print(list4)

main()