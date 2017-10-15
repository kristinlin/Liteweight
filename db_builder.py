# Kristin Lin
# Softdev pd07
# Work 09: Work 09: SQLite, same great SQL taste, half the calories
# 2017-10-15

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandits.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

# function for running command
def run(command) :
    c.execute(command)

# fill database table with csv rows
def fill(name, read) :
    for line in read :
        #take each column data in the row
        fields = []
        for field in read.fieldnames :
            fields.append("\'" + line[field] + "\'")
        #run command with values
        run("INSERT INTO " + name +  " VALUES (" + ', '.join(fields) + ")")
        
# main method for converting csv file into database table
def create(src, name) :
    with open(src) as table :
        read = csv.DictReader(table)
        fill(name, read)

# peeps convert
run("CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER PRIMARY KEY)")
create("peeps.csv", "peeps")

# courses convert
run("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)")
create("courses.csv", "courses")


#==========================================================
db.commit() #save changes
db.close()  #close database


