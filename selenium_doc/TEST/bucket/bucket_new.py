#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2018/2/23 16:56
# -*- coding:UTF-8 -*-
import random
import string
from time import sleep
from selenium import webdriver
from TEST.login import Login
'''
脚本作用 ：批量新建存储空间，景安站
循环里参数：m = random.randint(11, 25) 需要根据实际修改变化
'''

n = 5 #可修改，创建  n  个存储空间
login  = "jingan07"
password = "ceshi2015"

#批量创建存储空间
driver = webdriver.Firefox()
driver.delete_all_cookies()
driver.maximize_window()
# 直接访问景安站存储空间链接，并登录。用户名密码可修改
Login().Zzidc_login(driver,login,password)
sleep(3)
driver.get("http://storage.zzidc.com/storage/bucketList")
sleep(3)
#批量创建存储空间开始
for i in range(0,n):  #创建5个空间，此处参数，可以修改
    print ("nihao %d"  %(i))
    m = random.randint(6, 10)
    salt = ''.join(random.sample(string.ascii_letters, m))#此处是随机生成长度为 m  的字符串，可修改
    bucketname = salt.lower()#把生成的字符串转换为小写，赋值给存储空间名。
    # 在存储里新建空间
    driver.implicitly_wait(3)
    sleep(2)
    driver.find_element_by_link_text(u"新建空间").click()
    sleep(2)
    driver.implicitly_wait(3)
    driver.find_element_by_id("newBucketName").clear()
    driver.find_element_by_id("newBucketName").send_keys(bucketname)
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("html/body/div[4]/div[4]/div[3]/div[2]/a").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath(".//*[@id='layui-layer2']/div[3]/a[1]").click()
    driver.implicitly_wait(3)

print ("本次已创建完 %d 个空间"  %(i+1))