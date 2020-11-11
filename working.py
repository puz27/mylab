stroka="data{}"
stroka=stroka.format(1)
print(stroka)

stroka2="{:5} {:6}"
a='12345'
b='1234567888888888'

stroka2=stroka2.format(a,b)
print(stroka2)



shablon='''
    interface = {}
    vlan = {}
    '''

rezult=shablon.format('g0/1',2)
print(rezult)


