#!/usr/bin/env python
#-*- coding:utf8 -*-
from selenium import webdriver
from buy import *
driver = webdriver.Firefox()
driver.delete_all_cookies()
driver.maximize_window()
driver.get("http://www.kuaiyun.cn")
sleep(2)
driver.find_element_by_link_text(u"登录").click()
sleep(2)
#用户名密码
driver.find_element_by_xpath(".//*[@id='username']").send_keys("cuiwei3")
driver.find_element_by_xpath(".//*[@id='password']").send_keys("1111111q")
sleep(2)
driver.find_element_by_xpath("html/body/div[2]/div[2]").click()
sleep(2)
driver.find_element_by_xpath(".//*[@id='login-form']/div[5]/input").click()
buy().buy(driver)
