"""
Program: List Fuctions
Author: Jacob Dimoff
Date: 15/11/22
filename: listFuctions.py
Purpose: list of fuctions you can use on a list
"""
list1 = [1, 2, 3, 6, 7]
print(list1)
list2 = [4, 5, 6]
list2.insert(3, 100)
print(list2)

list3 = list1 + list2
print(list3)

list3 = 2 * list1
print(list3) 

for i in list1:
    if i in list2:
        print(f"{i} is in both lists!")
    else:
        print(f"{i} is not in both lists")


if list1 == list2:
    print("equal")
else:
    print("not")
 
rg = range(0, len(list3), 2)

for i in rg:
    print(list3[i])

print(list3.pop(4))


items = "Fred Wilma Dino Barney Betty BamBam".split()
print(items)

item2 = "11/14/2018".split("/")
print(item2)

# item3 =[]
# print("enter 5 numbers: ")
# for index in range(5):
#     item3.append(eval(input()))

# print(item3)

s = input("Enter 5 Numbers \
    separated by spaces:")
numbers =s.split()
item4 = [eval(x) for x in numbers]
print(item4)

item5 = []
for x in numbers:
    item5.append(eval(x))
print(item5)

def shift(lst):
    temp = lst[0]
    for i in range (1, len(lst)):
        lst[i - 1]=lst[i]
    lst[len(lst) - 1 ] = temp

shift(items)
print(items)

# i = 0
# while i < len(myList):
#     print(myList[i])
#     i += 1

