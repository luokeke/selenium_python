#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/19 17:09
# @Author : liuhuiling
import turtle as t
import random as r
def randomcolor():
    color = ("red")
    return color
def pink():
    color = (1, r.random(), 1)
    return color
def randomrange(min, max):
    return min + (max- min)*r.random()
def moveto(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
def heart(r, a):
    factor = 180
    t.seth(a)
    t.circle(-r, factor)
    t.fd(2 * r)
    t.right(90)
    t.fd(2 * r)
    t.circle(-r, factor)
# set canvas dimension
t.title("~~~给你画个小心心~~~")
t.hideturtle()
t.setup(800, 800, 100, 100)
t.speed(100)
t.pensize(1)
t.pencolor(randomcolor())
t.fillcolor(randomcolor())
t.penup()
for i in range(30):
    t.goto(randomrange(-300, 300), randomrange(-300, 300))
    t.begin_fill()
    t.fillcolor(pink())
    heart(randomrange(10, 50), randomrange(0, 90))
    t.end_fill()
# moveto(400, -400)
t.done()

'''
import turtle as t
from random import *
def heart(r, a):
    factor = 180
    t.seth(a)
    t.circle(-r, factor)
    t.fd(2 * r)
    t.right(90)
    t.fd(2 * r)
    t.circle(-r, factor)
t.title("~~~给你画一颗小心心~~~")
t.setup(600,500)
t.penup()
t.goto(0,100)
t.down()
t.color("red")
t.speed(10)
t.begin_fill()
t.fillcolor("red")
heart(randint(50,100), 45)
t.end_fill()
t.hideturtle()
t.done()

'''