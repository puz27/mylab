import subprocess

#see=subprocess.run("who")
#see
#mping=subprocess.run('ping 8.8.8.8 -c 5 -n', shell=True)
#mping


#myping2=subprocess.run('ping 8.8.8.8 -c 5 -n', shell=True, stdout=subprocess.PIPE,encoding='utf-8')
#print(myping2.stdout)
#print(myoing2.stdout.decode('utf-8'))


def checkip(ip):
   rez=subprocess.run('ping {} -c5 -n'.format(ip), shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding='utf-8')
   if rez.returncode == 0:
      print('yes')
      return True
   else:
      return False
      print('no')


checkip('8.8.8.8')
