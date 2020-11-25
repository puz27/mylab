import re
'''
stroka='privet 123'
print(re.search('123',stroka))
'''
# zifri
log1='fdsfsdf 11:10 dsfsdf'
info1=re.search('\d\d:\d\d',log1)
print(info1.group())