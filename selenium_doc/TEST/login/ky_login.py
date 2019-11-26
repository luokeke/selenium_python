#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2017/11/22 10:10 
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.delete_all_cookies()
driver.maximize_window()
driver.get("http://www.kuaiyun.cn")
sleep(3)
driver.find_element_by_link_text(u"登录").click()
sleep(3)
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("1")
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("luokeke")
sleep(3)
driver.find_element_by_css_selector("input.kylogin-link.fsize16").click()
sleep(3)
driver.get("http://mc.kuaiyun.cn")