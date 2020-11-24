import subprocess

ips=['8.8.8.8','192.168.1.1']


def checkip(ips):
    for ip in ips:
       rez=subprocess.run('ping {} -c 2 -n'.format(ip), shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding='utf-8')
       print('Pinging...',ip)
       print(rez.returncode)


checkip(ips)