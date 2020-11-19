with open('SWITCH_NEW','w') as r:
    r.seek(0)
    r.close()

slovar={}
ignore=['alias','auto']
with open('SWITCH') as f:
    #print(f.read())
    for line in f:
        if line.startswith('!'):
            pass
        else:
            for x in ignore:
                if x in line:
                    break
                else:
                    print(line)
                    with open('SWITCH_NEW','a+') as r:
                        r.write(line)

r.close()
