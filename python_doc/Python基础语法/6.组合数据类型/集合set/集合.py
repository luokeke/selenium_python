#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/09 17:51
# @Author : liuhuiling
print()
'''
集合：是多个元素的  无序  组合
- 用{}大括号表示，元素间用逗号分隔
- 建立集合类型用{}或set{}
- 建立空集合类型，必须使用set() b={}建立的是字典类型

- 集合类型和数学中的集合概念一致
- 集合元素之间无序，每个元素唯一，不存在相同元素
- 集合元素不可更改，不能是可变数据类型

非可变数据类型：整数、浮点数、负数、字符串类型、元组类型
可变数据类型：列表 、字典  报错：TypeError

'''
A = {"python",123,("python",123)}
B = set("pypy123")
#{'3', 'p', '1', '2', 'y'} 相同元素会被去掉
C = {"python",123,"python",123} # {"python",123}相同元素会被去掉

# jihe = {[1],[2]}  #TypeError: unhashable type: 'list'
# jihe = {(1,2),{"age":12}} #TypeError: unhashable type: 'dict'
