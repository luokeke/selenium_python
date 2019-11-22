#!/usr/bin/env python
#-*- coding:utf8 -*-
from selenium.webdriver.support.select import Select
import time
class open():
    def open(self,driver):

        time.sleep(2)
        driver.find_element_by_link_text(u"管理中心").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='accordion']/div[3]/div[1]/a").click()
        time.sleep(3)
        driver.find_element_by_xpath(".//*[@id='order-guanli']/ul/li[1]/a").click()
        time.sleep(3)

        driver.find_element_by_xpath(".//*[@id='cl-wrapper']/div[2]/div[2]/div/div[2]/div[1]/ul/li[2]/a").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"开通").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='ydxy']").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='nextbutton']").click()
        time.sleep(2)
        Select(driver.find_element_by_xpath(".//*[@id='choosext']")).select_by_value("2")
        time.sleep(2)
        Select(driver.find_element_by_xpath(".//*[@id='banben']")).select_by_value("123")
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='pwd']").send_keys("aaaAAA111")
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='email']").send_keys("cuiweiwei@zzidc.com")
        time.sleep(2)
        driver.find_element_by_link_text(u"下一步").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='ipbegin']/a").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='ipbegin']/ul/li[2]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='ktbutton']").click()