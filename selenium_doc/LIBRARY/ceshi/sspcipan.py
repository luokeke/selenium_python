#!/usr/bin/env python
#-*- coding:utf8 -*-
#服务器ssp磁盘管理
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
class cipan():
    def cipan(self,driver):
        sleep(3)
        # yprl = "10"
        # sleep(3)
        driver.find_element_by_xpath(".//*[@id='navigate_bar']/div/div[3]/a[4]").click()
        sleep(3)
        driver.find_element_by_link_text(u"产品中心").click()
        # driver.find_element_by_xpath(".//*[@id='accordion']/div[2]/div[1]/a").click()
        sleep(3)
        driver.find_element_by_xpath(".//*[@id='product']/ul/li[1]/a").click()
        sleep(8)
        driver.find_element_by_link_text(u"管理").click()
        sleep(5)
        # driver.find_element_by_xpath("html/body/div[9]/div[3]/div/button").click()
        # sleep(3)
        # driver.find_element_by_xpath("//button[@type='button']").click()
        try:
            driver.find_element_by_link_text("磁盘管理").click()
        except:
            driver.find_element_by_xpath("//button[@type='button']").click()
        # driver.find_element_by_xpath(".//*[@id='tab3_31']/a").click()
        sleep(5)
        driver.find_element_by_link_text(u"添加磁盘").click()
        sleep(3)
        driver.find_element_by_id("disk").clear()
        driver.find_element_by_id("disk").send_keys("1")
        driver.find_element_by_xpath("//button[@type='button']").click()
        # a = int(input("请输入硬盘容量"))
        # sleep(3)
        # driver.find_element_by_xpath(".//*[@id='disk']").send_keys("yprl")
        # sleep(3)
        # driver.find_element_by_xpath("html/body/div[10]/div[3]/div/button[1]").click()
        # sleep(3)
