import time, numpy, timeit, sys
from test import MyHTMLParser
arr = []
start = time.time()
PERIOD_OF_TIME = sys.argv[1]
while True :
    t=timeit.timeit('MyHTMLParser("http://python.org")', setup='from test import MyHTMLParser', number=1)
    arr.append(t)
    if time.time() > start + PERIOD_OF_TIME : break
print(len(arr))
print(numpy.average(arr))
print(numpy.sum(arr))
f = open('links.txt', 'w')
for a in (arr):
   sql = 'insert into results("script_type", "time") values ("script1", ' + a + ');'
   f.write(sql)
f.close()
