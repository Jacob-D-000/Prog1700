"""
Program: Rocket Shuttle Launch
Author: Jacob Dimoff
Date:27/10/22
filename: RocketShuttle.py
Purpose: Count Down for Rocket Launch
"""

import time

print ("Space Shuttle Coun Down!")
num = 10
while num != -1:
    print(num)
    time.sleep(1)
    num -= 1
print("Blast Off")