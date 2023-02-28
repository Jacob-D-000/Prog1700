"""
Program: A5 Progam True
Author: Jacob Dimoff
Date: 9/12/22
filename: A5_Program_True.py
Purpose: Query a in memory database
"""

#  Import nesscary Functions
import sqlite3 as PROGdemo
import os
os.chdir(os.path.dirname(__file__))

#  define the function to create a table
def crt_table(x):
    #  open table
    with x:
        # SQL to create the table
        x.execute("""
            CREATE TABLE persons (
            id INTEGER NOT NULL,
            firstName TEXT,
            lastName TEXT,
            postalCode TEXT,
            address TEXT,
            phone TEXT)
            """) 
        # define insert sql function
        sql = 'INSERT INTO persons (id, firstName, lastName, postalCode, address, phone) values(?, ?, ?, ?, ?, ?)'
        #  dinfe sql data inputed
        data = [
            (1, 'Tommy', 'Flintstone', 'B4V 1B1', '2675 Brook St', 9028380921),
            (2, 'Rogelio', 'Marion', 'L2N 1S8', '3148 Ontario St', 5454546521),
            (3, 'Robert', 'Marion', 'N0N 0N0', '2914 Gorham Street', 1155745951),
            (4, 'Isacc', 'Miele', 'P3A 1Z6', '1265 Paris St', 1448485321),
            (5, 'James', 'Henderson', 'T2C 2P3', '4276 40th Street', 4118684866),
        ]
        # execute each sql function defined previously
        x.executemany(sql, data)

#  define dump table function
def dump_table(x):
    # open table
    with x:
        data = x.execute('select * from persons')
        for rec in data:
            print(rec)

def last_name_sel(x):
    # define sentinal
    sentvar = 1
    #  define qu for concatination
    qu = "'"
    # open table
    with x:
        # define while loop
        while sentvar != 0:
            # define try catch
            try:
                #  input last name
                imp = input("Input a last name you want to find: ")
                #  if user input doesn't have "'", then it add it to the string
                if "'" not in imp:
                    imp = qu + imp + qu    
                # execute sql and places it in a variable
                data = x.execute(f'select * from persons Where lastName = {imp}')
                # loop prints each item in the data set
                for rec in data:
                    print(rec)
                    sentvar = 0
            # If an error is found, retry the function 
            except PROGdemo.Error:
                print("Value Error Try again")

# define user inputed data
def user_imp(x):
    # define sentinal
    sentvar = 1
    # print user instructions
    print("This input allows for you to input your own values input. You can input ID, First Name, Last Name, Address, Postal Code\nand Phone Number.\nEach Field must be comma seperated and the Phone number must only be digits")
    # while loop that runs the function
    while sentvar != 0:
        with x:
            #  define try cathc
            try: 
                # ask for each user input
                IDnum = int(input("Input ID: "))
                First = input("Input First Name: ")
                Last = input("Input Last Name: ")
                Postal = input("Input Postal Code: ")
                Address = input("Input Address: ")
                Phone = input("Input Phone number: ")
                # define sql
                exvar = ("INSERT INTO persons (id, firstName, lastName, postalCode, address, phone) values(?, ?, ?, ?, ?, ?)")
                # make inputed variables into a tuple
                date_tuple = (IDnum, First, Last, Postal, Address, Phone)
                # execute and commit the row
                x.execute(exvar, date_tuple)
                x.commit()
                sentvar = 0
            except PROGdemo.Error:
                print("Value Error Try again")

#  Define main
def main():
    #  Connect the database in memory
    con = PROGdemo.connect(':memory:')
    #  Control Varible called
    convar = 1
    #  Create Control
    crt_table(con)
    # print instructions
    print("This function allows you to connect to the persons table in the sqlite database in memory.\nIf you would like to see the conntents of the table, enter 1.\nIf you would like to search for data by last name, press 2.\nIf you would like to add a new entry into the table, press 3:\nIf you would like to exit the program, enter 0.")
    #  define fuctions while loop / menu
    while convar != 0:
        #  Input will determine what fuction is called
        convar = int(input("Make your selection: "))
        if convar == 1:
            dump_table(con)
        elif convar == 2:
            last_name_sel(con)
        elif convar == 3:
            user_imp(con)
        elif convar == 0:
            print("OK!")
        else:
            print("Value Error Try again")
    print("Thanks for using!")

main()