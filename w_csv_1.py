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
        
        '''


with open('info.csv') as f:
    retur=csv.DictReader(f)
    for line in retur:
        print(line)
        print(line['hostname'],line['location'])




