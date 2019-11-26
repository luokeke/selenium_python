#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2018/3/14 14:39 

import requests
#request模块练习
#发送请求
# r = requests.get('https://github.com/timeline.json')
# r = requests.post("http://httpbin.org/post")
# r = requests.put("http://httpbin.org/put")
# r = requests.delete("http://httpbin.org/delete")
# r = requests.head("http://httpbin.org/get")
# r = requests.options("http://httpbin.org/get")

#传递 URL 参数
#
# payload = {'key1': 'NULL', 'key2': 'value2'}
# r = requests.get("http://httpbin.org/get", params=payload)
# print(r.url)
#将一个列表作为值传入
# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
# r = requests.get('http://httpbin.org/get', params=payload)
# print(r.url)

#响应内容
# r = requests.get('https://developer.github.com/v3/activity/events/#list-public-events')
# r.encoding = 'ISO-8859-1'
# print  r.text
# # u'[{"repository":{"open_issues":0,"url":"https://github.com/...

# r = requests.get('https://github.com/timeline.json')
# r.json()
# print  r.json()
# # [{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...

#定制请求头



payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)
# {
#
#   "form": {
#     "key2": "value2",
#     "key1": "value1"
#   },
#
# }