#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/22 0:22
# @Author : liuhuiling

name='玲玲'
age = 29
print("name is : {}, age is : {}  " .format(name,age))  #结果：name is : 玲玲, age is : 29
C = 3.023
print("转换后的温度值为：{: 2f}".format(C)) #结果：转换后的温度值为： 3.023000

'''
参考链接：https://www.runoob.com/python/att-string-format.html
print 用fromat()函数格式化
{} 为槽，占位符
-- :    引导符号
-- 填充   用于填充的单个字符
-- 对齐   左对齐<  右对齐>  居中对齐^
-- 宽度   槽设定的输出宽度
-- , 数字的千位分隔符
-- .精度 浮点数小数精度或字符串最大输出长度 
-- 类型 整数类型 b,c,d,o,x,X  浮点数类型 e,E,f,%
'''
print("{0:=^20}".format("PYTHON"))  #结果  =======PYTHON=======
# :=^20，= 填充符号，^居中对齐，20输出宽度
'''format还能这样用 推荐'''
name = '玲玲'
age = 29
job = "面包师"
str3 = '''
    ------- hello word {0} -------
    Name:{0}
    Age:{1}
    Job:{2}
'''.format(name,age,job)
print(str3)
'''
结果：
------- hello word 玲玲 -------
    Name:玲玲
    Age:29
    Job:面包师
'''