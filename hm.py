import re
import string

test={"nmb":0,"ttl":'null',"mtd":'null',"mst":'null'}
#print "number			method			master"
with open('HMall.txt', "r") as source:
	for line in source:
		if re.match("(.*)(Test #)(.*)", line):
			tnum = re.findall("[0-9]+",line)
			test["nmb"] = str(tnum)[2:].split("'",1)[0]
			#print tnum
		if re.match('Title       =.*', line):
			tttl = re.findall('=.*', line)
			test["ttl"]=(str(tttl)[3:]).split("'",1)[0]
			#print (str(tttl)[3:]).split("'",1)[0]
		#if re.match("(.*)(=)(.*)", line):
		if re.match("Method      =.*",line):
			tmeth = re.findall("=.*",line)
			test["mtd"]=str(tmeth)[3:].split("'",1)[0]
			#print tmeth
		if re.match("MasterTest-Alive =.*",line):
			tmast = re.findall("=.*",line)
			test["mst"]=str(tmast)[3:].split("'",1)[0]
			#print tmast
			print test.get("nmb")+ test.get("ttl") + test.get("mtd") + test.get("mst")
			