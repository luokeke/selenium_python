#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/26 10:45
# @Author : liuhuiling

weekstr = "星期一星期二星期三星期四星期五星期六星期日"
weekId = eval(input("请输入星期数字（1-7）："))
pos = (weekId-1)*3
print(pos)
print(weekstr[pos:pos+3])

''' 
数字 对应索引      切片
1   0 1 2           0:3
2   3 4 5           3:6
3   6 7 8           6:9
4   9 10 11         9:12
5   12 13 14        12:15
6   15 16 17        15:18
7   18 19 20        18:21
'''
