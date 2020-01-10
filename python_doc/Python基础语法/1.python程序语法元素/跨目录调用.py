#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/1/7 11:36
# @Author : liuhuiling
import time
'''
同目录下直接调用掉用
跨目录调用,先引用
参考链接1：https://www.cnblogs.com/cindy-cindy/p/8258450.html

https://www.cnblogs.com/tynam/p/8940721.html
'''
from test.test import add  #test和该文件目录同级
print(add())
from test.test1.test1 import add1
print(add1())

'''
如果1行不通，把文件目录假如到python的path中
参考链接2：https://www.cnblogs.com/tynam/p/8940721.html
'''
import sys
from os.path import dirname,abspath
project_path = dirname(dirname(abspath(__file__))) #获得文件所在的绝对目录
sys.path.append(project_path+"\\test\\test1") #拼接要调用模块名称，并加入到path
print(project_path+"\\test\\test1")
print(sys.path)
#开始引用
from test1 import add1
print(add1())


# print(abspath(__file__))
# print(dirname(abspath(__file__)))
# print(project_path)
# print(sys.path)





