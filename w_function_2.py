import ipaddress
#ip='192.168.1.3575775/24'
#ipaddress.ip_interface(ip)



def checkip(ip):
    try:
        ipaddress.ip_interface(ip)
        #return True
        print('ok')
    except ValueError as err:
        #return False
        print('not ok')

checkip('192.162228.1.1/24')