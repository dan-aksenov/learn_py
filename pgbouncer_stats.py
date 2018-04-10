#from https://github.com/python-diamond/Diamond/blob/master/src/collectors/pgbouncer/pgbouncer.py

import psycopg2
import psycopg2.extras

conn = psycopg2.connect(database='pgbouncer', user=user, password=password, host=host, port=port)

conn.set_isolation_level(0)
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cursor.execute('''SHOW POOLS''')
query_results = cursor.fetchall()