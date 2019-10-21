#!/bin/python
import sys,  getopt

opts, args = getopt.getopt(sys.argv[1:], 'a:b:')

for opt, arg in opts:
    if opt in ('-a'):
        a = arg
    elif opt in ('-b'):
        b = arg

print "a is: " + a + ", b is: " + b
