import time, numpy, timeit, sys
from test import MyHTMLParser

# number of repeats
p_repeats = int(sys.argv[1])

a_time=timeit.repeat('MyHTMLParser("http://python.org")', setup='from test import MyHTMLParser', repeat=p_repeats, number=1)

print(numpy.average(a_time))
print(numpy.sum(a_time))
print(len(a_time))

# write to sqlfile
f = open('results_repeat.sql', 'w')
for a in (a_time):
   sql = 'insert into results("script_type", "time") values ("script2", ' + str(a) + ');'
   f.write(sql + "\n")
f.close()
