from sys import argv
script, from_file, to_file = argv

out_file = open(to_file,'w')
out_file.write(open(from_file).read())

#out_file.close()
#is close needed?
