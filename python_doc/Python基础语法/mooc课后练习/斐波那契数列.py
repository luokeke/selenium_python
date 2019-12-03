#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/3 12:43
# @Author : liuhuiling
'''
斐波那契数列
斐波那契数列（Fibonacci sequence），又称黄金分割数列、因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）
以兔子繁殖为例子而引入，故又称为“兔子数列”，
指的是这样一个数列：1、1、2、3、5、8、13、21、34、……
在数学上，斐波那契数列以如下被以递推的方法定义：
F(1)=1，F(2)=1,
F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）
'''
def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1)+f(n-2)
