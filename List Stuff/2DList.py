"""
Program: 2-D Lits Generator
Author: Jacob Dimoff
Date: 24/11/22
filename: 2DList.py
Purpose: Initialize a 2D list
"""
def create_list():
    matrix =[]
    numOfRows = eval(input("Enter the Number rows: "))
    numOfCols = eval(input("Enter the Number columns: "))
    for row in range(numOfRows):
        matrix.append([])
        for column in range(numOfCols):
            value = eval(input("Enter an Element and Press Enter: "))
            matrix[row].append(value)
    return matrix

def print_matrix(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            print(matrix[row][column], end="\n")
        print()
    print()
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()

def main():
    var = create_list()
    print(var)
    print_matrix(var)

main()

