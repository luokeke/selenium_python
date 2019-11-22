#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/21 18:11
# @Author : liuhuiling
'''
一串文字，中间都数字，让我把数字输出并且顺序反转一下
'''
str = 'sdfasdf1213asdf5asd32'
str2 = '0123456789'
str3=''
for i in range(len(str)):
    if str[i]  in str2:
        j = str[i]
        str3 += j
print (str3)#正序
print(str3[::-1])#倒叙