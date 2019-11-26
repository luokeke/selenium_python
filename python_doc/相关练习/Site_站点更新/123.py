#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/5 10:03
# @Author : liuhuiling

def NAME():
    xuanze = input("姓名请输入1，爱好请输入2：")
    while xuanze == '1':
        name = input("请输入你的姓名，退出请输入exit：")
        if name == "exit":
            xuanze = input("姓名请输入1，爱好请输入2:")
        else:
            print(name)
    while xuanze == '2':
        print("========================================")
        print("1.篮球；2.阅读；3.钢琴；4.骑行；5.攀岩：")
        aihao = input("请输入爱好编号，退出请输入exit：")
        list = ['1','2','3','4','5']
        # while aihao in list:
        if aihao =='1':
            print("qiaodan")
            print("========================================")
            print("1.篮球；2.阅读；3.钢琴；4.骑行；5.攀岩：")
            aihao = input("请输入爱好编号，退出请输入exit：")
        elif aihao =='2':
            print("傲慢与偏见")
            print("========================================")
            print("1.篮球；2.阅读；3.钢琴；4.骑行；5.攀岩：")
            aihao = input("请输入爱好编号，退出请输入exit：")
        elif aihao =='3':
            print("雅马哈")
            print("========================================")
            print("1.篮球；2.阅读；3.钢琴；4.骑行；5.攀岩：")
            aihao = input("请输入爱好编号，退出请输入exit：")
        elif aihao =='4':
            print("川藏线")
            print("========================================")
            print("1.篮球；2.阅读；3.钢琴；4.骑行；5.攀岩：")
            aihao = input("请输入爱好编号，退出请输入exit：")
        elif aihao =='5':
            print("川藏线")
            print("========================================")
            print("1.篮球；2.阅读；3.钢琴；4.骑行；5.攀岩：")
            aihao = input("请输入爱好编号，退出请输入exit：")
        elif aihao =='exit':
            xuanze = input("姓名请输入1，爱好请输入2：")
NAME()