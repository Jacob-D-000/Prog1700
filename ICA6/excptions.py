"""
Program: Python exceptions 
Author: Jacob Dimoff
Date: 6/12/22
filename:exceptions.py
Purpose: learn exceptions 
"""


def divide():
    try:
        num1 = int(input("Type #"))
        num2 = int(input("Type #"))
        result = num1 / num2
        print(result)
    except ZeroDivisionError as err:
        print(err)
    except ValueError as err:
        print(err)
    print("keep going")

def gross_pay():
    try:
        hours = int(input("Num of hours "))
        pay_rate = float(input('Enter pay-rate: '))
        gross_pay = hours * pay_rate
        gross_pay = format(gross_pay, ',.2f')
        print(f"Gross pay $ {gross_pay} : ")
    except ValueError:
        print("Error")
        print("be valid Int")

def read_file():
    filename = input("enter a filename")
    try:
        with open(filename, "r") as infile:
            contents = infile.read()
            print(contents)
    except IOError:
        print('An error occured')
        print('the file, filename')

def main():
    # divide()
    # gross_pay()
    read_file()

main()