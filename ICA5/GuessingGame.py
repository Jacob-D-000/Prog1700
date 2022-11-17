"""
Program: Guessing Game program
Author: Jacob Dimoff
Date:1/11/22
filename: GuessingGame.py
Purpose: To Create a Guessing Game
"""

import random
num1 = random.randint(0,9)

guess = int(input("Can you guess what number I'm think of: "))

if guess == num1:
    print("You are Right!!!") 
else:
    print("Sorry Wrong Answer!!!")
    if guess > num1:
        print("Too high!")
    # elif guess < num1:
    else:
        print("Too low!")
    
    # print(f"Sorry Wrong Answer!!! The Answer was {num1}!")