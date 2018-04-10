#from https://github.com/python-diamond/Diamond/blob/master/src/collectors/pgbouncer/pgbouncer.py

import psycopg2
import psycopg2.extras

conn = psycopg2.connect('dbname= ''pgbouncer'' user=''postgres'' password=''A8eQQaUH4xqKxP'' host=''10.139.127.9'' port=''6432''')

conn.set_isolation_level(0)
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cursor.execute('''SHOW POOLS''')
query_results = cursor.fetchall()