#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/27 9:47
# @Author : liuhuiling

import time
'''
文本进度条
--  采用字符串方式打印可以动态变化的文本进度条
--  进度条需要能在一行中逐渐变化
--  采用sleep()模拟一个持续的进度
'''
import time
for i in range(101):
    print("\r{:3}%".format(i),end="")
    #\r 指，在打印输出字符串之前，使光标退回到当前行的行首，构成单行刷新效果
    time.sleep(0.1)
'''
结果：从0% 会一直变动到100%

'''