"""
Program: Sets
Author: Jacob Dimoff
Date: 28/11/22
filename: sets.py
Purpose: Practice using sets
"""

# Set union Method
# Initialized A and B
A = {1,2,3,4,5}
B = {4,5,6,7,8}
# use | Operator
print(A | B)
print(A.union(B))
lst_A = list(A)
lst_B = list(B)
lst_B.extend(lst_A)
print(f"List A is {lst_A}")
print(f"List B is {lst_B}")
str_H = "HELLLLLO world"
set_H = set(str_H)
print(set_H)

# Intersection of Set
# Initialized A and B
A = {1,2,3,4,5}
B = {4,5,6,7,8}
# use & Operator
print(A | B)
#use intersection function of A and B
print(A.intersection(B))

# Create Sets
baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
# Display members of the baseball set.
print('The following students are on the baseball team:')
for name in baseball:
    print(name)
# Display members of the basketball set.
print('The following students are on the basketball team:')
for name in basketball:
    print(name)

# Demonstrate intersection
print('The following students play both baseball and basketball:')
for name in baseball.intersection(basketball):
    print(name)
# Demonstrate union
print('The following students play either baseball or basketball:')
for name in baseball.union(basketball):
    print(name)

# Demonstrate difference of baseball and basketball
print('The following students play baseball, but not basketball:')
for name in baseball.difference(basketball):
    print(name)
print(f"|baseball n basketBall'|: {len(baseball.difference(basketball))}")
# Demonstrate difference of basketball and baseball
print('The following students play basketball, but not baseball:')
for name in basketball.difference(baseball):
    print(name)
# Demonstrate symmetric difference
print('The following students play one sport, but not both:')
for name in baseball.symmetric_difference(basketball):
    print(name)

