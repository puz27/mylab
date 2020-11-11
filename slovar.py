slov = { 'host':'cisco',
         'ip':'150.31.44.1'}

print(slov['ip'])
print(slov['host'])

slov2=slov.get('ip')
print(slov2)





print('update dictionary')
slov1_new ={ 'ip': '1.1.1.1',
            'version':'new version'}
slov.update(slov1_new)
print(slov)