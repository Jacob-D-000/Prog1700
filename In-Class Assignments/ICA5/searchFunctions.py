"""
Program: Search Fuctions
Author: Jacob Dimoff
Date: 23/11/22
filename: searchFunctions.py
Purpose: Use search functons
"""

def linearsearch(lst, key):
    for i in range(len(lst)):
        if key == lst[i]:
            return i
    return -1



def binarySearch (lst, key):
    low = 0
    high = len(lst) - 1
    while high >= low:
        mid = (low + high) // 2
        if key == lst[mid]:
            return mid
        elif key < lst[mid]:
            high = mid -1
        else:
            low = mid + 1
    return -1


def main():
    nums = [10,2,4,6,2,76243,6,3,2]
    nums.sort()
    print(nums)
    print(linearsearch(nums,6))
    print(binarySearch(nums,6))

    letters = list("Hello World")
    print(letters)
    letters.sort()
    print(letters)


    print(linearsearch("Hello World", "o"))
    print(binarySearch("Hello World", "o"))
    print("Hello world".index("o"))

main()

# def main():
#     input("Press enter to find the index of o in 'hello world'")
