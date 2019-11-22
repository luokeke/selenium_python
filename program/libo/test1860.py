#!/usr/bin/env python
#coding:utf-8
import os, time, random, string
from selenium import webdriver

rdseed = list(string.ascii_uppercase) + list(string.digits) + list(string.ascii_lowercase)

# driver = webdriver.Chrome(r'C:\Users\tony\Desktop\auto test\env\browser driver\chromedriver_win32\chromedriver.exe')
driver = webdriver.Firefox()
driver.get('http://122.114.196.4:8121/ywht/')

# Modify
driver.find_element_by_id('username').clear()
driver.find_element_by_id('username').send_keys("likai")
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys("likai")
time.sleep(2)
driver.find_element_by_class_name('loginbutton').click()
time.sleep(2)

driver.find_element_by_xpath(u'//div[text()=\'资产管理\']').click()
time.sleep(2)
driver.find_element_by_xpath(u'//span[text()=\'资产列表\']').click()
time.sleep(2)

driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
time.sleep(1)
driver.find_element_by_id('datagrid-row-r1-2-0').click()
time.sleep(1)
driver.find_element_by_xpath(u'//span[text()=\'修改资产\']').click()
time.sleep(1)
driver.find_element_by_name('assetVo.cpu').clear()
driver.find_element_by_name('assetVo.cpu').send_keys(''.join(random.sample(rdseed, 5)))
driver.find_element_by_name('assetVo.ram').clear()
driver.find_element_by_name('assetVo.ram').send_keys(''.join(random.sample(rdseed, 5)))
driver.find_element_by_name('assetVo.disk').clear()
driver.find_element_by_name('assetVo.disk').send_keys(''.join(random.sample(rdseed, 5)))
driver.find_element_by_name('assetVo.raid').clear()
driver.find_element_by_name('assetVo.raid').send_keys(''.join(random.sample(rdseed, 5)))
driver.find_element_by_name('assetVo.motherboard').clear()
driver.find_element_by_name('assetVo.motherboard').send_keys(''.join(random.sample(rdseed, 5)))
driver.find_element_by_name('assetVo.power').clear()
driver.find_element_by_name('assetVo.power').send_keys(''.join(random.sample(rdseed, 5)))
driver.find_element_by_name('assetVo.netModel').clear()
driver.find_element_by_name('assetVo.netModel').send_keys(''.join(random.sample(rdseed, 5)))
driver.find_element_by_xpath(u'//span[text()=\'确定\']').click()
time.sleep(1)

driver.find_element_by_xpath(u'//a[@class=\'panel-tool-close\']').click()
time.sleep(1)
driver.find_element_by_xpath(u'//span[text()=\'返回\']').click()

raw_input('Press any key to stop: ')
driver.quit()