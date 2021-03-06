#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/26 15:42
# @Author : liuhuiling
str="abcABC"
str.replace("ABC","nihao")

'''
方法在编程中是面向对象的一个专有名词
-- 方法特指<a>.<b>()风格中的函数<b>()
-- 方法本身也是函数，但与<a>有关，<a>.<b>()风格使用
-- 字符串及变量也是 <a> ，存在一些方法
<a>.<b>() 面向对象的风格

str.lower() 将字符转换为小写，返回字符串的副本，全部字符小写。
str.upper() 将字符转换为大写，返回字符串的副本，全部字符大写。
str.split(sep=None) 返回一个列表，由str根据sep被分隔的部分组成;分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
str.replace(old,new) 返回字符串的副本，所有old子串被替换为new
str.center(width[,fillchar]) 字符串str根据宽度width居中，如果需要的话，就用fillchar进行填充，默认是空格。
str.strip(chars) 从str中去掉在其左侧和右侧chars中列出的字符
str.join(iter) 在iter变量除最后元素外每个元素后增加一个str, 类似均匀插入分隔符  
        print(','.join("abcABC")) #a,b,c,A,B,C iter可以是列表、元组
fromat()函数格式化
str.index(obj) 从字符串str中找出某个值第一个匹配项的索引位置 #obj非字符串元素时会报错 ValueError: substring not found

Python split()方法分割字符串 ： https://www.cnblogs.com/jsdd/p/11613121.html
'''
str="abcABC"
str1="a,b,c"
str2 = 'a b c'
str3 = '+abcdefab+'
str4= ','
print(str.lower()) #abcabc
print(str.upper())#ABCABC
print(str.replace("ABC","nihao")) #abcnihao
print(str3.strip("ab+") ) #cdef
print(",".join(str)) #a,b,c,A,B,C
print(str4.join(str)) #a,b,c,A,B,C
print(','.join("abcABC")) #a,b,c,A,B,C

print(str.split(sep=None))#['abcABC']
print(str.split())#['abcABC']
print(str1.split(sep=","))#['a', 'b', 'c'] 以，为分隔符，把字符串转换为列表
print(str2.split( ))# ['a', 'b', 'c']  以空格为分隔符，把字符串转换为列表
print(str2.split(sep=" "))# ['a', 'b', 'c']  以空格为分隔符，把字符串转换为列表   和上面等同

print(" ".join(["中国","美国","日本"])) #中国 美国 日本
print(type(" ".join(["中国","美国","日本"]))) #<class 'str'>