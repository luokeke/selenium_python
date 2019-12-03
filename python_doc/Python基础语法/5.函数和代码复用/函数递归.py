#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/3 9:50
# @Author : liuhuiling
'''
函数递归的理解：调用函数自身的方式就是递归
        数学中也广泛存在n!
两个关键特征：
- 链条：计算过程存在递归链条，递归有序的链条关系
- 基例：存在一个或多个不需要再次递归的基例
        基例，基础的实例 0!=1，与其它值不存在递归关系，是递归的最末端


阶乘亦可以递归方式定义：0!=1，n!=(n-1)!×n。

类似数学归纳法
- 数学归纳法
- 证明当n取第一个值n0时命题成立
- 假设当nk时命题成立，证明n(k+1)时命题也成立
- 递归是数学归纳法思维的编程提现

函数 + 分支语句
- 递归本身是一个函数，需要函数定义方式描述
- 函数内部，采用分支语句对输入参数进行判断
-基例和链条，分别编写对应代码
递归过程只关心递归链条，举例汉诺塔问题，你不可能搞清楚搬运的全过程
只需要搞清楚n和n-1之间的关系

'''
#    n!    0!=1，n!=(n-1)!×n。
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

#将字符串s反转后输出 s[::-1]
def rvs(s):
    if s == "":
        return s
    else:
        return rvs(s[1:])+s[0]
print(rvs("123456789"))

'''
斐波那契数列
F(1)=1，F(2)=1,
F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）
'''
def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1)+f(n-2)
#汉诺塔问题

count = 0
def haoni(n,src,dst,mid): # n圆盘数量，src源柱子，dst目标柱子，mid过渡柱子
    global count
    if n ==1 :
        print("{}:{}-->{}".format(1,src,dst))
        count +=1
    else:
        haoni(n-1,src,mid,dst)
        print("{}:{}-->{}".format(n, src, mid))
        count += 1
        haoni(n-1,mid,dst,src)
haoni(4,"A","C","B")
print(count)