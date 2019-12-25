#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/2 15:32
# @Author : liuhuiling
#- 绘制带刷新的时间倒计时效果
import turtle
import time
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
def drawCountDown():
    for i in [9,8,7,6,5,4,3,2,1]:
        dur =[]
        j = 0
        starte = time.perf_counter()
        drawDigit(i)
        turtle.clear()
        j =j+ 1
        dur[j] = time.perf_counter() - starte
        time.sleep(1 - dur[j])

def mian():
    start = time.perf_counter()
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-350)
    turtle.pensize(5)
    turtle.color("green")
    drawCountDown()
    turtle.hideturtle()
    turtle.done()
mian()
