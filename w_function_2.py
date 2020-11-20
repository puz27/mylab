import ipaddress
#ip='192.168.1.3575775/24'
#ipaddress.ip_interface(ip)



def checkip(ip):
    try:
        ipaddress.ip_interface(ip)
        return True
    except ValueError as err:
        return False

checkip('193434 2.168.1.1/24')