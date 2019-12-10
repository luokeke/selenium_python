#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/9 18:03
# @Author : liuhuiling
'''
集合操作符： 6 个
操作符及应用         描述
S | T                并，返回一个新集合，包括在集合S和T中的所有元素
S - T                差，返回一个新集合，包括在集合S但不在T中的元素
S & T                交，返回一个新集合，包括同时在集合S和T中的元素
S ^ T                补，返回一个新集合，包括集合S和T中的非相同元素
S <= T 或 S < T      返回True/False，判断S和T的子集关系
S >= T 或 S > T      返回True/False，判断S和T的包含关系
增强操作符 4个
操作符及应用         描述
S |= T              并，更新集合S，包括在集合S和T中的所有元素
S -= T              差，更新集合S，包括在集合S但不在T中的元素
S &= T              交，更新集合S，包括同时在集合S和T中的元素
S ^= T              补，更新集合S，包括集合S和T中的非相同元素
'''
A = {"p","y",123,("python",123)}
B = set("pypy123")
print(A|B) #{123,("python",123),'3', 'p', '1', '2', 'y'}
print(A-B) #{123,("python",123)}
print(A&B) #{'p',  'y'}
print(A^B)#{123,("python",123),'3',  '1', '2'}