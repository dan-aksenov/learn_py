#!/usr/bin/python
#
# Small script to show PostgreSQL and Pyscopg together
#

from Tkinter import *
import Tkinter
import psycopg2

try:
    conn = psycopg2.connect("dbname='postgres' user='postgres'")
except:
    print "I am unable to connect to the database"

cur = conn.cursor()

cur.execute("""select datname from pg_database""")

rows = cur.fetchall()

top = Tkinter.Tk()
w = Listbox(top)
w.pack()
for row in rows:
    w.insert(END, row)
top.mainloop()

