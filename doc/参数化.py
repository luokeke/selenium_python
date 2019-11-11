#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/23 11:48
# @Author : liuhuiling
from selenium import webdriver
from time import sleep
from pymysql import connect,cursors
import xlrd    ##需要先pip安装xlfd模块，安装方法pip install xlrd
#从excel文件读取用户名和密码+参数化+
data = xlrd.open_workbook('E:\GITHUB\selenium_python\doc\login_xinxi.xlt')
# 给使用到的部分参数赋值---需要提前设定好--
table = data.sheets()[0]  #读取第0个表格
login = table.cell(2, 0).value##读取第1行0列（从0开始计数的）
name = table.cell(2, 1).value##读取第1行1列（从0开始计数的）
password = table.cell(2, 2).value##读取第1行1列（从0开始计数的）
shengfen = table.cell(2, 3).value##读取第1行1列（从0开始计数的）
dishi = table.cell(2, 4).value##读取第1行1列（从0开始计数的）
email = table.cell(2, 5).value##读取第1行1列（从0开始计数的）
mobile = int(table.cell(2, 6).value) ##读取第1行1列（从0开始计数的）
# shangwu = table.cell(2, 7).value##读取第1行1列（从0开始计数的）
print (mobile)