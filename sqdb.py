 #sql data types
 # NULL, INTEGER, REAL, TEXT, BLOB
 #---Query Test---#
    #con = sqlite3.connect('sublist.db')
    #print("Connected to database: sublist.db (Connect #2)")
    
    # Output as array from database using lambda <---
    #con.row_factory = lambda cursor, row: row[0]
    #cur = con.cursor()
    #ids = cur.execute('Select * from subscriptions').fetchall()
    #print(ids[0])

import sqlite3

__version__ = '0.1a'

#-test arguments for database-#
de_month = 5
de_day = 31
de_year = 2000
subname = "Test"
price = 12
timeperiod = 'Monthly'   
#-----------------------------#

def yeet(de_month, de_day, de_year, subname, price, timeperiod):
    
    con = sqlite3.connect('sublist.db')
    print("Connected to database: sublist.db")
    cur = con.cursor()
    

    cur.execute("""Create Table subscriptions (
        Month   integer,
        Day     integer,
        Year    integer,
        SubName text,
        Price   real,
        PayPeriod   text
        )""")
    
    cur.execute("Insert Into subscriptions (Month, Day, Year, SubName, Price, PayPeriod) values (?,?,?,?,?,?)",
               (de_month, de_day, de_year, subname, price, timeperiod))

    con.commit()
    print("Committed data to database: sublist.db")
    con.close()

def updatetest(de_month, de_day, de_year):
    con = sqlite3.connect('test.db')
    print("Connected to database: test.db")
    cur = con.cursor()

    #cur.execute('''create table subscription (
     #   Month   integer,
      #  Day     integer,
       # Year    integer
        #)''')
    
    cur.execute("insert into subscription (Month, Day, Year) values (?,?,?)", (de_month, de_day, de_year))

    con.commit()
    print("Changes committed to test.db")
    con.close()

def listdb():
    

if __name__ == '__main__':
    updatetest(de_month, de_day, de_year)
