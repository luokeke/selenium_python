#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2018/9/12 9:17
'''
程序要求：输入三个整数 a 、 b 、 c 分别作为三角形的三边长度，通过程序判定所构成的三角形的类型；
当三角形为一般三角形、等腰三角形或等边三角形时，分别作 …处理 。
'''
# my_status = random.randint(1, 100)
a = int( input("请输入:"))
b = int( input("请输入:"))
c = int( input("请输入:"))
# while a is

if (a<b+c and b<a+c and c<b+a ):
    if (a==b & b==c):
        print("等边三角形")
    elif (a==b or b==c or a==c):
        print ("等腰三角形")
    else :
        print("普通三角形")
else :
    print("不是三角形")



