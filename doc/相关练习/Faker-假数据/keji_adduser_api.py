#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/23 17:42
# @Author : liuhuiling
#
import requests
headers = {"Content-Type": "application/json",
           "X-Access-Token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjY5OTAyOTQsInVzZXJuYW1lIjoiamVlY2cifQ.LCh-caTmPZXQ639d0-UqVD2AFCTaT7vf4V9QQT7KNLo"}
url = 'http://122.114.157.115/jeecg-boot/sys/user/addCustomer'#请求链接
json_value = {
    "id": "",
    "username": 'lihemma',
    "realname": "李m赫马",
    "userType": 2,
    "email": "15446m4@zzidc.com",
    "phone": "1529m8745696"
}
r = requests.post(url=url, json=json_value, headers=headers)
print(r.json())
print (r.text)
print (r.status_code)

# #form传参
# data_value="bucketName=lgw"
# def test_qualification_add():
#     if canshu=="0":
#         r = requests.post(url=url, headers=headers)  # 发送请求
#     else:
#         if headers=={"Content-Type": "application/x-www-form-urlencoded"}:
#             r = requests.post(url=url, data=data_value, headers=headers)  # 发送请求
#         elif headers=={"Content-Type": "application/json"}:
#             r = requests.post(url=url, json=json_value, headers=headers)  # 发送请求
#     return r.json
#     print (r.text)  # 获取响应报文
#     print (r.status_code)
# test_qualification_add()