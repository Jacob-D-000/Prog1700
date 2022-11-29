"""
Program:
Author: Jacob Dimoff
Date:
filename: 
Purpose:
"""

import math

class Circle:
    #Construct a Cirlce Object
    def __init__(self, radius: int = 1)-> None:
        self.radius = radius

    def getArea(self)->float:
        return self.radius * self.radius * math.pi
    
    def getperimeter(self):
        return 2 * self.radius * math.pi

    def setRadius(self,radius):
        self.radius = radius

# from circle import Circle only nessacary for fuction in own file.

def main():
    c1 = Circle()
    print(f"The area of the circle of radius {c1.radius} is {c1.getArea()}")
    c2 = Circle(2)
    print(f"The area of the circle of radius {c2.radius} is {c2.getArea()}")
    c3 = Circle(3)
    print(f"The area of the circle of radius {c3.radius} is {c3.getArea()}")

main()