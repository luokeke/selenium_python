#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2018/5/22 19:15
from selenium import webdriver
from time import sleep
from login01 import *
'''
脚本作用 ：服务器ssp功能
'''
#批量删除存储空间
driver = webdriver.Firefox()
driver.delete_all_cookies()
driver.maximize_window()
# 直接访问景安站存储空间链接，并登录。用户名密码可修改
Login().Ky_login(driver,"luokeke", "1")
sleep(3)
driver.get("https://mc.kuaiyun.cn/host/hostList")
sleep(3)
driver.find_element_by_link_text(u"管理").click()
sleep(5)
#打开管理跳转到新页面，涉及到多窗口操作。
all_window_handle = driver.window_handles # 获取打开的所有窗口句柄
driver.switch_to.window(all_window_handle[-1]) # 激活最顶层窗口句柄
#重装系统标签
driver.find_element_by_id("tab3_7").click()
sleep(5)


