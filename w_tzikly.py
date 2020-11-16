ip=[]
s_ip='192.168.1.1'
octet=s_ip.split('.')
'''
for i in [0,1,2,3]:
   #print('ADD:', i)
   mass='{:08b}'.format(int(octet[i]))
   ip.append(mass)
   print(ip)
'''
for x in octet:
   print(x)
   ip.append('{:08b}'.format(int(x)))
   print(ip)

interfaces=range(5)
for z in interfaces:
   print(z)
   print("interface GI/{z}")
   print("interface GI/{}".format(int(z)))