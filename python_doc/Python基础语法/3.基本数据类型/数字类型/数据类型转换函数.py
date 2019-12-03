#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/22 17:37
# @Author : liuhuiling
print("数据类型转换")
'''
int(x) 将x变成整数，舍弃小数部分
float(x) 将x变成浮点数，增加小数部分
complex(x) 将x变成复数，增加小数部分
str(x)  将x变为字符串类型
'''
print(int(123.43)) #123
print(int("123")) #123
print(float(12)) #12.0
print(float("123.02")) #123.02
print(complex(4))# (4+0j)

print(type(str(12))) # <class 'str'>
print(type(12))# <class 'int'>