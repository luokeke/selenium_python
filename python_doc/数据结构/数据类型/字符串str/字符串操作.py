#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/25 13:56
# @Author : liuhuiling
'''
-- x+y 连接两个字符串x和y
-- n*x 或者 x*n 复制n次字符串x
-- x in s 如果x是s的子串，返回Ture,否则返回False
'''
x="123"
y="456"
s="123789"
print(x+y)#123456
print(3*x) #123123123
print(x*3) #123123123
print(x in s) #True
print(y in s) #False