"""
Program: Student IO file
Author: Jacob Dimoff
Date: 1/12/22
filename: student.py
Purpose: Create example of an I/O File
"""

import os


def write_student(student_file):

    # print(os.getcwd())

    outfile = open(student_file, "w")
    # outfile = open("C:/Users/user/School Stuff/Prog/Prog1700/FileIO/students_absoulte.txt", "w")
    outfile.write("Jane Doe\n")
    outfile.write("Jane Smith\n")
    outfile.write("Jane rolfe\n")
    outfile.close

def append_student(student_file):

    # print(os.getcwd())

    outfile = open(student_file, "a")
    outfile.write("John Doe\n")
    outfile.write("John Smith\n")
    outfile.write("John rolfe\n")
    outfile.close

def read_stdent(student_file):
    infile = open(student_file, "r" )
    txt=(infile.read())
    print(txt)
    infile.close()

def realline_student(student_file):
    infile = open(student_file, "r")
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    infile.close()
    print(line1)
    print(line2)
    print(line3)

def read_eof():
    infile = open(student_file, "r")
    line = infile.readline()
    while line !=" ":
        print(line)
        line = infile.readline()
    infile.close()

def read_file(student_file):
    with open(student_file, "r") as infile:
        for line in infile:
            print(line)

def main():
    # file_name = "students.txt"
    print(os.getcwd())
    file_path = os.path.dirname(__file__)
    print(file_path)
    os.chdir(file_path)
    print(os.getcwd())
    txt_file = r"students_relative.txt"
    file = os.path.abspath(txt_file)
    if os.path.exists(file):
        # append_student(file)
        # read_stdent(file)
        realline_student(txt_file)
    else:
        write_student(file)

    # os.chdir(file_path)
    # print(os.getcwd())
    # read_stdent()

main()