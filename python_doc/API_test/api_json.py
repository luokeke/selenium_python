#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/28 19:58
# @Author : liuhuiling
import requests

'''POST请求json格式传参 application/json'''

payload = {"name": "jack", "age": 22, "height": 177}
r = requests.post("http://127.0.0.1:5000/add_user", json=payload)
result = r.json()
print(result)

'''
报错：json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
'''