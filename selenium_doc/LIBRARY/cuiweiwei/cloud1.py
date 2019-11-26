#!/usr/bin/env python
#-*- coding:utf8 -*-
# from buy import *
# from jiesuan import *
# from kaitong import *
# from Continued import *
# from shengji import *
from selenium import webdriver
from sspcipan import *
driver = webdriver.Firefox()
driver.delete_all_cookies()
driver.maximize_window()
driver.get("https://mc.kuaiyun.cn/host/hostList")
sleep(2)
driver.find_element_by_link_text(u"登录").click()
sleep(2)
#用户名密码
driver.find_element_by_xpath(".//*[@id='username']").send_keys("cuiwei")
driver.find_element_by_xpath(".//*[@id='password']").send_keys("1111111q")
sleep(2)
driver.find_element_by_xpath("html/body/div[2]/div[2]").click()
sleep(2)
driver.find_element_by_xpath(".//*[@id='login-form']/div[5]/input").click()
sleep(3)
# buy().buy(driver)
# jiesuan().jiesuan(driver)
# kaitong().kaitong(driver)
# shengji().shengji(driver)
# xufei().xufei(driver)
cipan().cipan(driver)