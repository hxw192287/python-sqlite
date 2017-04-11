import os
import sqlite3
os.chdir(os.getcwd() + '/namesbystate')

import csv
conn = sqlite3.connect('../' + 'babynamedb.db')
c = conn.cursor()
for filename in os.listdir(os.getcwd()):
    with open(filename, 'rU') as csvfile:
        fieldnames = ['state', 'sex', 'year_of_birth', 'name', 'number']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            # Inserting the records into the database
            c.execute("INSERT INTO baby_name (state,gender,year,name,number) VALUES (?,?,?,?,?);", (row['state'], row['sex'], row['year_of_birth'], row['name'], row['number']))
        conn.commit()
conn.close()
# Alternative without csv module

# Create a class that maps fieldnames to integer values (Enum in python 3+)
'''
class Baby_Name():
     STATE = 0
     SEX = 1
     YEAR_OF_BIRTH = 2
     NAME = 3
     NUMBER = 4

# Get all of the file names from the namesbystate
# For each file in the directory of the current working directory
for filename in os.listdir(os.getcwd()):
    # Open the file descriptor associated with the filename
    file = open(filename, "r")
    # for each line in the newly opened file descriptor
    for line in file:
        # Create an array of all token delimited string
        currentline = line.split(",")
        c.execute("INSERT INTO baby_name (state,gender,year,name,number) VALUES (?,?,?,?,?);", (currentline[Baby_Name.STATE], currentline[Baby_Name.SEX], currentline[Baby_Name.YEAR_OF_BIRTH], currentline[Baby_Name.NAME], currentline[Baby_Name.NUMBER]))
    conn.commit()
conn.close()
'''
