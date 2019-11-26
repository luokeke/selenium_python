#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/25 16:56
# @Author : liuhuiling

import requests

files = {'file': open('E:\\log.txt', 'rb')} #先建一个文件
r = requests.post("http://127.0.0.1:5000/upload", files=files)
result = r.json()
print(result)

'''
结果：{'message': 'upload success!', 'code': 10200}
'''