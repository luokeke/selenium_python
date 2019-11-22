#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -*- coding: utf-8 -*-
# @Time : 2019/11/19 13:54
# @Author : liuhuiling

# 将要被测试的类
class Widget:
    def __init__(self, size = (40,40)):
        self._size = size
    def getSize(self):
        return self._size
    def resize(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("illegal size")
        self._size = (width, height)
    def dispose(self):
        pass