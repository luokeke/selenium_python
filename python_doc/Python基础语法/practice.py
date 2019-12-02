#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/28 18:50
# @Author : liuhuiling
import turtle as t
import time

def drawgap(ft):
    t.penup()
    t.fd(0.11*ft)

def drawline(e,ft):
    drawgap(ft)
    t.pendown() if e else t.penup()
    t.fd(0.78*ft)
    drawgap(ft)
    t.right(90)

def drawdigit(digit,ft):
    drawline(True,ft) if eval(digit) in [2,3,4,5,6,8,9] else drawline(False,ft)
    drawline(True, ft) if eval(digit) in [0,1,3,4,5,6,7,8,9] else drawline(False, ft)
    drawline(True, ft) if eval(digit) in [0,2,3,5,6,8,9] else drawline(False, ft)
    drawline(True, ft) if eval(digit) in [0,2,6,8] else drawline(False, ft)
    t.left(90)
    drawline(True, ft) if eval(digit) in [0,4,5,6,8,9] else drawline(False, ft)
    drawline(True, ft) if eval(digit) in [0,2,3,5,6,7,8,9] else drawline(False, ft)
    drawline(True, ft) if eval(digit) in [0,1,2,3,4,7,8,9] else drawline(False, ft)
    t.right(180)
    t.fd(-ft)

def drawempty(ft):
    t.pendown()
    for j in range(4):
        t.fd(ft)
        t.right(90)
    t.left(90)
    for k in range(3):
        t.fd(ft)
        t.right(90)
    t.right(180)
    t.fd(-ft)

ft=100

t.pencolor('red')
t.pensize(0.12*ft)
t.setup(1000,450)

countnum=3
numstr=(['']*countnum)
for i in range(countnum):
    numstr[i]=str(countnum-i)
dur=(['']*countnum)
i=-1
t.speed(99*99)
#校正数字显示位置
t.penup()
t.fd(-0.5*ft)

#开始计时
for each in numstr:
    starte=time.perf_counter()
    drawdigit(each,ft)
    t.clear()
    i+=1
    dur[i]=time.perf_counter()-starte
    time.sleep(1-dur[i])

#校正直接打印数字的位置
t.right(90)
t.fd(ft)
t.left(90)
j=-1
for each in numstr:
    start=time.perf_counter()
    j+=1
    t.write(countnum-j,font=('Arial',ft,'normal'))
    time.sleep(0.7)
    t.clear()
    dur=time.perf_counter()-start
    time.sleep(1-dur)

#打印计时结束的提示信息
t.penup()
t.fd(-ft*2)
t.pencolor('green')
for i in range(5):
    t.clear()
    time.sleep(0.3)
    t.write('倒计时结束',font=('SimHei',int(ft*0.8),'italic'))
    time.sleep(0.4)
t.done()