#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/21 22:27
# @Author : liuhuiling

class A:
    def __int__(self,a,b):
        self.a = int(a)
        self.b = int(b)
    def add(self):
        return self.a+self.b
count = A('4',5)
print(count.add)
