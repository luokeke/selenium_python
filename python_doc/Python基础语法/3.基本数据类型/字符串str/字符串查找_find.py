#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
'''
https://www.cnblogs.com/johnson-yuan/p/7910087.html
python 字符串查找有4个方法，
1 str.find()    --查找子串，若找到返回第一次出现位置的索引值，若找不到返回-1
2 str.index()   --查找子串第一次出现位置的索引值，类似字符串的find方法，如果查找不到子串，抛出异常
3 str.rfind()   --和str.find()用法一样，只是从字符串的末尾开始查找。
4 str.rindex()  --和str.index()用法一样，只是从字符串的末尾开始查找。
'''
# 1 find()方法
info = 'abca'
print (info.find('abc'))##从下标0开始，查找在字符串里第一个出现的子串，返回结果：0
info = 'abca'
print (info.find('a',1))##从下标1开始，查找在字符串里第一个出现的子串：返回结果3 (下标3)
info = 'abca'
print (info.find('333'))##返回-1,查找不到返回-1
# 2 index()方法：
inf = 'abca'
print(inf.index('c'))# 返回2
# print(inf.index('333')) # 报错 ValueError 因为 333不是字符串abca中的元素

# # rfind和rindex方法用法和上面一样，只是从字符串的末尾开始查找。
str = "123a456dadsbca"
print(len(str))  #14
print(str.rfind("a")) # 13
print(str.rfind("7")) # -1
print(str.rindex("a")) # 1
# print(str.rindex("7")) # 报错ValueError: substring not found