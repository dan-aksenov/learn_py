import time, numpy, timeit, sys
from test import MyHTMLParser
arr = []
start = time.time()
run_time = float(sys.argv[1])
while True :
    t=timeit.timeit('MyHTMLParser("http://python.org")', setup='from test import MyHTMLParser', number=1)
    arr.append(t)
    if time.time() > start + run_time : break
print(len(arr))
print(numpy.average(arr))
print(numpy.sum(arr))
f = open('results.sql', 'w')
for a in (arr):
   sql = 'insert into results("script_type", "time") values ("script1", ' + str(a) + ');'
   f.write(sql + "\n")
f.close()
