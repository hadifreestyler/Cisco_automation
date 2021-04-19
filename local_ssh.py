#sudo apt install python3-pip
#sudo pip3 install -U netmiko

#!/usr/bin/env python

from netmiko import ConnectHandler

nx_os = {

	'device_type': 'cisco_ios',
	'ip': '10.1.1.180',
	'username': 'hadi',
	'password': 'hadi',
	'port': 22
		}

net_connect = ConnectHandler(**nx_os)
output = net_connect.send_command('show ip int brief')
print(output)



