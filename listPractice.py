"""
Program: List Method Practice
Author: Jacob Dimoff
Date: 21/11/22
filename: listPractice.py
Purpose: To practice methods that affect lists
"""

import random

myList = [30, 1, 2, 1 ,0]
print(f"1. {myList}")

myList.append(40)
print(f"2. {myList}")

myList.insert(1, 43)
print(f"3. {myList}")

myList.extend([1, 43])
print(f"4. {myList}")

myList[2]
print(f"5. {myList[2]}")

myList.index(2)
print(f"6. {myList.index(2)}")

myList.count(43)
print(myList.count(43))

len(myList)
print(len(myList))

max(myList)
print(max(myList))

min(myList)
print(min(myList))

sum(myList)
print(sum(myList))

myList.remove(1)
print(myList)

myList.pop(1)
print(myList)

myList.pop()
print(myList)

myList.sort()
print(myList)

myList.reverse()
print(myList)

random.shuffle (myList)
print(myList)

# calling the value of my list
myList2 = myList
print(id(myList))
print(id(myList2))

# This copys values from myList to myList3
myList3 = [x for x in myList]
print(id(myList3))
# Can also be written as "myList3 = [] + myList"

