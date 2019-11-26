#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/22 17:45
# @Author : liuhuiling

'''
基本问题：持续的价值
一年356天，每天进步1%，累计进步多少呢？
一年365天，每天退步1%，累计剩下多少呢？
三天打鱼两天晒网呢？
双休日又不退步
'''
dayup = pow(1.001,365)
daydown = pow(0.999,365)
print("天天向上：{:.2f}，天天向下：{:.2f}".format(dayup,daydown))
#天天向上：1.44，天天向下：0.69