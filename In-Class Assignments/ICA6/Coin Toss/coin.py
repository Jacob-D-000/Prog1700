"""
Program: Coin Class
Author: Jacob Dimoff
Date: 1/12/22
filename: coin.py
Purpose: Create a Coin Class
"""

import random

class coin:
    def __init__(self) -> None:
        print(self.toss())
        self.__side = self.toss
    
    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"
    
    def get_sideup(self):
        return self.__sideup