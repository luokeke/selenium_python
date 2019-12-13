#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/21 14:04
# @Author : liuhuiling
import time
'''
列表类型：由0个或多个数据组成的 有序 序列
- 列表是一种序列类型，创建后可以随意被修改
- 列表使用[]或list()创建，元素间采用逗号,分隔
- 列表中元素类型可以不同，无长度限制

使用保留字 in 判断一个元素是否在列表中
列表和元组
进行的操作包括 索引[]，切片[m,n,k]，加 + ，乘 * ，检查成员 in

- 添加元素 list.append("www_zzidc_com") 
- 删除元素 del list[0] 
- 截取列表 list[i:] 从第i个元素开始截取列表，从0开始计数的

Python列表脚本操作符      列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。

Python表达式               	结果            	           描述
len([1, 2, 3])              3	                           长度
[1, 2, 3] + [4, 5, 6]    	[1, 2, 3, 4, 5, 6]	           组合
['Hi!'] * 4             	['Hi!', 'Hi!', 'Hi!', 'Hi!']   重复
3 in [1, 2, 3]	            True	                       元素是否存在于列表中
for x in [1, 2, 3]: print x,	1 2 3	                   迭代

Python列表函数/方法
函数
list[i] = x          替换列表list第i元素为x
list[i:j:k] =lt      用列表lt替换llist切片后所对应的元素子列表 
del list[i]          删除列表list中第i元素
del list[i:j:k]      删除列表list中第i到第j以k为步长的元素
list += lt           更新列表list，将列表lt元素增加到列表list中
list *= n            更新列表ls，其元素重复n次
cmp(list1, list2)    比较两个列表的元素
len(list)            列表元素个数
max(list)            返回列表元素最大值
min(list)            返回列表元素最小值
list(seq)            将元组转换为列表

方法
list.append(obj)    在列表末尾添加新的对象
list.extend(seq)    在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表），注意必须是可迭代对象
list.insert(i,x)    在列表的第i位置增加元素x，其她元素依次向后增加序号，注意i从0开始计数

list.pop(i)    移除列表中第i位置的元素，并且返回该元素的值（不填i默认最后一个元素）列表为空会报错，IndexError: pop from empty list
list.remove(obj)    将列表中出现的第一个元素x删除
list.clear() 删除列表中所有元素

list.index(obj) 从列表中找出某个值第一个匹配项的索引位置
list.copy() 生成一个新列表，赋值ls中所有元素
list.reverse()      将列表中元素反转，逆序

list.sort(cmp=None, key=None, reverse=False)    对原列表进行排序
list.count(obj) 统计某个元素在列表中出现的次数

在列表中如果我们使用list()/[],那么我们真正的创建了一个列表，如果使用赋值,只是重新命名，还是同一个列表
参考链接：
Python键盘输入转换为列表的实例 ： https://www.jb51.net/article/142493.htm
python列表的赋值，浅复制和深复制 ： https://www.cnblogs.com/dfc001/p/11526151.html  https://www.jianshu.com/p/148ac5ab0fef
extend()方法和append()方法的差异 ：https://www.jianshu.com/p/597b3cfbf21e
列表获取 excel元素     ：  https://www.cnblogs.com/insane-Mr-Li/p/9092619.html
Python - 去除list中的空字符和None  ： https://www.cnblogs.com/yspass/p/9434366.html
列表元素去重 ：  https://www.cnblogs.com/yunlongaimeng/p/8728647.html

对列表中的元素去重并保持原顺序
https://blog.csdn.net/a1272899331/article/details/101039661
https://www.cnblogs.com/tingguoguoyo/p/10957216.html
https://blog.csdn.net/qq_41551919/article/details/83060738
https://blog.csdn.net/Jerry_1126/article/details/84677212
'''
l = ['Google', 'Runoob', 'Taobao']
l.append("www_zzidc_com") #添加元素。只能一次一个
del l[3]  #删除元素
l[1:] #从第二个元素开始截取列表

lt = [1,2,3]
ls = lt
lm = lt.copy()
print(id(lt),id(ls),id(lm)) #30366776 30366776 30367256

# server_ips = ['10.61.1.101', '10.61.1.101', 80, '10.61.1.104', '10.61.1.105']
# print (server_ips,server_ips[1],server_ips[2])
# #['10.61.1.101', '10.61.1.101', 80, '10.61.1.104', '10.61.1.105'] 10.61.1.101 80

#split 将输入的字符串数据转换为列表 ,输入的数据转化为列表元素
#new_site =input( "输入站点名称(站点之间请用空格隔开,退出输入exit)：")
new_site = "www_zzidc_com     www_kuaiyun_cn   www_kuaiyun_cn   "
list0 = new_site.split(" ")
print(list0) #['www_zzidc_com', '', '', '', '', 'www_kuaiyun_cn', '', '', 'www_kuaiyun_cn', '', '', '']
# Python - 去除list中的空字符和None https://www.cnblogs.com/yspass/p/9434366.html
list1 = list(filter(None, list0))
print(list1) #['www_zzidc_com', 'www_kuaiyun_cn', 'www_kuaiyun_cn']
# 列表元素去重  https://www.cnblogs.com/yunlongaimeng/p/8728647.html
list = sorted(set(list1),key=list1.index)
print(list) #['www_zzidc_com', 'www_kuaiyun_cn']
# 列表获取 excel元素   https://www.cnblogs.com/insane-Mr-Li/p/9092619.html
# import xlrd
# fname = '更新站点.xlsx'#设置文件名和路径
# date = xlrd.open_workbook(fname)# 打开文件
# guonei = date.sheet_by_name("国内").col_values(0, start_rowx=0, end_rowx=None)


