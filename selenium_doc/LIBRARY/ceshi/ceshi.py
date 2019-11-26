#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2017/11/21 16:38 

from time import sleep
from selenium import webdriver
import os
import random
import string
import win32gui
from time import sleep
import win32con


m = 0  #上传文件个数，可修改
j = 0 #从文件夹第几个文件开始上传，可修改
n = random.randint(11, 25) #生成一个随机数，作为空间名称的长度
salt = ''.join(random.sample(string.ascii_letters, n))#此处是随机生成长度为6的字符串，6  可以修改
bucketname = salt.lower()#把生成的字符串转换为小写，赋值给存储空间名。

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://mc.zzidc.com/storage/bucketList.action")
sleep(3)
driver.find_element_by_id("username").send_keys("luokeke")
driver.implicitly_wait(3)  # 如果元素存在立即执行，如果不存在就等三秒
driver.find_element_by_id("password").send_keys("1")
driver.implicitly_wait(3)
driver.find_element_by_id("username").clear()
driver.implicitly_wait(3)
driver.find_element_by_id("username").send_keys("luokeke")
driver.implicitly_wait(3)
driver.find_element_by_id("login-loginok").click()
