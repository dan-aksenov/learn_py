import pandas as pd

from xml.etree.ElementTree import parse
doc = parse('/tmp/alfa.xml').getroot()

store_items = []
all_items = []

for i in doc.findall('money_moves/money_move'):
    settlement_date = i.find("settlement_date").text
    oper_type = i.find("oper_type").text
    comment = i.find("comment").text
    volume = i.find("volume").text
    p_code = i.find("p_code").text
    oper_group = i.find("oper_group").text
    store_items = [ settlement_date, oper_type, comment, volume, p_code, oper_group ]
    all_items.append(store_items)

xmlToDf = pd.DataFrame(all_items, columns=[
  'settlement_date', 'oper_type', 'comment', 'volume', 'p_code', 'oper_group' ] )