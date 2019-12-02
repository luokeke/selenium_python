#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/29 9:17
# @Author : liuhuiling
#n的阶乘
def fact(n): #fact函数名 n参数
    s  = 1
    for i in range(1,n+1):
        s *= i
    return  s #返回值
