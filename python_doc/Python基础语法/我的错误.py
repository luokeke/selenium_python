#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/6 10:58
# @Author : liuhuiling
print()

'''
货币转换.py
我犯的错误：
1.print("{:.2f}".format(23.02))    {:.2f}少:,不加"",format() 里不填值
2.rmb和usd转换弄反，usd = rmb / 6.78 我弄成*  rmb = usd* 6.78 我弄成/
3.表示金钱数据是 m[3::]   我写成m[4::]
'''