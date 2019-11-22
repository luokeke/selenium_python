#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/23 18:28
# @Author : liuhuiling
#将批量生成的数据，通过接口写入，实现批量造数据
#requests 接口写入数据，excel批量读取数据
import requests
import xlrd
#读取
data = xlrd.open_workbook('data3.xls')  # 打开ecxel表
table = data.sheets()[0]  # 切换到对应的sheet
for i in range(22,24):
    username = table.cell(i, 0).value
    realname = table.cell(i, 1).value
    email = table.cell(i,2).value
    phone = table.cell(i,3).value
    if i%2 == 0:
        userType = 1
    elif i%2 == 1:
        userType = 2
    headers = {"Content-Type": "application/json","X-Access-Token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjY1NDIzNjEsInVzZXJuYW1lIjoiamVlY2cifQ.cENjgqk31R24YHFH2BK0D34Ugw3uumj1NVDsm6mxvIA"}
    url = ' http://122.114.157.115/jeecg-boot/sys/user/add'#请求链接
    json_value = {
    "activitiSync": "1",
    "username": username,
    "password": "ceshi2019",
    "confirmpassword": "ceshi2019",
    "realname": realname,
    "birthday": "",
    "email": email,
    "phone": phone,
    "selectedroles": "1",
    "userType": 0
}
    r = requests.post(url=url, json=json_value, headers=headers)
    print(r.json())
