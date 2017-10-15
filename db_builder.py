import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="kiddies.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

# function for running command
def run(command) :
    c.execute(command)

# alter list so that primary key is set
def add(fields, pid) :
    for num in range(0, len(fields)) : 
        if fields[num] == pid :
            fields[num] = pid + " primary key"
    return fields

# fill database table with csv rows
def fill(read) :
    for line in read :
        fields = []
        #take each column data in the row
        for field in read.fieldnames :
            fields.append("\"" + line[field] + "\"")
        run("INSERT INTO peeps VALUES (" + ', '.join(fields) + ")")

# main method for converting csv file into database table
def create(src, name, pid) :
    with open(src) as table :
        read = csv.DictReader(table)
        #add primary key to appropriate field, procured by fieldnames attribute
        fields = add(read.fieldnames, pid)
        #run create table command
        run("CREATE TABLE " + name + " (" + ', '.join(fields) + ")")
        fill(read)

create("peeps.csv", "peeps", "id") 
        
'''
peppers = "peeps.csv"
    
# open peeps.csv as ppl
with open(peppers) as tbl:

    #dictify it
    machina = csv.DictReader(tbl)

    #create table with appropriate fieldnames
    run("CREATE TABLE peeps (name, age, id integer primary KEY)")
    
    #for each line in peeps.csv, populate peeps the table
    for line in machina:
        retstr = "\"" + line["name"] + "\", " + line["age"] + ", " + line["id"]
        run("INSERT INTO peeps VALUES ( " + retstr + ")")

   ''' 

#==========================================================
db.commit() #save changes
db.close()  #close database


