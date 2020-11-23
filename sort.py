from operator import itemgetter
spisok=['1','1000','2','11','77','99']
print(sorted(spisok,key=len))
print(sorted(spisok,key=int))


data =[[5,'int0/1'],[2,'int0/2'],[4,'int0/7']]
print((sorted(data,key=itemgetter(1))))


list1=['1','2','3']
list2=['int1','int2','int3']
print(list(zip(list1,list2)))
dict(zip(list1,list2))