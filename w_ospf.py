slovar={}
data=[]
with open('OSPF') as f:
    #print(f.read())
    for line in f:
        #print(line)
        line=line.split()
        if line[0] == 'O':
            #rint(line[0])
            x=line[0].replace('O','OSPF')
            #print(line)
        protocol,inter,metric,_,hop,update,out = line
        slovar['PROTOCOL']=x
        slovar['IP']=line[1]
        slovar['NEXT HOP']=line[2]
        #print(slovar)
        for i in slovar:
            print(i,":",slovar[i])
