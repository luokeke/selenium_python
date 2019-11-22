#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/23 17:42
# @Author : liuhuiling
#将批量生成的数据，通过接口写入，实现批量造数据
#requests 接口写入数据，excel批量读取数据
import requests
import xlrd
#读取
data = xlrd.open_workbook('data3.xls')  # 打开ecxel表
table = data.sheets()[0]  # 切换到对应的sheet
for i in range(50,100):
    username = table.cell(i, 0).value
    realname = table.cell(i, 1).value
    email = table.cell(i,2).value
    phone = table.cell(i,3).value
    if i%2 == 0:
        userType = 1
    elif i%2 == 1:
        userType = 2
    headers = {
        "Content-Type": "application/json",
        "X-Access-Token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjY5NTY1NTUsInVzZXJuYW1lIjoiamVlY2cifQ.d7ng8dfvb55K1ItmacLkhe4Y6RBq9fOidWmoEyUBbZI"}
    url = 'http://122.114.157.115/jeecg-boot/sys/user/addCustomer'#请求链接
    json_value = {
    "id": "",
    "username": username,
    "realname": realname,
    "userType": userType,
    "email": email,
    "phone": phone
    }
    r = requests.post(url=url, json=json_value, headers=headers)
    print(r.json())
