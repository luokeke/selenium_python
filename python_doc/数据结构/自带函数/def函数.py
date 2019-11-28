#!/usr/bin/python
# -*- coding: UTF-8 -*-

def wash_face():
    print ("-------")
    print ("向盆子里面接凉水")
    print ("向盆子里面兑热水")
    print ("洗把脸")
    print ("把水倒掉")
    print ("清洗毛巾")
    return

def eat(food): # 这里的 food 最终会被调用者传过来的值所代替
    # food = "鸡蛋"
    print ("-------")
    print ("做饭 >>>>>>>>> " + food)
    print ("吃饭")
    print ("漱口")
    print ("洗碗")
    return

def depart(transport, to):
    print ("-------")
    print( "☆ 乘坐交通工具" + transport + "到" )+ to
    return

# 正常工作日的一天
wash_face()
eat("鸡蛋")
depart("自行车", "单位")

print ("-------")
print ("在单位辛苦工作8小时")
print ("外面下雨了")

depart("出租车", "家")
eat("晚饭")
wash_face()

print ("-------")
print ("单身的人一定没有夜生活")
print ("狗带")