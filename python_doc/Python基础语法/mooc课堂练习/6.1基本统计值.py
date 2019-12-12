#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/12 10:39
# @Author : liuhuiling
'''
基本统计值
-总个数：len()
- 求和：for … in
- 平均值：求和/总个数
- 方差：各数据与平均差的平方和的平均数
- 中位数：排序，奇数找中间1个，偶数找中间2个取平均
'''
#循环获得用户不定长输入
def getNum():
    nums = []
    iNumStr = input("请输入数字(回车退出)：")
    while iNumStr !="":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字(回车退出)：")
    return nums
#计算平均值
def mean(numbers):
    s = 0.0
    for num in numbers:
        s = s +num
    return s / len(numbers)
#计算方差
def dev(numbers,mean):
    sdev  = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev / (len(numbers)-1),0.5)
#计算中位数
def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1] + numbers[size // 2])/2
    else:
        med = numbers[size//2]
    return med
n = getNum()
m = mean(n)
print("平均值：{}，方差：{:.2},中位数：{}。".format(m,dev(n,m),median(n)))