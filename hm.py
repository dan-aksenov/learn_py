import re

#def group_by_heading( some_source ):
with open('HMall.txt', "r") as source:
	hm_list = {"Test": 0, "Method": 0}
	for line in source:
		if re.match("(.*)(Test #)(.*)", line):
			hm_list["Test"] = re.findall("[0-9]+",line) 
		if re.match("(.*)(=)(.*)", line):
			if re.match("(Method)(.*)",line):
				hm_list["Method"] = line
		print hm_list
