#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/27 17:35
# @Author : liuhuiling
print()
'''
条件判断，比较运算符
操作符     数学符号     描述
<           <           小于
<=          <=          小于等于
>=          >=          大于等于
>           >           大于
==          =           等于
!=          ≠          不等于
条件组合，保留字
操作符及使用          描述
x and y             两个条件x和y的逻辑与
x or y              两个条件x和y的逻辑或
not x               条件x的逻辑非
'''
guss = eval(input("请输入猜的数据："))
if guss>99 or guss <99:
    print("猜错了")
else:
    print("猜对了")