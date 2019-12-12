#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/12 11:29
# @Author : liuhuiling

a  ={'name':'limei',"age":2}
a["name"] ="lilei"
num = a["age"]
print(a)                #{'age': 2, 'name': 'lilei'}
print(list(a.items()))        #dict_items([('age', 2), ('name', 'lilei')])
print (a["age"])        #2
print(a.keys())         #dict_keys(['name', 'age'])
print(a.values())       #dict_values([2, 'lilei'])
'''
字典类型是“映射”的提现
- 键值对：键是数据索引的扩展
- 字典是键值对的集合，键值对之间无序
- 采用{}和dic()创建，键值对用冒号:表示
- de = {} 创建一个空的字典
理解“映射”
- 映射是一种键和值对的对应 / 索引和数据的对应
- 映射类型是由用户为数据定义索引的一种映射类型

'''

de = {}
print(type(de)) #<class 'dict'>