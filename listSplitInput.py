"""
Program: Practicing List Split Inputs
Author: Jacob Dimoff
Date: 21/11/22
filename: listSplitInput.py
Purpose: practice with list splitting an comprehension
"""

def shift(list):
    temp = list[0]
    for i in range (1, len(list)):
        list[i-1]=list[i]
    list[len(list)-1] = temp

item1 = "Fred Wilma Dino Barney Betty BamBam".split()
item2 = "11/14/2018".split("/")
print(item1)
print(item2)


# for loop input
items = []
print("Enter 5 numbers: ")
for index in range(5):
    items.append(eval(input()))

print(items)

s = input("Enter 5 numbers\nseparated by spaces: ")
numbers = s.split()
item3 = [eval(x) for x in numbers]

item4 = []
for x in numbers:
    item4.append(eval(x))
print(item3)
print(item4)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist2 = []
for x in fruits:
    if "a" in x:
        newlist2.append(x)
print(newlist2)