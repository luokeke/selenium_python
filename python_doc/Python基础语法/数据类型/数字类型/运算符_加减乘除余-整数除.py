#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/22 16:46
# @Author : liuhuiling
print(10//3)#3
print(10%3)#1
'''
x+y  加，x与y之和
x-y  减，x与y之差
x*y  乘，x与y之积

x/y  除，x与y之商，10/3结果是3.3333333333333335
x//y 整数除，x与y之整数商，10//3 结果是3
x%y 余数，模运算 10%3结果是1

x**y 幂运算，x的y次幂；当y是小数时，开方运算 10**0.5结果是√10
+x  x本身
-y  y的负值
'''
'''
增量赋值
x op= y 即 x = x op y，op为二元操作符 
x += y x -= y x *=y  x /= y
x //= y x %= y 
x **= y  与 x = x**y等价
'''
x = 1.2
x1=1.2
x **= 3
x1 = x1 **3
print(x,x1)#1.7279999999999998 1.7279999999999998
