#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/26 13:40
# @Author : liuhuiling
print("{0:=^20}".format("PYTHON"))#结果  =======PYTHON=======

print("{0:=^20}".format("PYTHON0"))  #结果  ======PYTHON0=======
# :=^20，= 填充符号，^居中对齐，20输出宽度

print("{0:*<20}".format("PYTHON"))# PYTHON**************
print("{0:*^9}".format("PYTHON"))