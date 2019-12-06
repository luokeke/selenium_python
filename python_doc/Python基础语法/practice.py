#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/6 10:05
# @Author : liuhuiling

#绘制同心圆

import turtle
turtle.pencolor("yellow")
turtle.circle(100)
turtle.penup()
turtle.seth(-90)
turtle.fd(100)
turtle.seth(0)
turtle.pendown()
turtle.pencolor("blue")
turtle.circle(200)