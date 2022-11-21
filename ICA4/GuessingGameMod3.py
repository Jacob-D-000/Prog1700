"""
Program: Guessing Game program
Author: Jacob Dimoff
Date:3/11/22
filename: GuessingGameMod3.py
Purpose: To Create a Guessing Game
"""

LCV = "Y"

import random

while LCV == 'Y':
    num1 = random.randint(0,9)

    guess = int(input("Can you guess what number I'm think of: "))

    while guess != num1:
        print("Sorry Wrong Answer!!!")
        if guess > num1:
            print("Too high!")
        else:
            print("Too low!")
        guess = int(input("Try again: "))
    
    print("You are Right!!!") 

    LCV = input("If you want to play again, press Y, if you would like to quit, press Q: ").upper()



    # print(f"Sorry Wrong Answer!!! The Answer was {num1}!")