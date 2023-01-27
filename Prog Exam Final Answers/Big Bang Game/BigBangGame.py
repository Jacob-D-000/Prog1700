"""
Program: Rock Paper Scissor Lizard Spock
Author: Jacob Dimoff
Date: 14/12/22
filename: BigBangGame.py
Purpose: To make a fun game for David
"""

import random

def displayInstructions():
    print("This is a game called: Rock Paper Scissor Lizard Spock!\nThe rules are simple\nRock crushes Lizard and Scissors.\nPaper covers rock and disproves Spock. \nScissors decapitate Lizard and cuts paper. \nLizard poisons Spock and eats Paper. \nSpock smashes scissors and vaporizes rock.\nRock[1]\nPaper[2]\nScissors[3]\nLizard[4]\nSpock[5]")

def getUserChoice():
    connvar = 1
    while connvar == 1:
        player = int(input("Choose your weapon: "))
        # player = player.capitalize()
        # if player == "Rock":
        #     playerchc = 1
        #     connvar = 0
        # elif player =="Paper":
        #     playerchc = 2
        #     connvar = 0
        # elif player =="Scissors":
        #     playerchc = 3
        #     connvar = 0
        # elif player =="Lizard":
        #     playerchc = 4
        #     connvar = 0
        # elif player =="Spock":
        #     playerchc = 5
        #     connvar = 0
        if 1 > player and player < 6:
            print("I didn't catch that. What did you say.")
        else:
            connvar = 0
    return player
          
def genetateComputerChoice():
    comp = random.randint(1, 5)
    if comp == 1: 
        print("The computer choose Rock")
    elif comp == 2: 
        print("The computer choose Paper")
    elif comp ==3: 
        print("The computer choose Scissors")
    elif comp == 4: 
        print("The computer choose Lizard")
    elif comp ==5: 
         print("The computer choose Spock")
    return comp

def determineWinner(x, y):
    if x == 1:
        if y == 1:
            winvar = 0  
        elif y == 2:
            winvar = 2
        elif y == 3:
            winvar = 1
        elif y == 4:
            winvar = 1
        elif y == 5:
            winvar = 2

    elif x == 2:
        if y == 1:
            winvar = 1
        elif y == 2:
            winvar = 0  
        elif y == 3:
            winvar = 2
        elif y == 4:
            winvar = 2
        elif y == 5:
            winvar = 1

    elif x == 3:
        if y == 1:
            winvar = 2            
        elif y == 2:
            winvar = 1
        elif y== 3:
            winvar = 0
        elif y== 4:
            winvar = 1
        elif y== 5:
             winvar = 2   

    elif x == 4:
        if y == 1:
            winvar = 2
        elif y == 2:
            winvar = 1
        elif y== 3:
            winvar = 2
        elif y== 4:
            winvar = 0
        elif y== 5:
            winvar = 1

    elif x == 5:
        if y == 1:
            winvar = 1
        elif y == 2:
            winvar = 2
        elif y== 3:
            winvar = 1
        elif y== 4:
            winvar = 2
        elif y== 5:
            winvar = 0    

    return winvar

def printWinner(x):
    if x == 0:
        print("It's a tie!")
    elif x == 1:
        print("You won!")
    elif x == 2:
        print("You lost!")

def trackScores(x, y, z):
    playscor = 0 + y
    compscor = 0 + z
    if x == 1:
        playscor += 1
    elif x == 2:
        compscor += 1
    return playscor, compscor

def determineChampion(x, y):
    if x == 3:
        chapvars = 1
    elif y == 3:
        chapvars = 2
    return chapvars

def outputResults(x):
    if x == 1:
        print("You won the match!")
    elif x == 2:
        print("You lost the match!")

def controlVarible():
    convar = 1
    while convar == 1:
        x = input("Would you like to play again?\nInput Here: ")
        x = x.capitalize
        if x == "Yes":
            returned = 0
            convar = 0
        elif x == "No":
            returned = 1
            convar = 0
        else:
            print("I didn't catch that.")
    return returned

def main():
    displayInstructions()
    functionvar = 0
    while functionvar == 0:
        playscore = 0
        compscore = 0
        while playscore < 3 and compscore < 3:
            player = getUserChoice()
            comp = genetateComputerChoice()
            winvar= determineWinner(player, comp)
            printWinner(winvar)
            scortup = trackScores(winvar, playscore, compscore)
            playscore = scortup[0]
            compscore = scortup[1]
        chapvars = determineChampion(playscore, compscore)
        outputResults(chapvars)
        functionvar = controlVarible()

main()
