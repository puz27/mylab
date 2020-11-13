ip = input('insert IP')
a=ip.split('.')
print(ip)
#proverka
"""
#print(list(ip[11]))
print('CHECK FOR LENGHT')
if (list(ip[3])) != '.':
    print('NOT CORRECT LENGHT')
elif  (list(ip[7])) != '.':
    print('NOT CORRECT LENGHT')
elif  (list(ip[11])) != '.':
    print('NOT CORRECT LENGHT')


"""
'''
b=int(a[0])
if b > 255:
    print('NOT CORRECT IP ADDRESS')
   '''

id_add = {'1octet': int(a[0]),
          '2octet': int(a[1]),
          '3octet': int(a[2]),
          '4octet': int(a[3]),
          }
print('CHECK IP')
if id_add['1octet'] > 255 or id_add['1octet'] < 0:
    print('ERROR IN 1 OCTET')
elif  id_add['2octet'] > 255 or id_add['2octet'] < 0:
    print('ERROR IN 2 OCTET')
elif id_add['3octet'] > 255 or id_add['2octet'] < 0:
    print('ERROR IN 3 OCTET')
elif id_add['4octet'] > 255 or id_add['4octet'] < 0:
    print('ERROR IN 4 OCTET')

print('TYPE OF IP:')
if ip == '255.255.255.255':
    print('BROADCAST')
elif ip == '0.0.0.0':
    print("UNSIGNED")
elif a[0] >='1' and a[0] <= '223':
    print('UNICAST')
elif a[0] >= '224' and a[0] <= '239':
    print('MULTICAST')
else:
   print('UNUSED')