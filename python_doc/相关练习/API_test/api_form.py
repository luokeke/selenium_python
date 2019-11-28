#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/28 20:29
# @Author : liuhuiling

import requests

'''POST请求from-data/x-www-from-urlencode'''

payload = {"username": "admin", "password": "a123456"}
r = requests.post("http://127.0.0.1:5000/login", data=payload)
result = r.json()
print(result)

'''
结果：{'message': 'login success', 'code': 10200}
'''