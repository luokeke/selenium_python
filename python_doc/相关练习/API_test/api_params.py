#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/23 18:11
# @Author : liuhuiling
import requests
'''POST请求params格式传参  application/x-www-form-urlencoded'''
#两个头部都可以
# headers = {
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Content-Type": "charset=UTF-8",
#     "cookie": "JSESSIONID=3A8584F2D2128A2DC6E875B44D000B97"}
headers = {"cookie": "JSESSIONID=39119A20F66560CDC12880F29FC0589D"}   #cookie会过期，需要更新
url = 'https://zhuzhan.gainet.com/site/getSites.action'#请求链接
date ={
    'siteVo.domain': 'beian.zzidc.com',
    'siteVo.flag': '-1',
    'siteVo.interface_type': '-1',
    'page': '1',
    'rows': '50'}
r = requests.post(url=url, params=date, headers=headers) #注意 params
print(r.json())
print (r.text)
print (r.status_code)
print (r.content)

# 抓包信息如下
'''
POST https://zhuzhan.gainet.com/site/getSites.action HTTP/1.1
Host: zhuzhan.gainet.com
Connection: keep-alive
Content-Length: 84
Accept: application/json, text/javascript, */*; q=0.01
DNT: 1
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36
Sec-Fetch-Mode: cors
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: https://zhuzhan.gainet.com
Sec-Fetch-Site: same-origin
Referer: https://zhuzhan.gainet.com/site/sites.action
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=3A8584F2D2128A2DC6E875B44D000B97

siteVo.domain=beian.zzidc.com&siteVo.flag=-1&siteVo.interface_type=-1&page=1&rows=50
'''