#!/usr/bin/env python3

import requests, sys

class Tendown:
    def login(self):
        try:
            r = requests.post('http://' + self.ip + ':' + str(self.port) + '/login/Auth', data={'username':'user', 'password':'user'}, allow_redirects=False)
        except:
            raise ValueError('Connection Error!')
            return 
        if r.status_code == 302:
            self.cookie = r.cookies['password']
        else:
            raise ValueError('Unexpected status code %s! Something is wrong!' % (str(r.status_code)))

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.cookie = 'user'
        login(self)

    def post_request(self, url, pdata):
        try:
            r = requests.post('http://' + self.ip + ':' + str(self.port) + url, data=pdata, allow_redirects=False)
        except:
            raise ValueError('Connection Error!')
        if r.status_code != 200:
            self.cookie = 'user'
            login(self)
        try:
            r = requests.post('http://' + self.ip + ':' + str(self.port) + url, data=pdata, allow_redirects=False)
        except:
            raise ValueError('Connection Error!')
        if r.status_code != 200:
            raise ValueError('Unexpected status code %s! Something is wrong!' % (str(r.status_code)))

    def firmware_update(self, filename):
        pdata = open(filename, 'rb').read()
        try:
            r = requests.post('http://' + self.ip + ':' + str(self.port) + url, data=pdata, allow_redirects=False, headers={'Content-Type': 'application/octet-stream'})
        except:
            raise ValueError('Connection Error!')
        if r.status_code != 200:
            self.cookie = 'user'
            login(self)
        try:
            r = requests.post('http://' + self.ip + ':' + str(self.port) + url, data=pdata, allow_redirects=False, headers={'Content-Type': 'application/octet-stream'})
        except:
            raise ValueError('Connection Error!')
        if r.status_code != 200:
            raise ValueError('Unexpected status code %s! Something is wrong!' % (str(r.status_code)))

if __name__ == "__main__":
    print('test')
