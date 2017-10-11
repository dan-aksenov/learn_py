import os
from time import strftime

'''
Arvhive and compress.
'''

logsdir = "/home/dbax/learn_py"
zip_program = "tar -zcvf"

for files in os.listdir(logsdir):
	if files.endswith(".txt"):
		files1 = files + "." + strftime("%Y-%m-%d") + ".zip"
		os.chdir(logsdir)
		os.system(zip_program + " " + files1 + " " + files)
		#os.remove(files)

