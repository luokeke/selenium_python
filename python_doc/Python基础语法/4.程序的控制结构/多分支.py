#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/27 17:16
# @Author : liuhuiling
print()
'''
多分支结构：
根据判断多个条件来选择不同语句块运行的一种分支结构
重点注意事项： 关注多分支条件的组合（算法设计）
-  多分支条件之间的覆盖是重要问题
-  程序可运行，但不正确，要注意多分支
-  分支结构是程序的重要框架，读程序先看分支
当你去阅读别人的时候，尤其是阅读函数内部的代码，首先要查看分支，
通过分支可以将程序分为几个不同的部分，而逐一再去向下看每部分的功能，
这样阅读代码的效率是非常高的。
if<条件1>:
    <语句块1>
elif<条件2>：
    <语句块2>

……

else：
    <语句块3>
'''

'''
根据输入成绩进行不同分数分级的问题
下面是反例，逻辑错误输入什么都是D：
- 注意多条件之间的包含关系
- 注意变量取值范围的覆盖
'''
# score = eval(input("请输入你的成绩（0-100）："))
# if  score>= 60:
#     grade = "D"
# elif score >= 70:
#     grade = 'C'
# elif score >=80:
#     grade = 'B'
# elif score >= 90:
#     grade = 'A'
# print("输入成绩属于级别{}".format(grade))

score = eval(input("请输入你的成绩（0-100）："))
if  score >= 90:
    grade = 'A'
elif  score >=80:
    grade = 'B'
elif  score >= 70:
    grade = 'C'
elif score>= 60:
    grade = "D"
else:
    grade = "E"
print("输入成绩属于级别{}".format(grade))