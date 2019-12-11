#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/9 18:19
# @Author : liuhuiling
print()
'''
集合处理方法
操作函数或方法              描述
S.add(x)                    如果x不在集合S中，将x增加到S
S.discard(x)                移除S中元素x，如果x不在集合S中，不报错
S.remove(x)                 移除S中元素x，如果x不在集合S中，产生KeyError异常
S.clear()                   移除S中所有元素
S.pop()                     随机取出S的一个元素，返回给用户并删除元素，更新S，若S为空产生KeyError异常
S.copy()                    返回集合S的一个副本
len(S)                      返回集合S的元素个数
x in S                      判断S中元素x，x在集合S中，返回True，否则返回False
x not in S                  判断S中元素x，x不在集合S中，返回True，否则返回False
set(x)                      将其他类型变量x转变为集合类型

'''
B = {'p', '2', '3', '1', 'y'}
for i in B:
    print(i,end="") #231yp
print()
B = {'p', '2', '3', '1', 'y'}
try:
    while True:
        print(B.pop(), end="")
except:
    pass
print("\n{}".format(B))

