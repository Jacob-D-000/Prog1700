"""
Program: Sum Fuction
Author: Jacob Dimoff
Date: 14/11/22
filename: sumFuction.py
Purpose: Create reusable fuctions that sum
"""

def sum (i1, i2):
    result = 0
    for i in range(i1, i2):
        result += i
    return result

def main():
    print(result)
    print(f"Sum from 1 to 10 is {sum(1, 11)}")
    print(f"Sum from 11 to 20 is {sum(10, 21)}")
    print(f"Sum from 21 to 30 is {sum(20, 31)}")

result ="hello"
main()

# res = sum(1, 11)    

# print(res)

# sum = 0
# for i in range (1, 11):
#     sum += i
#     print(f"Sum from 1 to  10 is {sum}")

