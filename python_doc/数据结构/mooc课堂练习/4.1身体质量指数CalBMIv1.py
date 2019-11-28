#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/28 9:42
# @Author : liuhuiling
print()
'''
-- BMI:国际上常用的衡量人体肥胖和健康程度的重要指标，只要勇于统计分析
-- 定义：BMI = 体重(kg)/身高平方(㎡)
国际：世界卫生组织 国内：国家卫生健康委员会
分类      国际BMI值 (kg/m2)       国内BMI值 (kg/m2)
偏瘦      <18.5                   <18.5
正常      18.5 ~ 25               18.5 ~ 24
偏胖      25 ~ 30                 24 ~ 28
肥胖      ≥30                    ≥28
'''
'''
问题需求：
- 输入：给定体重和身高
- 输出：BMI指标分类信息(国际和国内)
思路方法：
-  难点：在于同时输出国际和国内对应的分类
-  思路1：分别计算并给出国际和国内BMI分类
-  思路2：混合计算并给出国际和国内BMI分类
'''
height,weight = eval(input("请输入身高(米)和体重(公斤)[，逗号分隔]："))
bmi = weight / pow(height,2)
print("BMI指数为：{:.2f}".format(bmi))
who = ""
if bmi <18.5:
    who = "偏瘦"
elif 18.5 <= bmi <25:
    who = "正常"
elif 25 <= bmi <30:
    who = "偏胖"
else:
    who = "肥胖"
print("BMI 指标为：国际‘{0}’".format(who))

nat = ""
if bmi <18.5:
    nat = "偏瘦"
elif 18.5 <= bmi <24:
    nat = "正常"
elif 24 <= bmi <28:
    nat = "偏胖"
else:
    nat = "肥胖"
print("BMI 指标为：国内‘{0}’".format(nat))