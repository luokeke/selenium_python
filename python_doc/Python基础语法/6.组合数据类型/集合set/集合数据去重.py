#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/11 10:00
# @Author : liuhuiling

ls = ["p","p","y","y",123]
s = set(ls)  #利用了集合无重复元素的特点
#set(x)将其他类型变量x转变为集合类型
lt = list(s)  #[123, 'y', 'p']


'''
集合类型主要应用于：包含关系比较、数据去重

python 对数据去重的几种方法
https://www.jianshu.com/p/a239ac779f44


列表元素去重  https://www.cnblogs.com/yunlongaimeng/p/8728647.html
对列表中的元素去重并保持原顺序
https://blog.csdn.net/a1272899331/article/details/101039661
https://www.cnblogs.com/tingguoguoyo/p/10957216.html
https://blog.csdn.net/qq_41551919/article/details/83060738
https://blog.csdn.net/Jerry_1126/article/details/84677212

python中sorted方法和列表的sort方法使用详解 ： 
https://www.cnblogs.com/huchong/p/8296025.html
'''

