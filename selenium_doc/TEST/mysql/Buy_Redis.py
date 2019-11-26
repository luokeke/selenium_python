#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2017/11/13 18:06 
from TEST.login import *

username = "luokeke"
password = "1"
gmlx = 1 #1 入门型 2 进阶型 3 通用型 4 高速型
gmsc = 1 #0-36 月 整数
driver = webdriver.Firefox()
driver.delete_all_cookies()
driver.maximize_window()
Test_login().Zzidc_login(driver,username,password)
sleep(2)
driver.get("https://www.zzidc.com/database/buyRedis")

#选型号
if gmlx == 1:
    driver.find_element_by_xpath(".//*[@id='pzul']/li[1]/a").click()
elif gmlx == 2:
    driver.find_element_by_xpath(".//*[@id='pzul']/li[2]/a").click()
elif gmlx == 3:
    driver.find_element_by_xpath(".//*[@id='pzul']/li[3]/a").click()
elif gmlx == 4:
    driver.find_element_by_xpath(".//*[@id='pzul']/li[4]/a").click()
sleep(2)
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
