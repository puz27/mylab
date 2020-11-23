port_security_template = [
    'switchport port-security maximum 2',
    'switchport port-security violation restrict',
    'switchport port-security'
]
access_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

intf_vlan_mapping = {'FastEthernet0/12':10,
                     'FastEthernet0/14':11,
                     'FastEthernet0/16':17}


def generate_access_config(intf_vlan_mapping, access_template):
    print(access_template)
    print(intf_vlan_mapping)

    for i in intf_vlan_mapping:
        print(i)
        for z in  access_template:
            if z.endswith('vlan'):
                #intf_vlan_mapping.get(i)
                #print('VLAN')
                z=z+ str(intf_vlan_mapping.get(i))
            print(z)


generate_access_config(intf_vlan_mapping, access_template)
