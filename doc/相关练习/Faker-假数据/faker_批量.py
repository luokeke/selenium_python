#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/23 14:32
# @Author : liuhuiling
from faker import  Faker
import random
import string
f = Faker('zh_CN')
for i in range(1,100):
    print("用户名：", ''.join(random.sample(string.ascii_letters, 8)))
    print("姓名：", f.name())
    print("邮箱：", f.ascii_email())
    print("手机号：", f.phone_number())
