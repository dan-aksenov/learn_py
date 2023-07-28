# -*- coding: utf-8 -*-
import pandas as pd

from xml.etree.ElementTree import parse
doc = parse('/tmp/alfa.xml').getroot()

all_items = []

for i in doc.iter('{TaxAppendix}Details'):
  all_items.append(i.attrib)

xmlToDf = pd.DataFrame(all_items)

# xmlToDf.to_excel('/tmp/alfa.xlsx')
excel_file = '/tmp/alfa.xlsx'

with pd.ExcelWriter( excel_file, mode='a') as writer:  
  xmlToDf.to_excel(writer, sheet_name='Sheet_name_3')