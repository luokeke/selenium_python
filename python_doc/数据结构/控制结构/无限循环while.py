#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/28 10:04
# @Author : liuhuiling
print()
'''
无限循环 由条件控制的循环运动方式
while <条件>：
    <语句块>
- 反复执行语句块，直到条件不满足时结束

'''
a = 3
while a > 0:
    a = a-1 #若条件为a = a+1 会无线循环，需要Ctrl + c 退出
    print(a)