import os
'''
def ofile(filename):
    with open(filename) as f:
         #print(f.read())
          return (f.read())
r=ofile('MAC')
print(r)
'''

def ofile2(filename):
    if os.path.exists(filename):
        with open(filename) as f:
            print(f.read())
    else:
        print('NOT FINF FILE')

ofile2('SWITCHfg')