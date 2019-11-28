#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/25 16:54
# @Author : liuhuiling

import requests

headers = {"Content-Type": "application/json",
            "token": "3d80caXELzU1aWmHwxl0TzW7jtterObm8l5EeAfipnhyaKmhFl8KdhFRvy4"}
r = requests.post("http://127.0.0.1:5000/header", headers=headers)
result = r.json()
print(result)


'''
结果：{'data': {
                'Content-Type': 'application/json', 
                'token': '3d80caXELzU1aWmHwxl0TzW7jtterObm8l5EeAfipnhyaKmhFl8KdhFRvy4'
                },
 'code': 10200, 
 'message': 'header ok!'}
'''