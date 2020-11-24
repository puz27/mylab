import subprocess

see=subprocess.run("who")

see

mping=subprocess.run('ping 8.8.8.8 -c 5 -n', shell=True)
mping
