#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/25 16:56
# @Author : liuhuiling

import requests

auth = ("admin", "admin123")
r = requests.post("http://127.0.0.1:5000/auth", auth=auth)
result = r.json()
print(result)

'''
结果：{'code': 10200, 'message': 'Authorization success!'}
'''