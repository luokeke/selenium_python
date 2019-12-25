#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/2 12:05
# @Author : liuhuiling
'''
七段数码管绘制时间
- 需求：用程序绘制七段数码管
- turtle绘图体系
基本思路：
- 步骤1：绘制单个数字对应的数码管
- 步骤2：获得一串数字，绘制对应的数码管
- 步骤3：获得当前系统时间，绘制对应的数码管 time.localtime() or time.gmtime()
'''
import turtle
def drawLine(draw): #绘制单段数码管
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)
def drawDigit(digit): #根据数字绘制七段数码管
    #根据用户输入数据来绘制七段数码管
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()#为绘制后续数字确定位置
    turtle.fd(20)#为绘制后续数字确定位置
def drawDate(date):# 获得要输出的数字
    for i in date:
        drawDigit(eval(i)) #通过eval()函数，将数字变为整数
def main():  #主函数，设置初始值及结束信息等
    turtle.setup(800,350,200,200) #设定画布
    turtle.penup()
    turtle.fd(-300)#设定画笔初始位置
    turtle.pensize(5)
    drawDate("20181010")#设定绘制数字
    turtle.hideturtle()
    turtle.done()
main() #调用主函数，启动整个函数的运行
