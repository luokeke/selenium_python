#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/12 11:20
# @Author : liuhuiling
# 列表转换为字段
i = ['a','b']
l = [1,2]
print( dict([i,l]))
#字典转换为列表
count = {"age":12,"name":"lilei"}
li = list(count.items())
# list1 = list(count) #这种形式不对，会报错
print(count) #{'name': 'lilei', 'age': 12}
print(count.items()) #dict_items([('name', 'lilei'), ('age', 12)])

#输入字符串转换为列表
m = "1,2,3,4,5"
n = eval(m) #(1,2,3,4,5) 变为元组了
# print(list(eval(m))) #[1, 2, 3, 4, 5]
print(list(m)) #['1', ',', '2', ',', '3', ',', '4', ',', '5']
print(m.split(","))#['1', '2', '3', '4', '5']
print(m.split()) #['1,2,3,4,5']