#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/21 14:08
# @Author : liuhuiling

#熟悉技术的产品经理，

print (9 > 9) and (9 < 9) # False
print (9 > 8) or (8 > 9)  # True
print (not ((9 > 9) and (9 < 9)) )# True

'''
Python逻辑运算符  不仅仅返回布尔值，还可以返回数值
以下假设变量 a 为 10, b为 20:
运算符	    逻辑表达式	   描述	                                                                     实例
and	        x and y	      布尔"与"- 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
or	        x or y	      布尔"或" - 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。	        (a or b) 返回 10。
not	        not x	      布尔"非"- 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	     not(a and b) 返回 False
'''
a = 10
b = 20
print(10 and 20) #20
print(10 or 20) #10
print(0 or 25) #25
print(not b) #False
