#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/27 15:19
# @Author : liuhuiling
import turtle
from turtle import  *
'''turtle库的使用,python标准库，无需再次安装'''
'''
turtle.setup(width,height,startx,starty)  
    width,height窗体宽高;startx,starty窗体在屏幕中位置
    turtle.setup(800,400,0,0)    窗体出现在屏幕左上方
    turtle.setup(800,400)    窗体出现在屏幕中间

turtle.goto(100,100)#goto去到达某个位置
turtle.fd(100)#像海龟的正前方运行
turtle.bk(100)#像海龟的正后方运行

turtle.circle(r,angle) #以海龟当前位置左侧某一个点为圆心，r为半径，做angle的曲线运行

turtle.seth(angle) angle 为绝对度数 改变运行方向。
turtle.left(angle) 
turtle.right(angle) 

RGB色彩体系 0-255  0-1小数值标识
turtle.colormode(mode) 颜色
颜色填充函数
-设定填充色：fillecolor(r, g, b) 
-开始填充：begin_fill() 
-结束填充：end_fill()

更多参考：
https://www.cnblogs.com/yudanqu/p/8683794.html
https://blog.csdn.net/Galaxy__42/article/details/80764648
Turtle库颜色填充：
https://blog.csdn.net/zhengzuotian/article/details/79946226
'''

import turtle as t
t.title("画个太阳")
t.setup(800,600,100,100)
t.pensize(5)
t.color("red")
t.pencolor("red")
t.begin_fill()
t.fillcolor("red")
t.circle(100)
t.end_fill()
t.hideturtle()
t.done()