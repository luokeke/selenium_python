#!/usr/bin/env python
#coding:utf-8
import os, time, random, string
from selenium import webdriver

# driver = webdriver.Chrome(r'C:\Users\tony\Desktop\auto test\env\browser driver\chromedriver_win32\chromedriver.exe')
driver = webdriver.Firefox()
driver.get('http://122.114.196.4:8121/ywht/')

# Burst configuration ip
driver.find_element_by_id('username').clear()
driver.find_element_by_id('username').send_keys("likai")
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys("likai")
time.sleep(2)
driver.find_element_by_class_name('loginbutton').click()
time.sleep(2)

driver.find_element_by_xpath(u'//div[text()=\'基础功能\']').click()
time.sleep(2)
driver.find_element_by_xpath(u'//span[text()=\'IP管理\']').click()
time.sleep(2)

driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
driver.find_element_by_id('batchChangeIp').click()

driver.find_element_by_id('ySIp1').find_element_by_xpath('..').find_element_by_class_name('validatebox-invalid').send_keys("122.114.255.0")
driver.find_element_by_id('nSIp1').find_element_by_xpath('..').find_element_by_class_name('validatebox-invalid').send_keys("192.168.101.0")
driver.find_element_by_id('yMask1').find_element_by_xpath('..').find_element_by_class_name('validatebox-invalid').send_keys("255.255.255.0")
driver.find_element_by_id('nMask1').find_element_by_xpath('..').find_element_by_class_name('validatebox-invalid').send_keys("255.255.255.0")
driver.find_element_by_id('tag').click()
time.sleep(2)

# Single configuration ip
driver.refresh()
time.sleep(2)
driver.find_element_by_xpath(u'//div[text()=\'基础功能\']').click()
time.sleep(2)
driver.find_element_by_xpath(u'//span[text()=\'IP管理\']').click()
time.sleep(2)

driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
time.sleep(2)
driver.find_element_by_xpath(u'//div[text()=\'118594\']').click()
time.sleep(2)
driver.find_element_by_id('changeIp').click()
time.sleep(2)
driver.find_element_by_id('mask').clear()
driver.find_element_by_id('mask').send_keys("255.255.255.0")
driver.find_element_by_id('ipV6Gateway').click()

input('Press any key to stop: ')
driver.quit()