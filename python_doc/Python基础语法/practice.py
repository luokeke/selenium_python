#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/6 10:05
# @Author : liuhuiling
#输入字符串转换为列表
m = "1,2,3,4,5"
n = eval(m) #(1,2,3,4,5) 变为元组了
print(list(eval(m))) #[1, 2, 3, 4, 5]
print(list(m)) #['1', ',', '2', ',', '3', ',', '4', ',', '5']
print(m.split(","))#['1', '2', '3', '4', '5']
print(m.split()) #['1,2,3,4,5']