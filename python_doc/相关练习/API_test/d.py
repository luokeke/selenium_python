#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/28 22:06
# @Author : liuhuiling
import requests
'''POST请求json格式传参 application/json'''
headers = {"Content-Type": "application/json"}
# url = 'http://vhostapi.zzidc.com:60018/restful/vhost/domainManage/queryTemplateState'#请求链接
# date = {
#     "contactid":3883,
# 	"jkbh":100012
# }
url = 'http://vhostapi.zzidc.com:60018/restful/vhost/domainBiz/dealAliDomainBiz'#请求链接
date = {"lx":6}

r = requests.post(url=url, json=date, headers=headers)  # 注意 json
print(r.json())
print (r.status_code)





