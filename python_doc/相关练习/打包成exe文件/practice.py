#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/6 10:05
# @Author : liuhuiling
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
