'''
Parse reports from potok.digital.
Sould be parsing potok.digital not click's exports.
'''

import re
import csv
from datetime import datetime

a = open('d:/tmp/potok_6367_21_03_2018.csv', 'rb')
b =csv.reader(a, delimiter=';', quotechar='|')

returned = []
pcts = []
fines = []
interacc = []
invest = []
other = []
errors = []

returned_pattern = re.compile('выплата')
pcts_pattern = re.compile('проценты')
fines_pattern = re.compile('пени')
#interacc_pattern = re.compile('Внутрибанковский')
#other_pattern = re.compile('(\"*Частичный)|(\"*плата процентов)|(\"*плата пени)')
invest_pattern = re.compile('инвестирование')

def float_convert( input ):
    output = float(input.replace(',', '.'))
    return output

dt_start = datetime.strptime('01.03.2018', '%d.%m.%Y')
dt_end = datetime.strptime('22.03.2018', '%d.%m.%Y')
    
for row in b:
    if datetime.strptime(row[2], '%d.%m.%Y')>dt_start and datetime.strptime(row[2], '%d.%m.%Y')< dt_end:
        if returned_pattern.match(row[4]):
            #returned.append(row[1])
            returned.append(float_convert(row[3]))
        elif pcts_pattern.match(row[4]):
            #pcts.append(row[1])
            pcts.append(float_convert(row[3]))
        elif fines_pattern.match(row[4]):
            #fines.append(row[1])
            fines.append(float_convert(row[3]))
        elif invest_pattern.match(row[4]):
            #nominal.append(row[1])
            invest.append(float_convert(row[3]))
        else: #not other_pattern.match(row[1]):
            #other.append(row[1])
            other.append(float_convert(row[3]))
        
print str(sum(returned))
print str(sum(pcts))  
print str(sum(fines))
#print "in: "+ str(sum(interacc))
#print "errors: " + str(len(errors))
#print "others: " + str(len(other))

