#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/3 12:48
# @Author : liuhuiling
'''
相传在古印度圣庙中，有一种被称为汉诺塔(Hanoi)的游戏。该游戏是在一块铜板装置上，有三根杆(编号A、B、C)，
在A杆自下而上、由大到小按顺序放置64个金盘。
游戏的目标：把A杆上的金盘全部移到C杆上，并仍保持原有顺序叠好。
操作规则：每次只能移动一个盘子，并且在移动过程中三根杆上都始终保持大盘在下，小盘在上，操作过程中盘子可以置于A、B、C任一杆上。 [2]

分析：对于这样一个问题，任何人都不可能直接写出移动盘子的每一步，但我们可以利用下面的方法来解决。
设移动盘子数为n，为了将这n个盘子从A杆移动到C杆，可以做以下三步：
(1)以C盘为中介，从A杆将1至n-1号盘移至B杆；
(2)将A杆中剩下的第n号盘移至C杆；
(3)以A杆为中介；从B杆将1至n-1号盘移至C杆。
'''
count = 0
def haoni(n,src,dst,mid): # n圆盘数量，src源柱子，dst目标柱子，mid过渡柱子
    global count
    if n ==1 :
        print("{}:{}-->{}".format(1,src,dst))
        count +=1
    else:
        haoni(n-1,src,mid,dst)
        print("{}:{}-->{}".format(n,src,dst))
        count += 1
        haoni(n-1,mid,dst,src)
haoni(4,"A","C","B")
print(count)