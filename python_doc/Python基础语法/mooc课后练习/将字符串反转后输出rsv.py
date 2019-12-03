#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/3 12:43
# @Author : liuhuiling

#将字符串s反转后输出 s[::-1]
def rvs(s):
    if s == "":
        return s
    else:
        return rvs(s[1:])+s[0]
print(rvs("123456789"))