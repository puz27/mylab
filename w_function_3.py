
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

generate_access_config(intf_vlan_mapping, access_template)
