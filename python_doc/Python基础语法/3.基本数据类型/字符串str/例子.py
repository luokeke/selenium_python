#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/3 12:33
# @Author : liuhuiling
import os
'''一串文字，中间都数字，让我把数字输出并且顺序反转一下'''
str = "1sad4f5sadf155as12fdasdfasd4412d"
str1 = "0123456789"
str3 = ""
for i in range(len(str)):
    if str[i] in str1:
        str3 += str[i]
print(str3)#正序
print(str3[::-1])#倒叙

'''
字符串操作
-- x+y  连接两个字符串x和y
-- n*x  或者 x*n 复制n次字符串x
-- x in s 如果x是s的子串，返回Ture,否则返回False
索引和切片
--  索引：返回字符串中单个字符，str[i]  返回索引为i的字符
--  切片：返回字符串中一段字符子串，str[m:n]  截取m到n-1的子串

切片高级用法
str[m:n]，m缺失表示至开头，n缺失表示至结尾
str[m:n：k] ，根据步长k对字符串切片
str[::-1] ，逆序,步长为-1，即从后向前逐一的取出从开头到结尾的所有字符串

'''
