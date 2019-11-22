#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/28 21:47
# @Author : liuhuiling
import requests
'''GET POST PUT DELETE HEAD OPTINOS'''
r = requests.get('https://api.github.com/events') #GET请求
r = requests.post('http://httpbin.org/post', data={'key': 'value'})#POST请求
r = requests.put('http://httpbin.org/put', data = {'key':'value'})
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')
#传递 URL 参数
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)
#响应内容
print(r.text)
r.encoding = 'ISO-8859-1' #utf-8
#二进制响应内容
print(r.conte)
#json响应内容
print(r.json())
#原始响应内容
print(r.raw)
#定制请求头
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
#更加复杂的 POST 请求
import requests
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)
