#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2018/2/26 16:54 

import turtle

def drawSnake(rad, angle, len, neckrad):
    for i in range(len):
        turtle.circle(rad, angle)  #rad圆形轨迹半径，正表左侧，负表右侧
        turtle.circle(-rad, angle)  #angle 弧度值
    turtle.circle(rad, angle/2)
    turtle.fd(rad)  #turtle.forward()函数，参数表示爬行距离
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300, 1800, 0, 0)  #启动窗口宽度和高度及左上角在屏幕上坐标位置
    pythonsize = 10  #运行轨迹宽度
    turtle.pensize(pythonsize)
    # turtle.pencolor("yellow") #运行轨迹颜色，RGB方式定义颜色，可以用颜色 #2CBAD2
    turtle.pencolor("#30D3F6")
    turtle.seth(-40) #初始运行轨迹方向角度值,0表示向东，90度向北，180度向西，270度向南；负值表示相反方向。 向东南方向40度
    drawSnake(40,80,5,pythonsize/2)

main()