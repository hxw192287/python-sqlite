import sqlite3

sqlite_file = 'baby_name_database.sqlite'    # name of the sqlite database file

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('''CREATE TABLE baby_name
             (state TEXT NOT NULL,
               gender TEXT NOT NULL,
                year INTEGER NOT NULL,
                 name TEXT NOT NULL,
                  number INTEGER NOT NULL,
                  uid INTEGER PRIMARY KEY)''')

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()

'''
#Useful SQLite Commands

# Truncate table equivalent
DELETE FROM tablename;
'''
