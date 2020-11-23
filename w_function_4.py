
trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}


def generate_trunk_config(trunk_config,trunk_mode_template):
    for i in trunk_config:
        print(i)
        for z in trunk_mode_template:
            if z.endswith('vlan'):

                #print('VLAN')
                 print(str(trunk_config.get(i)))
                #z=z+str(trunk_config.get(i))
            print(z)


generate_trunk_config(trunk_config,trunk_mode_template)