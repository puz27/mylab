with open("file.txt",'r') as x:
    print(x.read())


file=open('file.txt','r')
#print(file.read())
s=file.readline()
print(s)