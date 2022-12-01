"""
Program: Student IO file
Author: Jacob Dimoff
Date: 1/12/22
filename: student.py
Purpose: Create example of an I/O File
"""

def main():
    outfile = open("students.txt", "w")
    outfile.write("John Doe\n")
    outfile.write("John Smith\n")
    outfile.write("John rolfe\n")
    outfile.close

main()