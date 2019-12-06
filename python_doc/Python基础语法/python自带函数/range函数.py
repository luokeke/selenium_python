#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/20 18:07
# @Author : liuhuiling

'''range()函数，产生循环计数序列
range(n) 从0至n-1循环计数，产生0到n-1的整数序列，共n个
range(m,n) 从m至n-1循环计数，产生m到n-1的整数序列，n-m个
range(m,n,k) 从m至根据步长k，循环计数。
'''
# 两种使用方法
range(5) #表示  0  1  2  3  4
range(2,5)#表示    2  3  4
# 跟for和in搭配行程计数循环


a = [[1,2,3], [4,5,6], [7,8,9]]
for c in a:
    for j in range(3):
        print(c[j])
