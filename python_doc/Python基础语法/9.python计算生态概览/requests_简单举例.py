#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/1/8 11:36
# @Author : liuhuiling
import requests
r = requests.get("https://api.github.com/user",auth = ("user","pass"))
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
