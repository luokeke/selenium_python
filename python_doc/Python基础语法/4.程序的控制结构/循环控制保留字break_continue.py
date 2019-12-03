#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/28 13:52
# @Author : liuhuiling
print()
'''
break 和 continue
- break 跳出并结束当前整个循环，执行循环后的语句
- continue 结束当次循环，继续执行后续次数循环
- break 和 continue  可以与for和while循环搭配使用


'''
#  continue  遍历字符串，出现T结束当次循环print不执行，
for c in "PYTHON":
    if c== "T":
        continue  #当次循环结束，不会打印T
    print(c,end="") #结果：PYHON
print("\n")
#   break  遍历字符串，到字母T时break，结束整个循环
for c in "PYTHON":
    if c== "T":
        break  #循环结束，后续不会打印
    print(c,end="") #结果：PY
print("\n")
#多层循环
s = "PYTHON"
while s != "":
    for c in  s:
        print(c,end="")
    s = s[:-1] #结果：PYTHONPYTHOPYTHPYTPYP
print("\n")
s = "PYTHON"
while s != "":
    for c in  s:
        if c == "T":
            break #仅跳出当前最内层循环
        print(c,end="")
    s = s[:-1] #结果：PYPYPYPYPYP


