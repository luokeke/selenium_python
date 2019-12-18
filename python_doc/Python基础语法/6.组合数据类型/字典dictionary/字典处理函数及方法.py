#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/12 11:34
# @Author : liuhuiling
print()
'''
字典类型操作函数和方法
del dict[k]         删除字典dict中键k对应的数据值
k in dict           判断键k是否在字典dict中，如果在返回True，否则返回False
dict.keys()         返回字典dict中所有的键信息
dict.values()       返回字典dict中所有的值信息
dict.items()        返回字典d中所有的键值对信息
dict.get(k,default) 键k存在，则返回相应值，不存在则返回默认值None  或设置的default值 （默认值）
dict.pop(k,default) 键k存在，则取出相应值并返回给用户。如果要删除的 key 不存在，则需要添加默认值，否则会报错KeyError；
dict.popitem()      随机从字典dict中取出一个键值对，以元组形式返回；给定值会报错TypeError: popitem() takes no arguments (1 given)
dict.clear()        删除所有的键值对
len(dict)           返回字典dict中元素的个数

dict.keys()/dict.values(),不返回列表类型，返回的是字典的keys和values类型
可以用for in 方式做遍历，但是不能当做列表类型来操作
'''
dict = {"中国":"北京","美国":"华盛顿","法国":"巴黎"}
print(type(dict.keys())) #<class 'dict_keys'>
print(type(dict.values())) #<class 'dict_values'>
print(dict.get("你好"))  #None
print(dict.get("你好","不存在")) #不存在
print(dict.pop("中国","不存在"))  #北京
print(dict.pop("你好","不存在")) #不存在
# print(dict.pop("你好"))  #KeyError: '你好'
dict["中国"] = "北京"
print(dict.popitem()) #('法国', '巴黎')
print(dict.popitem("法国")) #TypeError: popitem() takes no arguments (1 given)