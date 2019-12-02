#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/28 13:48
# @Author : liuhuiling
print()
'''
循环与else的高级用法: 与break有关
- 当循环没有被break语句退出时，执行else语句块
- else 语句块作为“正常”完成循环的奖励
- 这里else的用法与异常处理中else用法相似 参考：异常处理的高级使用
for <循环变量> in <遍历结构> :
    <语句块1>
else:
    <语句块2>

while <条件> :
    <语句块1>
else:
    <语句块2>

'''
#因没有break else语句会被执行
for c in "PYTHON":
    if c == "T":
        continue
    print(c,end="")
else:
    print("正常退出") #结果 ：PYHON正常退出
#因有break else语句不会会被执行
for c in "PYTHON":
    if c == "T":
        break
    print(c,end="")
else:
    print("正常退出") #结果 ：PY