#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/2 9:53
# @Author : liuhuiling
print()
'''
labmda函数返回函数名作为结果
- lambda函数是一种匿名函数，即没有名字的函数
- 使用lambda保留字定义，函数名是返回结果
- lambda函数用于定义简单的、能够在一行内表示的函数

<函数名> = lambda <参数>:<表达式> #只能使用表达式，不能使用函数体
等价于
def<函数名>(<参数>):
    <函数体>
    return <返回值>
谨慎使用lambda函数
- lambda函数主要用作一些特定函数活方法参数
- lambda函数有一些固定使用方式，建议逐步掌握
- 一般情况，建议使用def定义的普通函数

'''
f = lambda x,y:x+y
f(10,15) #25
f = lambda :"PYTHON123.io"
print(f()) #PYTHON123.io