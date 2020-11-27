import csv
from collections import OrderedDict
'''
with open('info.csv') as f:
    retur=csv.reader(f)
    for line in retur:
        print(line)
        


with open('info.csv') as f:
    retur=csv.reader(f)
    head=next(retur)
    for line in retur:
        print(line)
        
    


with open('info.csv') as f:
    retur=csv.DictReader(f)
    for line in retur:
        print(line)
        print(line['hostname'],line['location'])


data = [['hostname','vendor','model','location'],
         ['sw1','cisco','1232','moscow'],
         ['sw2','cisco','7789','ryazan'],
         ['sw3','cisco','3750','london']]
print(data)

with open('new_info.csv','w') as f:
    wri=csv.writer(f)
    for line in data:
        wri.writerow(line)
'''


slovar = [{'moscow':'2020',
         'ryazan':'2022'}]


#print(slovar)

with open('info4.csv','w') as s:
    writer=csv.DictWriter(s,fieldnames=list(slovar[0].keys()),quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(slovar)












