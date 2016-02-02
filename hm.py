import re

def group_by_heading( some_source ):
	buffer = []
	for line in some_source:
		if re.match("(.*)(Test #)(.*)", line):
			if buffer: yield buffer
			buffer =  [ re.findall("[0-9]+",line) ] 
		else:
			buffer.append( line )
	yield buffer

with open('HMall.txt', "r") as source:
	for heading_and_lines in group_by_heading( source ):
		heading = heading_and_lines[0]
		lines = heading_and_lines[1:]
		print heading
	#	print lines 
