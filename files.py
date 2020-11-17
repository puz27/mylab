#with open("file.txt",'r') as x:
   # print(x.read())


#file=open('file.txt','r')
#print(file.read())
#s=file.readline()
#print(file)
#file.close()
'''
file2=open('file.txt','a+')
file2.write('linefdgdg235465656546546\n')
file2.close()
with open("file.txt",'r') as x:
  print(x.read())

with open('file3.txt','r') as t:
  for x in t:
    if x.startswith('service'):
      print(x)
'''
with open ('file3.txt','r') as r, open("file4.txt","w") as w:
  for k in r:
    if k.startswith('service'):
      w.write(k)