import subprocess
import ipaddress
ips=['8.8.8.8','192.168.1.1','150.31.44.3']
ips2=['192.168.1.1-10']
ip_yes=[]
ip_no=[]
'''
def checkip(ips):
    for ip in ips:
       rez=subprocess.run('ping {} -c 2 -n'.format(ip), shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding='utf-8')
       print('Pinging...',ip)
       #print(rez.returncode)
       if rez.returncode == 0:
           print(ip ,'yes')
           ip_yes.append(ip)
       else:
           print(ip, 'no')
           ip_no.append(ip)
    print('I see',ip_yes)
    print('I not see',ip_no)


checkip(ips)
'''
for ip in ips2:
    if '-' in ip:
       # print('mnogestvo')
        start_ip,end_ip=ip.split('-')
        #print(start_ip)
        #print(start_ip.split('.')[:-1])
        end = ".".join(start_ip.split('.')[:-1]+[end_ip])
        #print(end)
        s=ipaddress.ip_address(start_ip)
        e=ipaddress.ip_address(end)
        print(range(int(s),int(e)))
        for ip in range(int(s),int(e)):
           #print(ip)
           print('pinging...',ipaddress.ip_address(ip))
           subprocess.run('ping {} -c 2 -n'.format(ip), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          encoding='utf-8')