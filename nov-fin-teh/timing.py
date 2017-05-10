import time, numpy, timeit, sys
from test import MyHTMLParser

a_times = []
start = time.time()
p_time = float(sys.argv[1])

while True :
    v_time=timeit.timeit('MyHTMLParser("http://python.org")', setup='from test import MyHTMLParser', number=1)
    a_times.append(p_time)
    if time.time() > start + p_time : break

print(len(a_times))
print(numpy.average(a_times))
print(numpy.sum(a_times))

f = open('results_timing.sql', 'w')
for t in (a_times):
   sql = 'insert into results("script_type", "time") values ("script1", ' + str(t) + ');'
   f.write(sql + "\n")
f.close()
