#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/27 15:10
# @Author : liuhuiling
print()
'''
文本进度条的不同设计函数
设计名称 趋势 设计函数
Linear Constant f(x) = x
Early Pause Speeds up f(x) = x+(1-sin(x*π*2+π/2)/-8
Late Pause Slows down f(x) = x+(1-sin(x*π*2+π/2)/8
Slow Wavy Constant f(x) = x+sin(x*π*5)/20
Fast Wavy Constant f(x) = x+sin(x*π*20)/80
Power Speeds up f(x) = (x+(1-x)*0.03)2
Inverse Power Slows down f(x) =1+(1-x)1.5 *-1
Fast Power Speeds up f(x) = (x+(1-x)/2)8
Inverse Fast Power Slows down f(x) = 1+(1-x)3 *-1

'''
