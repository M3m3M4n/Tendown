#!/usr/bin/env python3

import requests, sys

def login(ip, port=80):
	try:
		r = requests.post('http://' + ip + ':' + str(port) + '/login/Auth', data={'username':'user', 'password':'user'}, allow_redirects=False)
		print(r.cookies['password'])
	except:
		print('Connection Error!')
		sys.exit()
	if r.status_code == 302:
		cookie = r.cookies['password']
	else:
		print('Unexpected status code %s! Something is wrong!' % (str(r.status_code)))
		sys.exit()
	return cookie

def update(firmware_name, ip, port=80):
	return 0

login('192.168.0.1')
