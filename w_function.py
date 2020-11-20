import os
'''
def ofile(filename):
    with open(filename) as f:
         #print(f.read())
          return (f.read())
r=ofile('MAC')
print(r)

def ofile2(filename):
    if os.path.exists(filename):
        with open(filename) as f:
            print(f.read())
    else:
        print('NOT FINF FILE')

ofile2('SWITCHfg')


def kortez(a,b):
    return (a,b)
x,y=kortez(5,6)
print(x)
print(y)
'''

def fun1(a,b,c=True):
    if c:
        print(a+b)
    else:
        print(a-b)

fun1(1,1)
fun1(1,1,False)