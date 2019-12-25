#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/24 16:18
# @Author : liuhuiling
#打印输出附件文件的有效行数，注意：空行不计算为有效行数。
f = open("latex.log","r",encoding="utf-8")
ls = f.readlines()
li = 0
for i in ls:
    if i !="\n":
        li += 1
f.close()
print("共{}行".format(li))

f = open("latex.log")
s = 0
for line in f:
    line = line.strip('\n')
    if len(line) == 0:
        continue
    s += 1
print("共{}行".format(s))