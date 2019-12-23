#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/23 14:19
# @Author : liuhuiling
a = "1,2"
print(a.split(","))
print(list(map(eval,a.split(","))))
'''
自动轨迹绘制
步骤一：定义数据文件个数（接口）
步骤二：编写程序，根据文件接口解析参数绘制图形
步骤三：编制数据文件

数据接口定义：
    用一行表示一次操作
    一行六个数据，逗号分隔
    分别为：行进距离，转向判断，转向角度，RGB三个通道颜色（0-1之间浮点数）
    184,0,72,1,0,1
'''
import turtle as t
t.title("自动轨迹绘制")
t.setup(800,600,0,0)
t.pensize(5)
t.pencolor("red")
#数据读取
datals = []
f = open("drawdata.txt")
for line in f :
    line = line.replace("\n","")
    datals.append(list(map(eval,line.split(","))))
f.close()
print(datals)
#自动轨迹绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
