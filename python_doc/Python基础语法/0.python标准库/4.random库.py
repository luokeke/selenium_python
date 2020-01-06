#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/28 14:17
# @Author : liuhuiling
print()
'''
random 库是使用随机数的Python标准库
- 伪随机数：采用梅森旋转算法产生的(伪)随机序列中元素
- random库主要用户生成随机数
- 使用rendom库 ： import random
需要掌握的能力：
- 能够利用随机数种子产生“确定”伪随机数
- 能够产生随机整数
- 能够对序列类型进行随机操作

random库包含两类函数，常用的共有8个：
- 基本随机数函数：seed(),random()
- 扩展随机数函数：randint(),getrandbits(),uniform()
                  randrange(),choice(),shuffle()
            
- seed() 初始化给定的随机数种子，默认为当前系统时间
        random.seed(10)产生种子10对应的序列
- random() 生成一个[0.0,1.0)之间的随机小数
- uniform(a,b) 生成一个[a,b]之间的随机小数，16位，挺长的

- randint(a,b) 生成一个[a,b]之间的整数
- randrange(m,n,k) 生成一个[m,n)之间以k为步长的随机整数
- getrandbits(k) 生成一个k比特长的随机整数

- choice(seq) 从序列中随机选择一个元素
- shuffle(seq) 将序列seq中元素随机排列，返回打乱后的序列


'''
import random
random.seed() #种子默认为当前系统时间
random.seed(10)#种子10 ，种子只需要给一次
print(random.random()) #种子10一定产生这个小数0.5714025946899135
print(random.random()) #第二个小数：0.4288890546751146

import random
random.seed() #种子默认为当前系统时间 ，效果跟不加这一句一样
print(random.random()) #第一个小数0.4746010045755399
print(random.random()) #第二个小数：0.06541767655737263


