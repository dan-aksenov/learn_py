#!/usr/bin/python
#
# Inserting into PostgreSQL Database.
#

from Tkinter import *
import Tkinter
import psycopg2

try:
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost'")
except:
    print "I am unable to connect to the database"

cur = conn.cursor()
cur.execute("""select c1 from test1 limit 10""")
rows = cur.fetchall()
top = Tkinter.Tk()

e = Entry(top)
e.pack()

def insertdb():
   cur.execute("""insert into test1(c1) values (%s)""", e.get() )
   conn.commit()
b = Tkinter.Button(top, text='commit', command = insertdb)

def deletedb():
   cur.execute("""delete from test1""")
   conn.commit()
a = Tkinter.Button(top, text='delete', command = deletedb)
b.pack()
a.pack()
w = Listbox(top)
w.pack(side = RIGHT)
for row in rows:
    w.insert(END, row)
top.mainloop()

