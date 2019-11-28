#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/28 18:50
# @Author : liuhuiling
s = ""
for i in range(100,1000):
    J = str(i)
    G =eval(J[-1])
    S =eval(J[1])
    B =eval(J[0])
    sum =  pow(G,3)+ pow(S,3) + pow(B,3)
    if i == sum :
        s += "{},".format(i)
print(s[:-1])