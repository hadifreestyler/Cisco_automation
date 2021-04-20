#TSHARK

#sudo apt-get install tshark
#pip3 install pyshark

#tshark -w file.pcap

import pyshark

#cap = pyshark.FileCapture('/Users/hadi/Desktop/test.pcap')
#print(cap[20].icmp.type)
#cap[20].show()

capture = pyshark.LiveCapture ("en0")
for packet in capture:
	print(capture)
	#if 'ospf' in capture:
		#print('OSPF password: ' + capture.icmp.auth_simple)

