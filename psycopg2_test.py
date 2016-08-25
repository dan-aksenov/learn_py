#!/usr/bin/python
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

try:
    conn = psycopg2.connect("dbname='postgres' user='postgres'")
except:
    print "I am unable to connect to the database"

cur = conn.cursor()

cur.execute("""select datname from pg_database""")

rows = cur.fetchall()

print "\nShow me the databases:\n"
for row in rows:
    print "   ", row[0]

