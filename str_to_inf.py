string='1.2.3.4'
integer=[]
for octet in string.split('.'):
    print(int(octet))
    z=int(octet)
    integer.append(z)

print(integer)
