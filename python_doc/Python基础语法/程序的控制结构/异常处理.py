#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/27 17:47
# @Author : liuhuiling
print()
'''
异常处理的基本使用
try:
    <语句块1>
except:
    <语句块2>
try:
    <语句块1>
except<异常类型>:
    <语句块2>
    
异常处理的高级使用
try：
    <语句块1>
except:     #发生异常执行语句块2
    <语句块2> 
else:       #else 对应的语句块3，在不发生异常时执行
    <语句块3>
finally:    #finally 对应的语句块4一定执行
    <语句块4>
      
'''
#示例一
try:
    num = eval(input("请输入一个整数："))
    print(num**2)
except:
    print("输入的不是整数")
#示例二
try:
    num = eval(input("请输入一个整数："))
    print(num**2)
except NameError:
    print("输入的不是整数")
