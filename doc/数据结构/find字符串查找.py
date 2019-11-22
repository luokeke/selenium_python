#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
'''
python 字符串查找有4个方法，1 find,2 index方法，3 rfind方法,4 rindex方法。
find()方法：查找子字符串，若找到返回从0开始的下标值，若找不到返回-1
index方法：查找子串第一次出现的位置，类似字符串的find方法，如果查找不到子串，抛出异常
rfind方法
rindex方法
'''
# 1 find()方法
info = 'abca'
print (info.find('abc'))##从下标0开始，查找在字符串里第一个出现的子串，返回结果：0
info = 'abca'
print (info.find('a',1))##从下标1开始，查找在字符串里第一个出现的子串：返回结果3 (下标3)
info = 'abca'
print (info.find('333'))##返回-1,查找不到返回-1
# 2 index()方法：
info = 'abca'
print(info.index('a'))
print(info.index('333'))
# rfind和rindex方法用法和上面一样，只是从字符串的末尾开始查找。
# rfind和rindex方法用法和上面一样，只是从字符串的末尾开始查找。

