with open('MAC_NEW','w') as r:
    r.seek(0)
    r.close()

with open('MAC') as f:
    for line in f:
        if line.startswith(' 1') :
                #line.split()
                vlan,ma,_,int = line.split()
                print(vlan,ma,int)