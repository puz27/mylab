import ipaddress

network1 = ipaddress.ip_network('192.168.1.0/30')
print(network1)

for i in network1:
    print(i)

network2=ipaddress.ip_interface('150.31.44.0/24')
print(network2.netmask)



