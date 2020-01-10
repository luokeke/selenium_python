#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/6 10:05
# @Author : liuhuiling

'''
获得用户输入的一个华氏温度值，将其转换成摄氏温度并输出，保留小数点后两位
I   输入：一个数字  华氏温度值
P   处理：
    1.输入是任意实数，即浮点类型
    2.公式  C = (F -32) / 1.8  F: 华氏温度，C：摄氏温度
O   输出：保留两位小数 "{:.2f}".format()
'''
F = eval(input())
C = (F - 32) / 1.8
print("{:.2f}".format(C))
