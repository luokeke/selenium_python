#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/29 9:15
# @Author : liuhuiling
print()
'''
函数是一段代码的表示
- 函数是一段具有特定功能的可重用的语句组
- 函数是一种功能的抽象，一般函数表达特定功能
- 两个作用：降低编程难度和代码复用

函数的定义
使用保留字def来定义函数，return给出返回值
def <函数名>(<参数(0个或多个)>):
    <函数体>
    return <返回值>
    
- 函数定义时，参数是输入、函数体是处理、结果是输出(IPO)
- 函数定义后，不经调用，不会被执行
- 函数定义时，所指定的参数是一种占位符

函数的调用
函数名(参数)
- 调用时给出实际参数
- 实际参数替换定义中的参数
- 函数调用后得到返回值

函数的参数传递
- 参数个数：可以有参数也可以没有，()必须保留
- 可选参数传递：函数定义时可以为某些参数指定默认值，构成可选参数
    def <函数名>(<非可选参数,可选参数>):
        <函数体>
        return <返回值>
    强制约定：可选参数需要放必选参数后面
- 可变参数传递：函数定义设计时可以设计可变数量参数，即不确定参数总量
    def <函数名>(<参数,*b>): *b来表达不确定的参数
        <函数体>
        return <返回值>
    max() min()就是可变参数传递

参数传递的两种方式
- 位置传递  fact(10,5)
- 名称传递  fact(m=10,n=5)

函数的返回值：
- return 保留字用来传递返回值
- 函数可以有返回值，也可以没有，可以有return，也可以没有
- return可以传递0个返回值，也可以传递任意多个返回值

局部变量和全局变量
-局部变量 函数内部使用的变量
-全局变量 函数外部整个程序使用的变量
使用规则：
-规则1:基本数据类型，无论是否重名，局部变量与全局变量不同
       局部变量是函数内部的占位符，与全局变量可能重名但不同
- 函数运算结束后，局部变量被释放
- 可以使用global保留字在函数内部使用全局变量
-规则2：组合数据类型，如果局部变量未真实创建，等同于全局变量

ls = ["F","f"] #通过使用[]真是创建一个全局变量列表ls
def func(a):
    ls.append(a)#此处ls是列表类型，未真实创建，则是全局变量
    return
func("C")#全局变量ls被修改
print(ls) #结果：['F', 'f', 'C']


'''
#参数传递 n！计算
def fact(n): #fact函数名 n参数
    s  = 1
    for i in range(1,n+1):
        s *= i
    return  s #返回值
print(fact(5)) #120  #函数调用过程

#可选参数  n！//m
def fact(n,m=1): #fact函数名 n参数
    s  = 1
    for i in range(1,n+1):
        s *= i
    return  s//m #返回值
print(fact(5)) #120
print(fact(5,3)) #40  给定可选参数 m为3
print(fact(m=10,n=5)) #12

#可变参数 计算n!*b
def fact(n,*b): #fact函数名 n参数
    s  = 1
    for i in range(1,n+1):
        s *= i
    for item in b:
        s *= item
    return  s
print(fact(5)) #120
print(fact(5,3)) #360  给定可变参数 b为3
print(fact(10,3,5,8)) #435456000

#return返回多个返回值
def fact(n,m=1):
    s  = 1
    for i in range(1,n+1):
        s *= i
    return  s//m,n,m #多个返回值中间有，分隔
print(fact(5)) #(120, 5, 1)  #多个返回值

#局部变量和全局变量
n , s = 10 , 100
def face(n):
    s = 1 #这里的s为局部变量
    for i in range(1,n+1):
        s *= i
    return s
print(fact(n),s)  #s

n , s = 10 , 100
def fact(n):
    global s #用global保留字使用全局变量
    for i in range(1,n+1):
        s =s* i
    return s
print(fact(n),s)



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