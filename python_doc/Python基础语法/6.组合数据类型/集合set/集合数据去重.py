#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/11 10:00
# @Author : liuhuiling

ls = ["p","p","y","y",123]
s = set(ls)  #利用了集合无重复元素的特点
#set(x)将其他类型变量x转变为集合类型
lt = list(s)  #[123, 'y', 'p']


'''
python 对数据去重的几种方法
https://www.jianshu.com/p/a239ac779f44

对列表中的元素去重并保持原顺序
https://blog.csdn.net/a1272899331/article/details/101039661
'''

