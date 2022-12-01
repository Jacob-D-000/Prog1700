"""
Program: Main coin toss file
Author: Jacob Dimoff
Date: 1/12/22
filename: coinMain.py
Purpose: pratice class importation
"""

from coin import coin

def main():
    my_coin = coin()
    print(f"This side is up: {my_coin.get_sideup()} ")
    print("I am tossing the coin...")
    my_coin.toss()
    print(f"This side is up: {my_coin.get_sideup()}")

main()