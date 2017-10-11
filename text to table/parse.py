#!/usr/bin/env python
from cStringIO import StringIO
import re

'''
Parse file like
[ Object 1]
[ Property 1 ]
[ Property 2 ]
-----

into
[ Object 1]
[ Property 1 ],[ Property 2 ]

right now does a bit wrong:
[ Object 1 ]
['[ Property 1 ]']
['[ Property 1 ]', '[ Property 2 ]']

last array state only.

'''

#
obj_start = re.compile(r'\[ Object [0-9]* \]') # do it with \n
obj_end =  re.compile(r'[ ----- ]' ) # imporove it!
prop = re.compile(r'\[ Property [0-9]* \]') # also with n
test_file = "./testfile.txt"

in_obj = False
curr_obj = None
prop_list=[]

with open(test_file) as f:
for line in f:
    obj_start_match = obj_start.match(line)
    if obj_start_match:
        in_obj = True
        obj_name = ("{}".format(obj_start_match.group(0)))
        prop_list=[]
        print obj_name
    if in_obj:
        prop_match = prop.match(line)
        if prop_match:
           prop_name = ("{}".format(prop_match.group(0)))
           prop_list.append(prop_name)
        if not prop_match:
            pass
        else:
           print prop_list
    elif obj_end_match:
        in_obj = False
