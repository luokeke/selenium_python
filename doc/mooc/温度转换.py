#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/20 17:27
# @Author : liuhuiling

T= input("请输入温度值（例如：82F,52C）：")
if T[-1] in ['F','f']:
    C = (eval(T[0:-1])-32)/1.8
    print("转换后的温度值为：{: 2f}".format(C))
elif T[-1] in ['C','c']:
    F = eval(T[0:-1])*1.8+32
    print("转换后的温度值为：{:.2f}".format(F))
else:
    print("请输入正确的温度值")