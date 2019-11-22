#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/4 14:39
# @Author : liuhuiling
# https://www.cnblogs.com/insane-Mr-Li/p/9092619.html

import xlrd

fname = '更新站点.xlsx'#设置文件名和路径
date = xlrd.open_workbook(fname)# 打开文件
#获取当前文档的表(得到的是sheet的个数，一个整数）
table = date.sheet_by_name(u"国内")
guonei = table.row_slice(0)
print (guonei)
n = table.col(0, start_rowx=0, end_rowx=None)  #返回由该列中所有的单元格对象组成的列表
m = table.col_slice(0, start_rowx=0, end_rowx=None)  #返回由该列中所有的单元格对象组成的列表
j = table.col_types(0, start_rowx=0, end_rowx=None)    #返回由该列中所有单元格的数据类型组成的列表
k = table.col_values(0, start_rowx=0, end_rowx=None)   #返回由该列中所有单元格的数据组成的列表
print(n)
print(m)
print(j)
print(k)