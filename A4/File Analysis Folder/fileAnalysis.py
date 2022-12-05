"""
Program:File Analysis
Author: Jacob Dimoff
Date: 5/12/22
filename: fileAnalysis.py
Purpose: To use IO files to analysis text files 
"""

import os

# defines the files that will be analyzed
file1 = "text_file_1.txt"
file2 = "text_file_2.txt"

#define reading function
def read_file(x):
    # open file
    rwd = open(x, "r")
    # read file
    word = (rwd.read())
    # convert file contents into an list easier
    word = word.lower()
    wrdlst = word.split (" ")
    # close file
    rwd.close
    return wrdlst

# define function to convert list
def set_convert(x):
    setlst = set(x)
    return setlst

# define union function
def union(x, y):
    union = x.union(y)
    print(union)

# define intersection function
def intersect(x, y):
    intersection = x.intersection(y)
    print(intersection)

# define difference function
def diff(x, y):
    differnece = x.difference(y)
    print(differnece)
    return differnece

# define union of the difference
def diff_union(x, y):
    unionDiff = x.union(y)
    print(unionDiff)

# define main function
def main(): 
    # Start of main make sure function runs in the proper file
    file_path = os.path.dirname(__file__)
    os.chdir(file_path)
    # Two files are read and converted into a set
    wrdlst1= read_file(file1)
    setlst1 = set_convert(wrdlst1)
    wrdlst2 = read_file(file2)
    setlst2 = set_convert(wrdlst2)
    # Run union function
    union(setlst1, setlst2)
    # Run intersection function
    intersect(setlst1, setlst2)
    # Runs and defines the difference function
    difference1 = diff(setlst1, setlst2)
    difference2 = diff(setlst2, setlst1)
    # Run difference union function
    diff_union(difference1, difference2)
 


main()
