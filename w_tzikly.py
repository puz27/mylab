ip=[]
s_ip='192.168.1.1'
octet=s_ip.split('.')

print(octet)
'''
'''
for i in [0,1,2,3]:
   #print('ADD:', i)
   mass='{:08b}'.format(int(octet[i]))
   ip.append(mass)
   print(ip)


