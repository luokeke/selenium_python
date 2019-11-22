#!/usr/bin/env python
#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
# from ceshi.mclogin尝试 import *
driver = webdriver.Firefox()
#清除cookies
driver.delete_all_cookies()
#窗口最大化
driver.maximize_window()
Mc().in_kymc()
driver.implicitly_wait(3)
# 调用登录
driver.find_element_by_xpath(".//*[@id='navigate_bar']/div/div[3]/div/div/a[1]").click()
time.sleep(2)
driver.find_element_by_id("username").send_keys("wyf.mir")
time.sleep(4)
driver.find_element_by_id("password").send_keys(1)
time.sleep(4)
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("wyf.mir")
driver.find_element_by_xpath(".//*[@id='login-form']/div[5]/input").click()

above = driver.find_element_by_xpath(".//*[@id='J_common_header_menu']/li[2]/span")
ActionChains(driver).move_to_element(above).perform()
jisuan  = driver.find_element_by_xpath(".//*[@id='J_common_header_menu']/li[2]/div/div/div[1]/a[1]")
ActionChains(driver).context_click(jisuan).perform()
vps = driver.find_element_by_xpath(".//*[@id='J_common_header_menu']/li[2]/div/div/div[2]/div[1]/div/div[4]/a").click()
driver.implicitly_wait(3)
Select(driver.find_element_by_id("gmqx")).select_by_visible_text(u"289元/半年")
# 价格下拉框获取
driver.find_element_by_id("buy1629").click()
# driver.find_element_by_id("selectall").click()
# driver.find_element_by_id("orderId9934").click()
driver.find_element_by_link_text(u"去支付").click()
driver.find_element_by_xpath("//button[@type='button']").click()
driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
driver.find_element_by_link_text(u"详情").click()

    
