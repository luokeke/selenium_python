#!/usr/bin/env python
#coding:utf-8
import os, time, random, string
from selenium import webdriver

rdseed = list(string.ascii_uppercase) + list(string.digits) + list(string.ascii_lowercase)
collection_offset = '012' # base is 1000, 1000 stand for zhengzhou, 1001 for beijing, 1002 for hongkong

# driver = webdriver.Chrome(r'C:\Users\tony\Desktop\auto test\env\browser driver\chromedriver_win32\chromedriver.exe')
driver= webdriver.Chrome()
# driver = webdriver.Firefox()
driver.get('http://122.114.196.4:8121/ywht/')

# Create
driver.find_element_by_id('username').clear()
driver.find_element_by_id('username').send_keys("likai")
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys("likai")
time.sleep(2)
driver.find_element_by_class_name('loginbutton').click()
time.sleep(2)

driver.find_element_by_xpath(u'//div[text()=\'配置管理\']').click()
time.sleep(2)
driver.find_element_by_xpath(u'//span[text()=\'汇聚配置\']').click()
time.sleep(2)

driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
driver.find_element_by_id('addCon').click()
remark = ''.join(random.sample(rdseed, 5))
driver.find_element_by_id('remark').send_keys(remark)
driver.find_element_by_id('city').click()
driver.find_element_by_xpath(u'//option[@value=100%s]' % ''.join(random.sample(collection_offset, 1))).click()
driver.find_element_by_xpath(u'//span[text()=\'添加\']').click()
time.sleep(1)
alert = driver.switch_to.alert
print(alert.text)
alert.dismiss()
time.sleep(2)

#
# # Modify
driver.refresh()
time.sleep(2)
driver.find_element_by_xpath(u'//div[text()=\'配置管理\']').click()
time.sleep(2)
driver.find_element_by_xpath(u'//span[text()=\'汇聚配置\']').click()
time.sleep(2)
driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
driver.find_element_by_xpath(u'//div[text()=\'%s\']' %  remark).click()
driver.find_element_by_id('changeCon').click()
driver.find_element_by_id('city').click()
driver.find_element_by_xpath(u'//option[@value=100%s]' % ''.join(random.sample(collection_offset, 1))).click()
driver.find_element_by_xpath(u'//span[text()=\'修改\']').click()
time.sleep(1)
alert = driver.switch_to.alert
print(alert.text)
alert.dismiss()
time.sleep(2)

# Delete
driver.refresh()
time.sleep(2)
driver.find_element_by_xpath(u'//div[text()=\'配置管理\']').click()
time.sleep(2)
driver.find_element_by_xpath(u'//span[text()=\'汇聚配置\']').click()
time.sleep(2)
driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
driver.find_element_by_xpath(u'//div[text()=\'%s\']' %  remark).click()
driver.find_element_by_id('delectCon').click()
driver.find_element_by_xpath(u'//span[text()=\'确定\']').click()
time.sleep(1)
driver.find_element_by_xpath(u'//span[text()=\'确定\']').click()

raw_input('Press any key to stop: ')
driver.quit()