# -*- coding:UTF-8 -*-
from TEST.login import *
from selenium import webdriver
from time import sleep
'''
脚本作用 ：批量删除存储空间，景安站
'''
n = 10 #删除存储空间内前  n  个空间，此处参数，可以修改
login  = "jingan07"
password = "ceshi2015"

#批量删除存储空间
driver = webdriver.Firefox()
driver.delete_all_cookies()
driver.maximize_window()
# 直接访问景安站存储空间链接，并登录。用户名密码可修改
login().Zzidc_login(driver,login, password)
sleep(3)
driver.get("http://storage.kuaiyun.cn/storage/listObjects?bucketName=sdfkja456")
sleep(3)
#批量删除存储空间开始
for i in range(0,n):
    driver.implicitly_wait(3)
    driver.find_element_by_link_text(u"删除").click()
    sleep(1)
    driver.find_element_by_css_selector("a.layui-layer-btn0").click()
    sleep(1)
    # i=i+1;
    # print i
print "本次已删除 %d 个空间"  %(i+1)
