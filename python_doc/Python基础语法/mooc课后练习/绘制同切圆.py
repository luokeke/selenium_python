#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/6 14:32
# @Author : liuhuiling
import turtle

turtle.pensize(2)
turtle.circle(10)
turtle.circle(20)
turtle.circle(40)
turtle.circle(80)
turtle.circle(160)
turtle.hideturtle()



#绘制同心圆

import turtle
turtle.pencolor("yellow")
turtle.circle(100)
turtle.penup()
turtle.seth(-90)
turtle.fd(200)
turtle.seth(0)
turtle.pendown()
turtle.pencolor("blue")
turtle.circle(300)
turtle.done()