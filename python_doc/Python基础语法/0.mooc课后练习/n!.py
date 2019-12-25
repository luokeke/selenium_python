#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/29 9:17
# @Author : liuhuiling
'''
阶乘是基斯顿·卡曼（Christian Kramp，1760～1826）于 1808 年发明的运算符号，是数学术语。1808年，基斯顿·卡曼引进这个表示法。
一个正整数的阶乘（factorial）是所有小于及等于该数的正整数的积，并且0的阶乘为1。
自然数n的阶乘写作n!。亦即n!=1×2×3×...×(n-1)n。
阶乘亦可以递归方式定义：0!=1，n!=(n-1)!×n。
'''
def fact(n): #fact函数名 n参数
    s  = 1
    for i in range(1,n+1):
        s *= i
    return  s #返回值

def fact1(n): #递归函数
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
