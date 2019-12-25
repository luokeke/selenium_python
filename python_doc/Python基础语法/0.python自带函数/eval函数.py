#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/26 12:10
# @Author : liuhuiling
print()
'''
eval(<字符串或字符串变量>) 评估函数
把<字符串或字符串变量>外层的引号去掉，并执行余下语句的函数
'''
print(eval("2+   1"))  #3
print(eval("21"))#21
print(eval('print("Hello")')) #Hello
# print(eval([1,'a'])) # 1 a
# print(eval((1,'a')))  # 1 a
# print(eval({'name':'lili','age':'12'}))

a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
print(type(a))
b = eval(a)
print(type(b))
print(b)

