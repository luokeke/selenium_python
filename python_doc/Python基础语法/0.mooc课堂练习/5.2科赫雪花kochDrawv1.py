#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/3 14:32
# @Author : liuhuiling
'''
科赫雪花，也叫雪花曲线
用同一个操作来对其中的曲线或直线进行不断迭代，就构成了科赫曲线的实现过程

绘制n阶科赫曲线线段
- 递归思想：函数+分支
- 递归链条：线段的组合
- 递归基例：初始线段

举一反三：
- 康托尔集、谢尔宾斯基三角形、门格海绵…
- 龙形曲线、空间填充曲线、科赫曲线…
'''
import turtle
from time import sleep
def koch(size,n):
    if n == 0:
        turtle.fd(size)
    else:
        for angele in [0,60,-120,60]:#转角度需要想一下
            turtle.left(angele)
            koch(size/3,n-1)
def main():
    turtle.setup(600,600)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(2)
    level = 3  #3阶科赫雪花
    koch(400,level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.hideturtle() #将画笔隐藏
    sleep(5) #五秒后画布关闭
    # turtle.done() #画布不关闭

main()#调用主函数，启动整个函数的运行
