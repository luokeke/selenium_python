#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/4 10:03
# @Author : liuhuiling
import xlrd
# guonei =['www_zzidc_com', 'mc_zzidc_com','ssp_kuaiyun_cn','www_kuaiyun_cn','mc_kuaiyun_cn','pubgl_zzidc_com','beian_zzidc_com,']
# guoji = ['www_zzidc_hk', 'mc_zzidc_hk']
# guojitask = ['zjtask_zzidc_hk','dbtask_zzidc_hk','vctask_zzidc_hk','csafetask_zzidc_hk']
# guoneitask = ['oa_task_zhiguan360_cn','VCBtask_kuaiyun_cn']


# 列表获取 excel元素  https://www.cnblogs.com/insane-Mr-Li/p/9092619.html
fname = '更新站点.xlsx'#设置文件名和路径
date = xlrd.open_workbook(fname)# 打开文件
guonei = date.sheet_by_name("国内").col_values(0, start_rowx=0, end_rowx=None)
guoji = date.sheet_by_name("国际").col_values(0, start_rowx=0, end_rowx=None)
guoneitask = date.sheet_by_name("国内task").col_values(0, start_rowx=0, end_rowx=None)
guojitask = date.sheet_by_name("国际task").col_values(0, start_rowx=0, end_rowx=None)
GN = []
HK = []
GNTASK = []
HKTASK = []

new_site =input( "输入站点名称(站点之间请用空格隔开,退出输入exit)：")
#new_site = "www_zzidc_com www_kuaiyun_cn"
list0 = new_site.split(" ") #split 将输入的字符串数据转换为列表 ,输入的数据转化为列表元素
# Python - 去除list中的空字符和None https://www.cnblogs.com/yspass/p/9434366.html
list1 = list(filter(None, list0)) #filter函数去除list0中的空字符
# 列表元素去重  https://www.cnblogs.com/yunlongaimeng/p/8728647.html
list = sorted(set(list1),key=list1.index)
# list = ['www_zzidc_com', 'www_zzidc_hk', 'mc_zzidc_com','oa_task_zhiguan360_cn','dbtask_zzidc_hk','vctask_zzidc_hk']
for i in range (0,len(list)):  #判断类型
    if list[i] in guonei:
        GN.append(list[i])
    elif list[i] in guoji:
        HK.append(list[i])
    elif list[i] in guoneitask:
        GNTASK.append(list[i])
    elif list[i] in guojitask:
        HKTASK.append(list[i])
print("输入站点数：",(len(list1)))
# print(list1)
print("去重后站点数：",(len(list)))
# print(list)
print("测试更新：")
print("国内：",*GN)
print("国际：",*HK)
print("定时任务站点：")
print("国内：",*GNTASK)
print("国际：",*HKTASK)

