#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/28 10:00
# @Author : liuhuiling
print()
'''
遍历循环： 遍历某个结构行成的循环运行方式
for <循环变量> in <遍历结构>：
    <语句块>
- 由保留字for和in组成，完整便利所有元素后结束
- 每次循环，从遍历结构中提取元素，所获得元素放入循环变量，并执行一次语句块
具体应用：
- 计数循环（N次）
- 计数循环（特定次）
- 字符串遍历循环
- 列表遍历循环
- 文件遍历循环
……
计数循环（N次）
for i in range(n):#0,1至 n-1
    <语句块>
- 遍历由range()函数产生的数字序列，产生循环
计数循环（特定次）
for i in range(m,n,k):#从m至n-1，步长为k
    <语句块>
- 遍历由range()函数产生的数字序列，产生循环

字符串遍历循环
for c in s:
    <语句块>
- s是字符串，遍历字符串每个字符，产生循环
- c代表字符串中每个字符
从字符串s中按顺序取出每个字符放到c中，并执行一次语句块，产生循环

列表遍历循环
for item in ls：
    <语句块>
- ls是一个列表，遍历其每个元素，产生循环

文件遍历循环
for line in fi：
    <语句块>
- fi是一个文件标识符，遍历其每行，产生循环
'''
for i in range(5):
    print(i) #计数循环（N次）
for i in range(1,6,2):
    print(i) #计数循环（特定次）
for c in ("python123"):
    print(c,end=",") #p,y,t,h,o,n,1,2,3,
#联想到字符串处理方法join：print(",".join("python123")) #p,y,t,h,o,n,1,2,3
for item in ["python","你好",12]:
    print(item,end=",") #python,你好,12,
