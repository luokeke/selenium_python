#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2017/11/22 10:55
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.delete_all_cookies()
driver.maximize_window()
driver.get("http://gl.zzidc.com")
sleep(3)
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("1")
sleep(3)
driver.find_element_by_css_selector(
    "#loginform > div.login-name.mbottom16 > #username").clear()
driver.find_element_by_css_selector(
    "#loginform > div.login-name.mbottom16 > #username").send_keys("systemmaster")
sleep(3)
# 点击登录按钮
driver.find_element_by_xpath(".//*[@id='loginform']/div[3]/a").click()
sleep(3)