#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/27 15:37
# @Author : liuhuiling

print()
'''
二分支结构：
根据判断条件结果而选择不同向前路径的运行方式
if<条件>:
    <语句块1>
else：
    <语句块2>
紧凑形式：适用于简单表达式的二分支结构
<表达式1> if <条件> else <表达式2>

'''
guss = eval(input("请输入一个数字："))
if guss == 99:
    print("猜对了")
else:
    print("猜错了")

guss = eval(input("请输入一个数字："))
print("猜{}了".format("对" if guss == 99 else "错"))
print("猜对了" if guss == 99 else "猜错了")