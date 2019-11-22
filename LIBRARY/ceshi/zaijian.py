#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2017/11/21 16:13 

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
# driver.find_element_by_xpath(".//*[@id='loginform']/div[3]/a").clear()
# driver.find_element_by_xpath(".//*[@id='loginform']/div[3]/a").send_keys("luokeke")
# driver.find_element_by_id("password2-1").clear()
# driver.find_element_by_id("password2-1").send_keys("1")
# driver.implicitly_wait(3)
# driver.find_element_by_xpath(".//*[@id='username']").clear()
# driver.find_element_by_xpath(".//*[@id='username']").send_keys("luokeke")
# driver.implicitly_wait(3)  # 如果元素存在立即执行，如果不存在就等三秒
# driver.find_element_by_id("login-loginok").click()
driver.find_element_by_css_selector("#loginform > div.login-name.mbottom16 > #username").clear()
driver.find_element_by_css_selector("#loginform > div.login-name.mbottom16 > #username").send_keys("luokeke")
driver.find_element_by_id("password2-1").clear()
driver.find_element_by_id("password2-1").send_keys("ceshi2019")
driver.find_element_by_id("login-loginok").click()
sleep(3)
#检测空间是否存储，如果存在直接进入空间内批量上传文件；如果不存在，新建一个空间，然后进入空间内批量上传文件
try:
    sleep(2)
    driver.find_element_by_link_text(bucketname).click()
except:
    driver.find_element_by_link_text(u"新建空间").click()
    driver.find_element_by_id("newBucketName").clear()
    driver.find_element_by_id("newBucketName").send_keys(bucketname)
    driver.find_element_by_link_text(u"确定").click()
    driver.find_element_by_link_text(u"确认").click()
    driver.find_element_by_link_text(bucketname).click()
sleep(2)
#开始上传文件
# 点击页面上上传文件按钮，出现上传文件弹框
driver.find_element_by_id("dropDiv").click()
sleep(1)
driver.implicitly_wait(3)
#上传多个文件
for i in range(0,m):  #上传10个文件，此处参数，可以修改

    file_dir = 'D:\\Pictures'
    for root, dirs, files in os.walk(file_dir):
        pass
    path = files[j]
    pt = 'D:\\Pictures\\' + path
    #点击弹框里上传文件按钮，出现上传文件的选择框
    upload = driver.find_element_by_id("addFile")
    upload.click()
    sleep(1)
    driver.implicitly_wait(3)
    dialog = win32gui.FindWindow('#32770', u'文件上传') # 对话框
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None) # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
    button = win32gui.FindWindowEx(dialog, 0, 'Button', None) # 确定按钮Button
    win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, pt) # 往输入框输入绝对地址
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button) # 按button
    j=j+1
    i=i+1
sleep(15)
up = driver.find_element_by_class_name("layui-layer-btn0")
up.click()