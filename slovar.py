'''
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

'''
slovar = {'moscow':{'street':'10','year':'2020'},
          'ryazan':{'street':'20','year':'2022'}
          }
#print(slovar)

for town in slovar:
    print(town)
    for info in slovar[town]:
        print(info)
        #print(slovar['moscow'])

