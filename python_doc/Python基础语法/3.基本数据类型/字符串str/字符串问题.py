#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/6 10:26
# @Author : liuhuiling
import time
#这两种格式都是输出除最后一位的字符串，m[0:-1]效率更高
m  = "1231"
start = time.perf_counter()
time.sleep(1)
print(m[0:-1])
print(time.perf_counter()-start)

start0 = time.perf_counter()
time.sleep(1)
print(m[0:len(m)-1])
print(time.perf_counter()-start0)
