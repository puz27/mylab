ip = input('insert IP')
a=ip.split('.')
#print(a[0])


if ip == '255.255.255.255':
    print('BROADCAST')
elif ip == '0.0.0.0':
    print("UNSIGNED")
elif a[0] >='1' and a[0] <= '223':
    print('UNICAST')
elif a[0] >= '224' and a[0] <= '239':
    print('MULTICAST')
else:
    print(ip)
