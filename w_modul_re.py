import re
'''
stroka='privet 123'
print(re.search('123',stroka))
'''
# zifri
log1='fdsfsdf 11:10 df qwer.qwer.qwr'
info1=re.search('\d\d:\d\d',log1)
print(info1.group())

info2=re.search('\w\w\w\w.\w\w\w\w.\w{3}',log1)
print(info2.group())

log3='Ethernet 121212 sfsdf'
info3=re.search('^Ethernet',log3)
print(info3.group())

log4=' information Ethernet0'
info4=re.search('Ethernet0$',log4)
print(info4.group())

log5='Ethernet0/1 10.10.10.1'
info5=re.search('\S+ \S+',log5)
print(info5.group())

print('vivod with kartezg')
log6='Ethernet0/5 10.10.10.1'
info6=re.search('(\S+) (\S+)',log5)
print(info6.groups())
print(info6.group(2))

print('vivod with dicionary')
log7='Ethernet0/5 10.10.10.1'
info7=re.search('(?P<inter>\S+) (?P<io>\S+)',log5)
print(info7.groupdict())



