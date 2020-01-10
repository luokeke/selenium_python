#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/27 14:44
# @Author : liuhuiling
import time
scale = 50
print("执行开始".center(scale//2,"-"))
start = time.perf_counter()
for i in range(scale+1):
    a = '*'*i
    b = ','*(scale - i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,"-"))
'''
print("\n"+"执行开始".center(scale//2,"-"))
str.center(width[,fillchar]) 字符串str根据宽度width居中，以fillchar进行填充（fillchar可选）
'''
'''
结果：
-----------执行开始----------
100%[**************************************************->]5.06s
-----------执行开始----------
'''