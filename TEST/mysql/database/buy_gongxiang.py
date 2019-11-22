#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2017/11/13 17:33 
from TEST.login.login_zuofei import *
driver = webdriver.Firefox()
driver.delete_all_cookies()
driver.maximize_window()
Login().user_login(driver,"http://ac.zzidc.com/cas/login?service=https%3A%2F%2Fwww.zzidc.com%2Fdatabase%2Fchoosedxconfig","luokeke","1")
sleep(2)
gmjf = 1 # 1郑州机房 2香港机房
chkj = 5 #1-20 数字
gmsc = 5 # 0-36
#共享版
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div[2]/div[1]/div[2]/ul/li[2]/a").click()
sleep(2)
#选机房
if gmjf == 1:
    driver.find_element_by_id("").click()
elif gmjf == 2:
    driver.find_element_by_id("").click()
#选存储空间
driver.find_element_by_id("diskinput").clear()
driver.find_element_by_id("diskinput").send_keys(chkj)
#购买时长
driver.find_element_by_id("timeinput").clear()
driver.find_element_by_id("timeinput").send_keys(gmsc)
sleep(2)
#购买
driver.find_element_by_id("buy").click()
sleep(2)
#支付
driver.find_element_by_xpath("./html/body/div[2]/div/div[5]/div/div[2]/div[2]/a[2]").click()
sleep(2)
#确认支付
driver.find_element_by_xpath(".//*[@id='layui-layer1']/div[3]/a[1]").click()
sleep(2)
#确认支付成功
driver.find_element_by_xpath(".//*[@id='layui-layer3']/div[3]/a[1]").click()
sleep(2)


