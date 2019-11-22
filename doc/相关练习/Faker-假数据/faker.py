#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/23 13:52
# @Author : liuhuiling
import random
import string
from faker import  Faker

f = Faker('zh_CN')
print ("用户名：",''.join(random.sample(string.ascii_letters, 8)) )
print("姓名：",f.name())
print("邮箱：",f.ascii_email())
print("手机号：",f.phone_number())
# print("用户名：", f.user_name())
# print("身份证号",f.ssn())
# print("公司",f.company())
# print("信用卡号",f.credit_card_number(card_type=None))
# print("地址：",f.address())
# print("text:",f.text())

# print("姓名：",faker.name)
# print("地址：",faker.address)
# print("text:",faker.text)
