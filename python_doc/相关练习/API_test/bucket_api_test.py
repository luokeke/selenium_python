 #!/usr/bin/env python
#coding=utf-8
import requests
import json
import unittest
canshu=""#如果为空填写0.其他为需要传参并在下面data中填写参数
headers = {"Content-Type": "application/x-www-form-urlencoded"}#传参方式application/x-www-form-urlencoded   application/json   等等
url = 'http://storageapi.kuaiyun.cn:60020/gainet/cloudstorage/judgeHttps'#请求链接
json_value = {
    'bucketName': 'u123'
    #'ipdz': '122.114.196.140',
    # #'memberId':'288634'
}
#form传参
data_value="bucketName=luokeke007"
def test_qualification_add():
    #url = "http://web2.zzidc.com:8117/restful/glht/glht/getVmIP?resource=VG3OQ81wtrNGANeuq8IdwTBhgkAF53lFOIY6aCIBeo0=&ywlx=0"  # 测试的接口url
    if canshu=="0":
        r = requests.post(url=url, headers=headers)  # 发送请求
    else:
        if headers=={"Content-Type": "application/x-www-form-urlencoded"}:
            r = requests.post(url=url, data=data_value, headers=headers)  # 发送请求
        elif headers=={"Content-Type": "application/json"}:
            r = requests.post(url=url, json=json_value, headers=headers)  # 发送请求
    # return r.json
    print (r.text)  # 获取响应报文
    print (r.status_code)
test_qualification_add()