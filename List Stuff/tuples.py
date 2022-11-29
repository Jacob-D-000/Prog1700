"""
Program: Tuples
Author: Jacob Dimoff
Date: 29/11/22
filename: tuples.py
Purpose: Practice using tuples
"""

import sys

my_list = ["apple", "banana", "cherry"]
my_tuple = ("apple", "banana", "cherry")
my_tuple2 = ("apple", "banana", "cherry", my_list)

print(type(my_list))
print(type(my_tuple))
print(type(my_list[0]))
print(my_list[0]==my_tuple[0])
print()
print(my_tuple)
my_list[0] = "Grape"
print(my_list)
# my_tuple[0] = "grape" # cant' do this for a tunple
print(my_tuple)
print(my_tuple.index("cherry"))

print(sys.getsizeof(my_list))
print(sys.getsizeof(my_tuple))
print(my_tuple2[3][0])
my_tuple2[3][0] = "listgrape"
print(my_tuple2[3][0])
print(my_tuple2)