#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/6 10:05
# @Author : liuhuiling

def prime(mun):
    for j in range(2, mun + 1):
        if mun % j == 0 and mun != j:
            break
    else:
        return True

n = eval(input())
m = int(n)
m = m +1 if m <n else m
mm =  ""
count = 5
while count > 5:
    if prime(m) is True:
        list.append(m)
    count
    m += 1
for i in list:
    mm = mm +","+str(i)
print(mm[1:])



