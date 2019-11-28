#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/28 15:25
# @Author : liuhuiling
print()
'''
圆周率计算问题分析：
- 近似计算
- 蒙特卡罗方法

'''
from random import random
from time import perf_counter #对程序运行计时
DARTS = 1000*1000
hits = 0.0
start = perf_counter() #启动计时
for i in range(1,DARTS+1):
    x,y = random(),random() #random [0.0,1.0)之间的小数
    dist = pow(x**2+y**2,0.5) #计算点到圆心的距离
    if dist <=1.0: #使用的是单位正方形，所以到圆心的距离<=1.0
        hits = hits +1
pi = 4*(hits/DARTS)
print("圆周率值是：{}".format(pi))
print("运行时间是：{:.5f}s".format(perf_counter()-start))

