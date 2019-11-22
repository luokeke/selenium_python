#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2017/11/13 15:43
from TEST.login import *

gmpz = 4 # 1微型 2小型 3中型 4大型
sjkbb = 5.6 #5.5  MySQL5.5   5.6  MySQL5.6
gmsc =  5 # 0-36
username = "luokeke"
password = "1"

driver = webdriver.Firefox()
driver.delete_all_cookies()
driver.maximize_window()
Test_login().Zzidc_login(driver,username,password)
sleep(2)
# 数据库独享版购买页地址#"https://www.zzidc.com/database/choosedxconfig"
#带登录的页面："http://ac.zzidc.com/cas/login?service=https%3A%2F%2Fwww.zzidc.com%2Fdatabase%2Fchoosedxconfig"
driver.get("http://ac.zzidc.com/cas/login?service=https%3A%2F%2Fwww.zzidc.com%2Fdatabase%2Fchoosedxconfig")
sleep(2)
#独享版
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div[2]/div[1]/div[2]/ul/li[1]/a").click()
sleep(2)
#购买配置   1微型 2小型 3中型 4大型
if gmpz == 1:
    driver.find_element_by_xpath(".//*[@id='pzul']/li[1]/a").click()
elif gmpz == 2:
    driver.find_element_by_xpath(".//*[@id='pzul']/li[2]/a").click()
elif gmpz == 3:
    driver.find_element_by_xpath(".//*[@id='pzul']/li[3]/a").click()
elif gmpz == 4:
    driver.find_element_by_xpath(".//*[@id='pzul']/li[4]/a").click()
sleep(2)
#数据库版本  5.5  MySQL5.5   5.6  MySQL5.6
if sjkbb  == 5.5:
    driver.find_element_by_xpath(".//*[@id='choosebb']/li[1]/a").click()
elif sjkbb ==5.6:
    driver.find_element_by_xpath(".//*[@id='choosebb']/li[2]/a").click()
sleep(2)
#购买时长  # 0-36个月
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


