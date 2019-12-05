#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/4 9:45
# @Author : liuhuiling
'''
随机密码生成 描述
补充编程模板中代码，完成如下功能：‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬
以整数17为随机数种子，获取用户输入整数N为长度，产生3个长度为N位的密码，密码的每位是一个数字。每个密码单独一行输出。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬
产生密码采用random.randint()函数。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬

输入输出示例           	输入	 输出
示例 1	                3       634
                                524
                                926
'''
import random
#我的答案，支持输入0
def genpwd(length):
    if length == 0:
        return random.randint(0,0)
    else:
        return random.randint(pow(10,length-1),(pow(10,length)-1))
length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))

#参考答案，输入0会报错
def genpwd(length):
    a = 10**(length-1)
    b = 10**length - 1
    print(a,b)
    return "{}".format(random.randint(a, b))

length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))

