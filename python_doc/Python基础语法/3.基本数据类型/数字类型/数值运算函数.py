#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/22 17:07
# @Author : liuhuiling
print(pow(2,15)) #32768
print(pow(2,-15)) #3.0517578125e-05
print(pow(2,10,10)) #1024%10 = 4

'''
abs(x) 绝对值，x的绝对值
divmod(x,y) 商余，(x//y,x%y) ，同时输出商和余数
pow(x,y)函数，计算x的y次幂即 x**y ，想算多大，算多大
pow(x,y[,z]) 幂余，其效果等于，pow(x,y)%z 即(x**y)%z（余数）,[..]表示参数z可省略
round(x,d):对x四舍五入，d是小数截取尾数，默认值为0 
    浮点数间运算及比较用 round()函数辅助
max(x1,x2,...,xn)  最大值，返回x1,x2,...,xn中的最大值，n不限
min(x1,x2,...,xn)  最小值，返回x1,x2,...,xn中的最小值，n不限

'''
''' round(x,d) d 可为0'''
print(round(1.235698))  #1 默认为0，即不保留小数。
print(round(1.235698,2))  #1.24，保留2位小数
print(round(0.1+0.2) == 0.3) #False
print(round(0.1+0.2,1) == 0.3)#Ture
'''max 和 min'''
print (max("abcd") ) #d
print (min("abcd") ) #a
print (max(1,3,45,0) ) #45
print (min(1,3,45,0) ) #0