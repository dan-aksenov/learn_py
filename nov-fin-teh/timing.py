import time, numpy, timeit
from test import MyHTMLParser
arr = []
start = time.time()
PERIOD_OF_TIME = 1000
while True :
    t=timeit.timeit('MyHTMLParser("http://python.org")', setup='from test import MyHTMLParser', number=1)
    arr.append(t)
    if time.time() > start + PERIOD_OF_TIME : break
print(len(arr))
print(numpy.average(arr))
print(numpy.sum(arr))
