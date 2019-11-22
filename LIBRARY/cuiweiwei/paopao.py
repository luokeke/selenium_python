#!/usr/bin/env python
from selenium import webdriver

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
sleep(8)
driver.find_element_by_link_text(u"管理").click()