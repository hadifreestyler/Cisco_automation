#sudo apt install python3-pip
#sudo pip3 install -U netmiko
#https://pynet.twb-tech.com/blog/automation/netmiko.html
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

#output = net_connect.find_prompt()
#print(output)
'''
config_commands = ['hostn S', 'hostn Switch1']  

output = net_connect.send_config_set(config_commands)
print(output)
'''

output = net_connect.send_command("show run | inc logging")

print(output)




