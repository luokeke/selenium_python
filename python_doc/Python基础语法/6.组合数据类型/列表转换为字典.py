#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/12 11:20
# @Author : liuhuiling
print()
'''列表转换为字段'''
i = ['a','b']
l = [1,2]
print( dict([i,l]))

'''字典转换为列表'''
count = {"age":12,"name":"lilei"}
li = list(count.items())
# list1 = list(count) #这种形式不对，会报错
print(count) #{'name': 'lilei', 'age': 12}
print(count.items()) #dict_items([('name', 'lilei'), ('age', 12)])

'''输入字符串转换为列表'''
m = "1,2,3,4,5"
n = eval(m) #(1,2,3,4,5) 变为元组了
# print(list(eval(m))) #[1, 2, 3, 4, 5]
print(list(m)) #['1', ',', '2', ',', '3', ',', '4', ',', '5']
print(m.split(","))#['1', '2', '3', '4', '5']
print(m.split()) #['1,2,3,4,5']

'''
int(x)          --将x变成整数，舍弃小数部分
float(x)        --将x变成浮点数，增加小数部分
complex(x)      --将x变成复数，增加小数部分

str(x)          -- 任意类型x所对应的字符串形式；任意类型x增加引号，使它变为字符串，
set(x)          -- 将其他类型变量x转变为集合类型，也用于设置空集合set();x是可迭代的对象，元组/字符串/列表/字典
list(seq)       -- 将元组转换为列表
tuple(seq)      -- 将列表转换为元组。
dict([seq,seq]) -- 将列表，元组转换为字典
eval(str)       -- 将字符串变为元组类型
'''