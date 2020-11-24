import ipaddress

def myip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

print(myip('192.168.1.1'))