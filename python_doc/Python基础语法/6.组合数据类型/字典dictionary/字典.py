#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/12 11:29
# @Author : liuhuiling
print()
'''
字典类型dict是“映射”的体现
- 键值对：键是数据索引的扩展
- 字典是键值对的集合，键值对之间无序
- 采用{}和dic()创建，键值对用冒号:分隔
- dict[key]方式既可以索引，也可以赋值
- de = {} 创建一个空的字典

值可以取任何数据类型，但键必须是唯一不可变的，如字符串，数字或元组,不能用列表。
dict = {key1 : value1, key2 : value2 }
创建字典时，如果相同键对应不同值，字典采用最后（最新）一个"键值对"。

理解“映射”
- 映射是一种键和值对的对应 / 索引和数据的对应
- 映射类型是由用户为数据定义索引的一种映射类型

应用场景：
- 表达键值对数据，进而操作它们
元素遍历
    for k in d:
        <语句块>
'''

a  ={'name':'limei',"age":2}
a["name"] ="lilei"
num = a["age"]
print(a)                #{'age': 2, 'name': 'lilei'}
print(list(a.items()))        #dict_items([('age', 2), ('name', 'lilei')])
print (a["age"])        #2
print(a.keys())         #dict_keys(['name', 'age'])
print(a.values())       #dict_values([2, 'lilei'])


de = {}
print(type(de)) #<class 'dict'>
