import subprocess

ips=['8.8.8.8','192.168.1.1','150.31.44.3']
ip_yes=[]
ip_no=[]

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