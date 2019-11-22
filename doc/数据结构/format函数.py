#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/22 0:22
# @Author : liuhuiling

'''
参考链接：https://www.runoob.com/python/att-string-format.html
'''
name='玲玲'
age = 29
print("name is : {}, age is : {}  " .format(name,age))
#结果：name is : 玲玲, age is : 29
'''print 用fromat()函数格式化'''
C = 3.023
print("转换后的温度值为：{: 2f}".format(C))
# format还能这样用 推荐
name = input("name:")
age = input('age:')
job = input('job:')
str3 = '''
    ------- hello word {0} -------
    Name:{0}
    Age:{1}
    Job:{2}
''' .format(name,age,job)
print(str3)