#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/6 10:05
# @Author : liuhuiling


#split 将输入的字符串数据转换为列表 ,输入的数据转化为列表元素
#new_site =input( "输入站点名称(站点之间请用空格隔开,退出输入exit)：")
new_site = "www_zzidc_com     www_kuaiyun_cn    "
list0 = new_site.split(" ")
print(list0)
# Python - 去除list中的空字符和None https://www.cnblogs.com/yspass/p/9434366.html
list1 = list(filter(None, list0))
# 列表元素去重  https://www.cnblogs.com/yunlongaimeng/p/8728647.html
list = sorted(set(list1),key=list1.index)
# 列表获取 excel元素  https://www.cnblogs.com/insane-Mr-Li/p/9092619.html
import xlrd
# # fname = '更新站点.xlsx'#设置文件名和路径
# date = xlrd.open_workbook(fname)# 打开文件
# guonei = date.sheet_by_name("国内").col_values(0, start_rowx=0, end_rowx=None)

print(list1)