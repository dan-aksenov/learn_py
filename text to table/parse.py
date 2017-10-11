#!/usr/bin/env python
from cStringIO import StringIO
import re

obj_start = re.compile(r'\[ Object [0-9]* \]') # do it with \n
obj_end =  re.compile(r'\[ -* \]' ) # imporove it!
prop = re.compile(r'\[ Property [0-9]* \]') # also with n
test_file = "./testfile.txt"

in_obj = False
curr_obj = None

with open(test_file) as f:
   for line in f:
       obj_start_match = obj_start.match(line)
       if obj_start_match:
          obj_name = ("{}".format(obj_start_match.group(0)))
          print obj_name
          prop_match = prop.match(line)
       if prop_match:
          prop_name = ("{}".format(prop_match.group(0)))
          print prop_name
       if obj_end_match:
          in_obj = False
