#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/25 14:10
# @Author : liuhuiling

'''
获取星期字符串
-- 输入：1-7的整数，表示星期几
-- 输出：输入整数对应的星期字符串
-- 例如：输入3，输出星期三
这种方法比较繁琐，更简洁的参考v1  v2  其中v2最简洁
'''

num = input("请输入星期数字(1-7)：")
week = int(num)

if week == 1:
    print("今天天是星期一")
elif week == 2:
    print("今天天是星期二")
elif week == 3:
    print("今天天是星期三")
elif week == 4:
    print("今天天是星期四")
elif week == 5:
    print("今天天是星期五")
elif week == 6:
    print("今天天是星期六")
elif week == 7:
    print("今天天是星期日")
else:
    print("请输入正确的星期数字")

