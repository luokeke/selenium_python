#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/21 14:12
# @Author : liuhuiling
print()

'''
元组是序列类型的一种扩展
- 元组是一种序列类型，一旦创建就不能被修改
- 使用小括号() 或 tuple()创建，元素间用逗号,分隔

元组类型继承了序列的通用操作 函数及方法
元组类型不可修改，因此没有特殊的针对元组类型的操作

序列通用操作符 6个
x in s           如果x是序列s的元素，返回True,否则返回False
x not in s       如果x是序列s的元素，返回True,否则返回True
s + t            链接两个序列s和t
s*n 或 n*s       将序列s复制n次
s[i]             索引，返回s中第i个元素，i是序列的序号，从0开始
s[i:j] s[i:j:k]  切片，返回序列s中第i到j以k为步长的元素子序列

序列通用函数及方法 5个
len(s)                  返回序列s的长度
max(s)/min(s)           返回序列s的最大/小元素，s中元素需要可比较，类型不同不可比较会报错
s.index(x)/s.index(x,i,j) 序列s从i位置开始到j位置中第一次出现元素x的位置
s.count(x)                  返回序列中x出现的总次数

'''
def function():
    return 1,2 #返回值是元组类型，tuple
a=()
print(len(a))#0
a=(0,)
print(len(a)) #1
print(a[0]) #0
a=(0)
#print(len(a))#TypeError: object of type 'int' has no len()
a = 1,2
b = (a,3,4)
print(b) #((1, 2), 3, 4)