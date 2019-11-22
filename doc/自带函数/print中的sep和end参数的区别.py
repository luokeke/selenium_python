#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/22 0:01
# @Author : liuhuiling
print(1)
'''
参考链接：print中的sep和end参数的区别 https://blog.csdn.net/qq_43701814/article/details/91490349
1. end参数[后跟字符]
end：可以设置print打印结束时最后跟的字符形式。
    s1 = 'hello'
    s2 = 'world'
    print(s1)
    print(s2)
    输出：
    hello
    world
    
s1 = 'hello'
s2 = 'world'
print(s1, end=' ')
print(s2)
输出：hello world

    s1 = 'hello'
    s2 = 'world'
    print(s1, end=',')
    print(s2)
    输出：hello,world
2. sep参数[分隔符]
sep：可以设置print中分隔不同值的形式。
    s1 = 'hello'
    s2 = 'world'
    print(s1, s2)
    输出：hello world

s1 = 'hello'
s2 = 'world'
print(s1, s2, sep=', ')
输出：hello, world

'''