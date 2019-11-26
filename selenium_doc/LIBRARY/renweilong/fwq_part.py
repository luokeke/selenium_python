#!/usr/bin/env python
#coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium import webdriver
import unittest
from time import sleep
import time
import os
import win32gui
import win32con

import tkMessageBox
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class fwq():



#                                购买
# ========================================================================
    def goumai(self,driver):
        gmlx="香港机房"
        pz=u"快云服务器Ⅲ型" # Ⅰ,Ⅱ,Ⅳ,Ⅴ, u"快云服务器Ⅲ型"   u"自选配置"
        gmsc="2"#时间1-14   11 1年，12 2年  ，13 3年，14  5年
        czxt="CentOS"#Windows,Centos,Debian,Ubuntu
        xtbb="CentOS-6.8-x86_64"

        #当为自选时，参数
        sjp="100"#大小
        cpu=""#1,2,4,8,16
        nc=""#cpu为1时1,2,4,8,12；2时2,4,8,12,16；4时4,8，12，16，24；8时8,12，，16，24，32，16时12，16，24，32，64
        gwdk="15"#1-100M


        driver.get("https://www.kuaiyun.cn/kcloud/config")
        driver.find_element_by_link_text(pz).click()
        if "香港" in gmlx:
            driver.find_element_by_link_text(u"香港机房").click()
        driver.find_element_by_css_selector("input.bk-disk-input").clear()
        driver.find_element_by_css_selector("input.bk-disk-input").send_keys(sjp)
        #cpu跟核数不知道咋写目前没写

        driver.find_element_by_xpath("html/body/div[4]/div[1]/div[1]/div[2]/div[6]/div[2]/div[2]/input").clear()
        driver.find_element_by_xpath("html/body/div[4]/div[1]/div[1]/div[2]/div[6]/div[2]/div[2]/input").send_keys(sjp)

        driver.find_element_by_link_text(u"下一步选择时长与镜像").click()
        gmsc1="//div[@id='slider-date-2']/ul/li["+gmsc+"]"
        driver.find_element_by_xpath(gmsc1).click()
        driver.find_element_by_link_text(czxt).click()
        #选择系统版本
        driver.find_element_by_css_selector("cite").click()
        print xtbb
        sleep((2))
        driver.find_element_by_link_text(xtbb).click()


        sleep(2)
        driver.find_element_by_link_text(u"立即购买").click()
