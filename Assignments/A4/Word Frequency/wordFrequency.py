"""
Program: Word Frequency
Author: Jacob Dimoff
Date: 5/12/22
filename: wordFrequency.py
Purpose: Count Frequency 
"""

import os

# define file to be anaylized
file = "fileForFreq.txt"

# define read file
def read_file(x):
    # open file
    rwd = open(x, "r")
    # read file
    word = (rwd.read())
    # prepare file to be formated into a list
    word = word.lower()
    word = word.replace(".", "")
    wrdlst = word.split (" ")
    # close file
    rwd.close
    return wrdlst
    
# define list to dictionary fuction
def lst_to_dic(x):
    # define dictonary
    lstdic ={}
    # define range of list
    lenran = range(len(x))
    # for loop that runs through list
    for i in lenran:
        # define lstitem as item at inbdex
        lstitem = x[i]
        # if item is in list, increase key by one else add item to list
        if lstitem in lstdic:
            lstdic[lstitem] += 1
        else:
            lstdic[lstitem] = 1
    return lstdic    
        
def main():
    # Start of main make sure function runs in the proper file
    file_path = os.path.dirname(__file__)
    os.chdir(file_path)
    # define wrdlst with read_file
    wrdlst =  read_file(file)
    # define diclst with lst_to_dic
    diclst = lst_to_dic(wrdlst)
    print(diclst)


main()