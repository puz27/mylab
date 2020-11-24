import subprocess

see=subprocess.run("who")

see

#mping=subprocess.run('ping 8.8.8.8 -c 5 -n', shell=True)
#mping


myoing2=subprocess.run('ping 8.8.8.8 -c 5 -n', shell=True, stdout=subprocess.PIPE)
print(myoing2.stdout)
print(myoing2.stdout.decode('utf-8'))