'''
with open('conf.txt') as f:
    #print(f.read())
    for line in f:
        line=line.split()
        if line[0] != 'information':
            print(line)
'''
slov={}

'''
with open('conf.txt') as f:
    #print(f.read())
    for line in f:
        line=line.split()
        if line[1][0].isdigit():
            # print(line)
            int,ip,*rest=line
            slov[int]=ip

print(slov)
'''
spisok=[]
with open('conf2.txt') as f:
    #print(f.read())
    for line in f:
        #print(line)
        if 'my' in line:
            int=line.split()[0]
            print(int)

        if 'mtu' in line:
            speed=line.split()[1]
            print(speed)
            slov[int]=speed
            spisok.append([int,speed])
print(slov)
print(spisok)


