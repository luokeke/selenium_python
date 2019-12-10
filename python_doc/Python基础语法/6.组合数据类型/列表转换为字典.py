#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/12 11:20
# @Author : liuhuiling

# i = ['a','b']
# l = [1,2]
# print( dict([i,l]))

sum = 0
i = 5
for j in range(2, i + 1):
    if i % j == 0 and  j != i:
        print(i)
