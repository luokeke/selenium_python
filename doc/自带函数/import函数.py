#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/20 18:20
# @Author : liuhuiling
'''import引用方式'''

# 导入time模块
import time
time.sleep(3)
time.time()

# 导入time模块，重命名为t
import time as t
t.sleep(3)
t.time()

# 导入time模块中的sleep, time函数
from time import sleep, time
sleep(3)
time()#返回当前时间

# 导入time模块中的所有函数
from time import *
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



