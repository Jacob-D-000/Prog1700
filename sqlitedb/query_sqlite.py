"""
Program:
Author: Jacob Dimoff
Date:
filename: 
Purpose:
"""

import sqlite3 as PROGdemo

# con = PROGdemo.connect('Person_Address_Photo_Data.sqlite')

# with con:
#     data = con.execute('select * from Address')
#     for rec in data:
#         print(rec)

con = PROGdemo.connect('students.sqlite')

with con:
    con.execute("""
    CREATE TABLE STUDENTS (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    firstName TEXT,
    lastName TEXT,
    course TEXT,
    courseGrade INTEGER );
    """)

sql = 'INSERT INTO STUDENTS (id, firstName, lastName, course, courseGrade) values(?, ?, ?, ?, ?)'
data = [
(1, 'Fred', 'Flintstone', 'PROG1700', 78),
(2, 'Barney', 'Rubble', 'PROG1700', 92),
(3, 'Wilma', 'Flintstone', 'COMM1700', 75),
(4, 'Betty', 'Rubble', 'COMM1700', 53),
(5, 'Pebbles', 'Flintstone', 'PROG1700', 81),
(6, 'BamBam', 'Rubble', 'PROG1700', 98)
]

with con:
    con.executemany(sql, data)

