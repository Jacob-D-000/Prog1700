"""
Program: Circle Mai
Author: Jacob Dimoff
Date: 1/30/22
filename: cirmain.py
Purpose: Main function for circle module.
"""
from circle import Circle

def main():
    c1 = Circle()
    print(f"The area of the circle of radius {c1.getRadius()} is {c1.getArea()}")
    c2 = Circle(2)
    print(f"The area of the circle of radius {c2.getRadius()} is {c2.getArea()}")
    c3 = Circle(3)
    print(f"The area of the circle of radius {c3.getRadius()} is {c3.getArea()}")


main()