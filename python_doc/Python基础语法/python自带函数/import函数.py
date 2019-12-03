#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/20 18:20
# @Author : liuhuiling
print("import函数")
'''
import引用方式
1.通过import关键字调用time模块
2.对导入的模块重命名   /  对导入的函数重命名
3.直接导入time模块下多个函数
4.导入time模块下所有函数 不推荐
'''

import time # 导入time模块
time.sleep(3)  #模块名.函数名
time.time()

import time as t# 导入time模块，重命名为t
t.sleep(3)
t.time()

from time import sleep as time_sleep # 导入sleep函数，重命名为time_sleep
time_sleep(2)

from time import sleep, time # 导入time模块中的sleep, time函数
sleep(3)
time()#返回当前时间

from time import * # 导入time模块中的所有函数
sleep(3)
time()

'''
import module_name

引用模块中函数的语法如下：
module_name.function_name

如果在Python程序中大量使用模块中的某些函数，那么每次在调用函数时都要加上“模块名”显得有些麻烦，
所以在这种情况下，可以使用from…import…语句将模块中的函数直接暴露出来。该语句的语法结构如下：

from module_name import function_name

如果要想导入模块中的所有函数，可以将function_name替换成型号（*），这样我们就可以直接使用该模块中的所有函数了。

from module_name import *
'''



