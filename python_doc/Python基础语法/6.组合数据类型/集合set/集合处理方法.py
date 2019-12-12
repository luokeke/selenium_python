#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/9 18:19
# @Author : liuhuiling
print()
'''
集合处理方法
操作函数或方法 描述
set(x)         将其他类型变量x转变为集合类型，也用于设置空集合set();x是可迭代的对象，元组/字符串/列表/字典
len(S)         返回集合S的元素个数
x in S         判断S中元素x，x在集合S中，返回True，否则返回False
x not in S     判断S中元素x，x不在集合S中，返回True，否则返回False

S.add(x)       如果x不在集合S中，将x增加到S

S.discard(x)   移除S中元素x，如果x不在集合S中，不报错
S.remove(x)    移除S中元素x，如果x不在集合S中，产生KeyError:x异常
S.pop()        随机取出S的一个元素，返回给用户并删除元素，更新S，若S为空产生KeyError: 'pop from an empty set'异常
               不同于list.pop(i)，集合无序不能给定索引值，S.pop()默认给定参数，填值会报错TypeError: pop() takes no arguments (1 given) 
S.clear()      移除S中所有元素
S.copy()       返回集合S的一个副本

集合类型主要应用于：包含关系比较、数据去重

'''
B = {'p', '2', '3', '1', 'y'}
for i in B:
    print(i,end="") #231yp
print()
B = {'p', '2', '3', '1', 'y'}
try:
    while True:
        print(B.pop(), end="") #32yp1
except:
    pass
print("\n{}".format(B))  # B是一个空集合set()
print(type(B)) #<class 'set'>


s = {"name":"lie","age":12}
print(set(s.items())) #{('age', 12), ('name', 'lie')}
print(set(s)) #{'name', 'age'}
print(set(s.keys())) # {'name', 'age'}
print(set(s.values())) #{'lie', 12}

s = [1,2,3,4,5]
print(set(s))#{1, 2, 3, 4, 5}
s = (1,2,3,4)
print(set(s)) #{1, 2, 3, 4}

s = 123
# print(set(s)) #TypeError: 'int' object is not iterable
s = 123.4
print(set(s)) #TypeError: 'float' object is not iterable