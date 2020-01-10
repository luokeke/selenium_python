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
pi = 0
N = 100
for k in range(N):
    pi += 1/pow(16,k)*(
        4/(8*k+1)-2/(8*k+4)-
        1/(8*k+5)-1/(8*k+6))
print("圆周率值是：{}".format(pi))
