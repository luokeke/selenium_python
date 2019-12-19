#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/21 23:46
# @Author : liuhuiling
print(())
'''
参考链接：有趣的赋值操作 https://blog.csdn.net/weixin_33894992/article/details/85120575
Python语言支持序列解包（Sequence Unpacking）、链式赋值（Chained Assignments）和增量赋值（Augmented Assignments）  
1.序列解包      是指将多个值赋给多个变量
    x,y,z = 1,2,3      print(x,y,z)    结果：1 2 3
    同时将多个值赋给多个变量的操作，等号（=）右侧的值与左侧的变量个数必须相等，否则会抛出异常
    Python语言的这种特性称为序列解包（Sequence Unpacking），其实任何一个可迭代（Iterable）的对象都支持这一特性
    
    利用序列解包交换x和y的值
    x,y = 20,30      x,y = y,x      print(x,y)  结果：30 20  
2.链式赋值      是指将同一个值连续赋给多个变量 
    x = y = 20
3.增量赋值      是指将变量自身增加或减小（负增量）指定值的表达式的简化形式
    x = x + 2，如果用增量赋值表达式，可以写成   x += 2
    x = x % 3可以写成    x %= 3
'''

'''
Python赋值运算符
以下假设变量a为10，变量b为20：
运算符	    描述	                实例
=	        简单的赋值运算符	    c = a + b 将 a + b 的运算结果赋值为 c
增量赋值
+=	        加法赋值运算符	        c += a 等效于 c = c + a
-=	        减法赋值运算符	        c -= a 等效于 c = c - a
*=	        乘法赋值运算符	        c *= a 等效于 c = c * a
/=	        除法赋值运算符	        c /= a 等效于 c = c / a
%=	        取模赋值运算符	        c %= a 等效于 c = c % a
**=	        幂赋值运算符	        c **= a 等效于 c = c ** a
//=	        取整除赋值运算符	    c //= a 等效于 c = c // a
'''