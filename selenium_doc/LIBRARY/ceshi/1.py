#!/usr/bin/env python
#-*- coding:utf8 -*-
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.delete_all_cookies()
driver.maximize_window()
driver.get("https://mc.kuaiyun.cn/host/hostList")
sleep(2)
#用户名密码
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("1111111q")
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("cuiwei")
sleep(3)
driver.find_element_by_css_selector("input.kylogin-link.fsize16").click()
sleep(3)
driver.find_element_by_link_text(u"管理").click()
sleep(5)
driver.find_element_by_link_text(u"实名认证").click()
driver.find_element_by_link_text(u"快云服务器管理").click()
driver.find_element_by_link_text(u"磁盘管理").click()
# try:
#     driver.find_element_by_xpath(".//*[@id='tab3_31']/a").click()
# except:
#     driver.find_element_by_css_selector("#tab3_31>a").click()

