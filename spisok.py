list = [1,2,3]
print(list)


spisok=['port',
        'vlan',
        'ip']
print(spisok)


print(spisok[2])

spisok.append(100)
print(spisok)


#neskolko dannyih
list5=[1,2,3]
list5.extend([200,366,'my'])
print(list5)

#delete dannyih
list5=[2,5,3,44,3,111]
list5.remove(2)
list5.sort()
print(list5)

print('Zamena interface')
my_list='interface gigabit0/0'
my_list=my_list.replace("gigabit","ethernet")
print(my_list)

my_list='ASDF:1DFF:DFVC'
my_list=my_list.replace(':','.')
print(my_list)

#konvert to dvoicnaya
print('10 -> 2')
ip2="{:b}.{:b}.{:b}.{:b}"
ip10="{:d}.{:d}.{:d}.{:d}"
ip2=ip2.format(192,168,100,1)
ip10=ip10.format(192,168,100,1)
print(ip10)
print(ip2)