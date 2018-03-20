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
errors = []

returned_pattern = re.compile('\"*Частичный')
pcts_pattern = re.compile('\"*(О|У)плата процентов')
fines_pattern = re.compile('\"*(О|У)плата пени')
interacc_pattern = re.compile('Внутрибанковский')
#other_pattern = re.compile('(\"*Частичный)|(\"*плата процентов)|(\"*плата пени)')
nominal_pattern = re.compile('^Пополнение номинального')
errors_pattern = re.compile('Возврат ошибочно переведенных средств по займам')

def float_convert( input ):
    output = float(input.replace(',', '.'))
	return output

for row in b:
    if returned_pattern.match(row[1]):
        #returned.append(row[1])
		returned.append(float_convert(row[2]))
    elif pcts_pattern.match(row[1]):
	    #pcts.append(row[1])
		pcts.append(float_convert(row[2]))
	elif fines_pattern.match(row[1]):
	    #fines.append(row[1])
		fines.append(float_convert(row[2]))
	elif interacc_pattern.match(row[1]):
	    #interacc.append(row[1])
		interacc.append(float_convert(row[2]))
    elif nominal_pattern.match(row[1]):
	    #nominal.append(row[1])
		nominal.append(float_convert(row[2]))
	elif errors_pattern.match(row[1]):
	    #errors.append(row[1])
		errors.append(float_convert(row[2]))
	else: #not other_pattern.match(row[1]):
	    #other.append(row[1])
		other.append(float_convert(row[2]))
		
print "returned: " + str(sum(returned))
print "interest: " + str(sum(pcts))  
print "fines " + str(sum(fines))
#print "in: "+ str(sum(interacc))
#print "errors: " + str(len(errors))
#print "others: " + str(len(other))

