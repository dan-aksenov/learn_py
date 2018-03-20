'''
Parse movementList.csv with data from potok.digital
'''

import re
import csv

a = open('d:/tmp/movementList.csv', 'rb')
b =csv.reader(a, delimiter=';', quotechar='|')

returned = []
pcts = []
fines = []
interacc = []
nominal = []
other = []

returned_pattern = re.compile('\"*Частичный')
pcts_pattern = re.compile('\"*(О|У)плата процентов')
fines_pattern = re.compile('\"*(О|У)плата пени')
interacc_pattern = re.compile('Внутрибанковский')
other_pattern = re.compile('(\"*Частичный)|(\"*плата процентов)|(\"*плата пени)')
nominal_pattern = re.compile('^Пополнение номинального')

for row in b:
    if returned_pattern.match(row[1]):
        returned.append(row[1])
    elif pcts_pattern.match(row[1]):
	    pcts.append(row[1])
	elif fines_pattern.match(row[1]):
	    fines.append(row[1])
	elif interacc_pattern.match(row[1]):
	    interacc.append(row[1])
    elif nominal_pattern.match(row[1]):
	    nominal.append(row[1])
	elif not other_pattern.match(row[1]):
	   other.append(row[1])
		
print len(returned)
print len(pcts)
print len(fines)
print len(interacc)
print len(other)

