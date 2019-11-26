#!/usr/bin/env python
#coding:utf-8
import os, time, random, string
from selenium import webdriver

# driver = webdriver.Chrome(r'C:\Users\tony\Desktop\auto test\env\browser driver\chromedriver_win32\chromedriver.exe')
driver = webdriver.Firefox()
driver.get('http://122.114.196.4:8121/ywht/')

# Search for log
driver.find_element_by_id('username').clear()
driver.find_element_by_id('username').send_keys("kuaiyundb")
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys("admin")
time.sleep(2)
driver.find_element_by_class_name('loginbutton').click()
time.sleep(2)

driver.find_element_by_xpath(u'//div[text()=\'基础功能\']').click()
time.sleep(2)
driver.find_element_by_xpath(u'//span[text()=\'快云数据库日志管理\']').click()
time.sleep(2)

driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
time.sleep(2)
driver.find_element_by_xpath(u'//span[@class=\'textbox combo\']').click()
time.sleep(2)
driver.find_element_by_id('_easyui_combobox_i1_1').click()
driver.find_element_by_xpath(u'//input[@placeholder=\'方法名说明，实例ID，数据库名称\']').send_keys("yzsshi")
time.sleep(1)
driver.find_element_by_xpath(u'//span[text()=\'查询日志\']').click()
time.sleep(1)
driver.find_element_by_xpath(u'//span[text()=\'删除7天以前的备份日志\']').click()
time.sleep(1)
driver.find_element_by_xpath(u'//span[text()=\'确定\']').click()
time.sleep(1)
driver.find_element_by_xpath(u'//span[text()=\'确定\']').click()

input('Press any key to stop: ')
driver.quit()