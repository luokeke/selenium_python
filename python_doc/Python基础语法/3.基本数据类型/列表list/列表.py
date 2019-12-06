#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/21 14:04
# @Author : liuhuiling
import time
'''
列表类型 
由0个或多个数据组成的有序序列
列表使用[]表示，采用逗号，分隔各元素
使用保留字 in 判断一个元素是否在列表中
列表和元组
进行的操作包括 索引[]，切片[m,n,k]，加 + ，乘 * ，检查成员 in

- 添加元素 list.append("www_zzidc_com") 
- 删除元素 del list[0] 
- 截取列表 list[i:] 从第i+1个元素开始截取列表

Python列表脚本操作符      列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。

Python表达式               	结果            	           描述
len([1, 2, 3])              3	                           长度
[1, 2, 3] + [4, 5, 6]    	[1, 2, 3, 4, 5, 6]	           组合
['Hi!'] * 4             	['Hi!', 'Hi!', 'Hi!', 'Hi!']   重复
3 in [1, 2, 3]	            True	                       元素是否存在于列表中
for x in [1, 2, 3]: print x,	1 2 3	                   迭代

Python列表函数&方法
函数
cmp(list1, list2)   比较两个列表的元素
len(list)   列表元素个数
max(list)   返回列表元素最大值
min(list)   返回列表元素最小值
list(seq)   将元组转换为列表
方法
list.append(obj)    在列表末尾添加新的对象
list.count(obj) 统计某个元素在列表中出现的次数
list.extend(seq)    在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.index(obj) 从列表中找出某个值第一个匹配项的索引位置
list.insert(index, obj) 将对象插入列表
list.pop([index=-1])    移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj)    移除列表中某个值的第一个匹配项
list.reverse()  反向列表中元素
list.sort(cmp=None, key=None, reverse=False)    对原列表进行排序

参考链接：https://www.jb51.net/article/142493.htm
'''
list = ['Google', 'Runoob', 'Taobao']
list.append("www_zzidc_com") #添加元素。只能一次一个
del list[3]  #删除元素
list[1:] #从第二个元素开始截取列表

server_ips = ['10.61.1.101', '10.61.1.101', 80, '10.61.1.104', '10.61.1.105']
print (server_ips)
print (server_ips[1])
print (server_ips[2])

# split 将输入的字符串数据转换为列表 ,输入的数据转化为列表元素
new_site =input( "输入站点名称(站点之间请用空格隔开,退出输入exit)：")
list0 = new_site.split(" ")

#Python - 去除list中的空字符和None https://www.cnblogs.com/yspass/p/9434366.html
list1 = list(filter(None, list))

#列表元素去重  https://www.cnblogs.com/yunlongaimeng/p/8728647.html
list = sorted(set(list1),key=list1.index)

#列表获取 excel元素  https://www.cnblogs.com/insane-Mr-Li/p/9092619.html
import xlrd
fname = '更新站点.xlsx'#设置文件名和路径
date = xlrd.open_workbook(fname)# 打开文件
guonei = date.sheet_by_name("国内").col_values(0, start_rowx=0, end_rowx=None)