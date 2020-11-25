import re
data=()
with open('config_r1') as f:
    #print(f.read())
    for line in f:
        find=re.search('ip address (?P<ip>\S+) (?P<mask>\S+)',line)
        #print(find.group())
        try:
            if find:
                 #print(find.group())
                 ip,mask=find.groups()
                 #print(ip,mask)
                 data=data+find.groups()
                 #print(data)
                 #print((find.groupdict()))

        except ArithmeticError as err:
            pass

    print(data)



