#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/3 14:11
# @Author : liuhuiling
'''
基本思路：
- 步骤1：绘制单个数字对应的数码管
- 步骤2：获得一串数字，绘制对应的数码管
- 步骤3：获得当前系统时间，绘制对应的数码管
    使用time库获得系统当前时间 time.localtime() or time.gmtime()
    增加年月日标记
    年月日颜色不同
应用问题的扩展
- 绘制带小数点的七段数码管
- 带刷新的时间倒计时效果
- 绘制高级的数码管
'''
import turtle
from time import gmtime,strftime
def drawGap(): #绘制间隔
    turtle.penup()
    turtle.fd(5)
def drawLine(draw): #绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawDigit(digit): #根据数字绘制七段数码管
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):# date为日期，格式未'%Y-%m=%d+'获得要输出的数字  -年 =月 +日
    for i in date:
        if i == '-':
            turtle.write('年',font=("Arial",18,"normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font=("Arial",18,"normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write("日",font=("Arial",18,"normal"))
        else:
            drawDigit(eval(i))
def main():  #主函数，设置初始值及结束信息等
    turtle.setup(850,350,200,200) #设定画布
    turtle.penup()
    turtle.speed(100)
    turtle.fd(-330)#设定画笔初始位置
    turtle.pensize(5)
    # drawDate("20200101")#设定绘制数字
    drawDate(strftime("%Y-%m=%d+", gmtime()))#设定绘制数字
    turtle.hideturtle()
    turtle.done()
main() #调用主函数，启动整个函数的运行