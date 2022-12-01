"""
Program: Circle module
Author: Jacob Dimoff
Date: 1/12/22
filename: cricle.py
Purpose: Create a module to calculate a ciricle
"""

import math

class Circle:
    #Construct a Cirlce Object
    def __init__(self, radius: int = 1)-> None:
        self.__radius = radius

    def getArea(self)->float:
        return self.__radius* self.__radius * math.pi
    
    def getperimeter(self):
        return 2 * self.__radius * math.pi

    def setRadius(self,radius):
        self.__radius = radius
    
    def getRadius(self):
        return self.__radius

# from circle import Circle only nessacary for fuction in own file.
