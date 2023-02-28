"""
Program Math Operators
Author: Jacob Dimoff
Date 24/10/22
Filename:Math_Operators.py
Purpose: get two numbers as input and demo the various math operators
"""

num1 = input("Enter 1st Number: ")
num2 = input("Enter 2nd Number(Larger than First): ")

# Addition Demo
sum_result = int(num1) + int(num2)
print("The sum of the two numbers is {}. ".format(sum_result))

# Subtraction Demo
minus_result = float(num2) - float(num1)
print("The result of subtracting the 2nd Number form the 1st is %s." % minus_result)

# Negation Demo
neg_result = - int(num1)
print(f"The result of negating your first number is {neg_result}. ")

neg_result = - int(num2)
print(f"The result of negating your second number is {neg_result}. ")

# Exponentiation demo
ex_result = int(num1) ** int(num2)
print(f"The result of multiplying the first number by the second number exponentially is {ex_result}")

# Multiplication Demo
multi_result = int(num1) * int(num2)
print(f"The result of multiplying the first number by the second number is {multi_result}.")

# Division Demo
div_result = int(num2) / int(num1)
print(f"The result of dividing the second number by the first is {div_result}")

# Quotient Demo
quo_result = int(num2) // int(num1)
print(f"The resulting floor of dividing the first number form the second is {quo_result}")

# Modulus Demo
mod_result = int(num2) % int(num1)
print(f'The resulting modulus (or remainder) from dividing the first number by the seconded number is {mod_result}')