import re
with open('config_r1') as f:
    #print(f.read())
    for line in f:
        find=re.search('ip address \S+',line)
        #print(find.group())
        try:
            if find:
                print(find.group())
        except ArithmeticError as err:
            pass



