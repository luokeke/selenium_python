#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2018/6/21 16:26

from selenium import webdriver
import logging
from  time import  sleep
#获取浏览器操作权限，打开，清理缓存并最大化
#logging.basicConfig(level=logging.DEBUG)
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://mc.zzidc.com/")
driver.add_cookie({'login-name':'username','valeu':'luokeke'})
driver.add_cookie({'login-name':'username','valeu':'luokeke'})
# driver.find_element_by_id("password").clear()
# driver.find_element_by_id("password").send_keys(1)
# sleep(3)
# driver.find_element_by_css_selector(
#     "#loginform > div.login-name.mbottom16 > #username").clear()
# driver.find_element_by_css_selector(
#     "#loginform > div.login-name.mbottom16 > #username").send_keys('luokeke')
# sleep(3)
# # 点击登录按钮
# driver.find_element_by_xpath(".//*[@id='loginform']/div[3]/a").click()
# sleep(3)







