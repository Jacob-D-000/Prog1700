"""
Program:
Author: Jacob Dimoff
Date: 6/12/22
filename: 
Purpose:
"""

import sqlite3 as PROGdemo
import os
os.chdir(os.path.dirname(__file__))

con = PROGdemo.connect('sqlitedb.sqlite')




# con = PROGdemo.connect('Person_Address_Photo_Data.sqlite')

# with con:
#     con.execute("""
#     CREATE TABLE STUDENTS (
#     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#     firstName TEXT,
#     lastName TEXT,
#     course TEXT,
#     courseGrade INTEGER );
#     """)

# sql = 'INSERT INTO STUDENTS (id, firstName, lastName, course, courseGrade) values(?, ?, ?, ?, ?)'
# data = [
# (1, 'Fred', 'Flintstone', 'PROG1700', 78),
# (2, 'Barney', 'Rubble', 'PROG1700', 92),
# (3, 'Wilma', 'Flintstone', 'COMM1700', 75),
# (4, 'Betty', 'Rubble', 'COMM1700', 53),
# (5, 'Pebbles', 'Flintstone', 'PROG1700', 81),
# (6, 'BamBam', 'Rubble', 'PROG1700', 98)
# ]

# with con:
#     con.executemany(sql, data)

# def dir_chi():
#     # file_path = os.path.dirname(__file__)
#     os.chdir(file_path)
#     os.getcwd(file_path)
#     # os.chdir("..")
#     print(os.getcwd())


def dump_table(x):
    with x:
        data = x.execute('select * from PersonTwo')
        for rec in data:
            print(rec)

def main():
    con = PROGdemo.connect('Person_Address_Photo_Data.sqlite')
    # dir_chi()
    dump_table(con)

main()
    
    