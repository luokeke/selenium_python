#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/27 15:19
# @Author : liuhuiling

'''turtle库的使用,python标准库，无需再次安装'''
import turtle
from turtle import  *
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

'''