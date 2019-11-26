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

class diaoyongbufen():


#                                  登录
#============================================================
    def usr_login(self,driver):
        #driver = webdriver.Firefox()
        login = u"12212212224"
        password = u"4429836q"
        driver.get("http://www.kuaiyun.cn/")
        driver.maximize_window()


        driver.find_element_by_link_text("登录").click()
        time.sleep(2)
        driver.find_element_by_id("username").send_keys(login)
        time.sleep(1)
        driver.find_element_by_id("password").send_keys(password)
        time.sleep(1)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(login)
        driver.find_element_by_xpath(".//*[@id='login-form']/div[5]/input").click()
        sleep(2)
#=====================================================================




#                                购买
#========================================================================
    def goumai(self,driver):
        #driver = webdriver.Firefox()
        gmlx = "快云vps郑州机房经济型"  # 举例快云vps郑州机房经济型,
        gmsc = "6m"  # 1m,1y月年
        czxt = "CentOS 6.7"  # Windows2003,CentOS 6.7,Windows2008-未激活         使用时请复制后面三种类型
        gmlx = "快云vps郑州机房经济型"  # 举例快云vps郑州机房经济型,
        driver.get("http://www.kuaiyun.cn/vps/kyvpsindex")
        if "vps" in gmlx:
            # driver.find_element_by_css_selector("div.menu-dropdown-down-item.mtop26 > a.nav-link").click()
            driver.get("http://www.kuaiyun.cn/vps/kyvpsindex")
            # driver.find_element_by_xpath("//ul[@id='J_common_header_menu']/li[2]/div/div/div[2]/div/div/div[4]/a").click()



            if "基础" in gmlx:
                print "选择为基础型"
                sleep(2)
                if czxt == "CentOS 6.7":
                    driver.find_element_by_xpath("//div[@id='os1629']/div[2]/span[2]").click()
                elif czxt == "Windows2008-未激活":
                    driver.find_element_by_xpath("//div[@id='os1629']/div[3]/span").click()
                sleep(2)
                if gmsc == "1m":
                    Select(driver.find_element_by_xpath("(//select[@id='gmqx'])")).select_by_visible_text(u"49元/1个月")
                elif gmsc == "6m":
                    Select(driver.find_element_by_xpath("(//select[@id='gmqx'])")).select_by_visible_text(u"289元/半年")
                elif gmsc == "1y":
                    Select(driver.find_element_by_xpath("(//select[@id='gmqx'])")).select_by_visible_text(u"560元/1年")
                elif gmsc == "2y":
                    Select(driver.find_element_by_xpath("(//select[@id='gmqx'])")).select_by_visible_text(u"1100元/2年")
                elif gmsc == "3y":
                    Select(driver.find_element_by_xpath("(//select[@id='gmqx'])")).select_by_visible_text(u"1600元/3年")
                elif gmsc == "5y":
                    Select(driver.find_element_by_xpath("(//select[@id='gmqx'])")).select_by_visible_text(u"2600元/5年")

                try:
                    driver.find_element_by_id("buy1629").click();
                except:
                    print "基础型加入购物车"

            if "普及" in gmlx:
                print "选择为普及型"
                sleep(2)
                if czxt == "CentOS 6.7":
                    driver.find_element_by_xpath("//div[@id='os1630']/div[2]/span[2]").click()
                elif czxt == "Windows2008-未激活":
                    driver.find_element_by_xpath("//div[@id='os1630']/div[3]/span").click()
                sleep(2)
                if "北京" in gmlx:
                    driver.find_element_by_xpath("//div[@id='dq1630']/div[2]/span").click()
                elif "香港" in gmlx:
                    driver.find_element_by_xpath("//div[@id='dq1630']/div[3]/span").click()
                sleep(2)

                if "郑州" in gmlx:
                    if gmsc == "1m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[2]")).select_by_visible_text(
                            u"111元/1个月")
                    elif gmsc == "6m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[2]")).select_by_visible_text(u"599元/半年")
                    elif gmsc == "1y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[2]")).select_by_visible_text(u"999元/1年")
                    elif gmsc == "2y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[2]")).select_by_visible_text(
                            u"1900元/2年")
                    elif gmsc == "3y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[2]")).select_by_visible_text(
                            u"2700元/3年")
                    elif gmsc == "5y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[2]")).select_by_visible_text(
                            u"4400元/5年")
                elif "北京" in gmlx:
                    if gmsc == "1m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[2]")).select_by_visible_text(
                            u"180元/1个月")
                    elif gmsc == "6m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[2]")).select_by_visible_text(u"900元/半年")
                    elif gmsc == "1y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[2]")).select_by_visible_text(
                            u"1699元/1年")
                    elif gmsc == "2y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[2]")).select_by_visible_text(
                            u"3230元/2年")
                    elif gmsc == "3y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[2]")).select_by_visible_text(
                            u"4590元/3年")
                    elif gmsc == "5y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[2]")).select_by_visible_text(
                            u"7600元/5年")

                elif "香港" in gmlx:
                    if gmsc == "1m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[2]")).select_by_visible_text(u"99元/1个月")
                        # elif gmsc=="6m":
                        # Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[2]")).select_by_visible_text(u"999元/半年")
                    elif gmsc == "1y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[2]")).select_by_visible_text(u"999元/1年")
                    elif gmsc == "2y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[2]")).select_by_visible_text(
                            u"1900元/2年")
                    elif gmsc == "3y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[2]")).select_by_visible_text(
                            u"2700元/3年")
                    elif gmsc == "5y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[2]")).select_by_visible_text(
                            u"4400元/5年")

                try:
                    driver.find_element_by_id("buy1630").click();
                except:
                    print "普及型加入购物车"

            if "经济" in gmlx:
                print "选择为经济型"

                sleep(2)
                if czxt == "CentOS 6.7":
                    driver.find_element_by_xpath("//div[@id='os1631']/div[2]/span[2]").click()
                elif czxt == "Windows2008-未激活":
                    driver.find_element_by_xpath("//div[@id='os1631']/div[3]/span").click()
                sleep(2)
                if "北京" in gmlx:
                    driver.find_element_by_xpath("//div[@id='dq1631']/div[2]/span").click()
                elif "香港" in gmlx:
                    driver.find_element_by_xpath("//div[@id='dq1631']/div[3]/span").click()
                sleep(2)
                if "郑州" in gmlx:
                    if gmsc == "1m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(
                            u"222元/1个月")
                    elif gmsc == "6m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(
                            u"1199元/半年")
                    elif gmsc == "1y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(
                            u"1999元/1年")
                    elif gmsc == "2y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(
                            u"3800元/2年")
                    elif gmsc == "3y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(
                            u"5400元/3年")
                    elif gmsc == "5y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(
                            u"8800元/5年")

                elif "北京" in gmlx:
                    if gmsc == "1m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(
                            u"260元/1个月")
                    elif gmsc == "6m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(
                            u"1300元/半年")
                    elif gmsc == "1y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(
                            u"2399元/1年")
                    elif gmsc == "2y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(
                            u"4560元/2年")
                    elif gmsc == "3y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(
                            u"6480元/3年")
                    elif gmsc == "5y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(
                            u"10500元/5年")

                elif "香港" in gmlx:
                    if gmsc == "1m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(
                            u"218元/1个月")
                    elif gmsc == "3m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(u"580元/季度")
                    elif gmsc == "6m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(
                            u"1100元/半年")
                    elif gmsc == "1y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(
                            u"1999元/1年")
                    elif gmsc == "2y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(
                            u"3900元/2年")
                    elif gmsc == "3y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(
                            u"5800元/3年")
                    elif gmsc == "5y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(
                            u"9600元/5年")

                print gmsc
                try:
                    driver.find_element_by_id("buy1631").click();
                except:
                    print "经济型加入购物车"

            if "豪华" in gmlx:
                print "选择为豪华型"

                sleep(2)
                if czxt == "CentOS 6.7":
                    driver.find_element_by_xpath("//div[@id='os1632']/div[2]/span[2]").click()
                elif czxt == "Windows2008-未激活":
                    driver.find_element_by_xpath("//div[@id='os1632']/div[3]/span").click()
                sleep(2)
                if "北京" in gmlx:
                    driver.find_element_by_xpath("//div[@id='dq1632']/div[2]/span").click()
                elif "香港" in gmlx:
                    driver.find_element_by_xpath("//div[@id='dq1632']/div[3]/span").click()
                sleep(2)
                if "郑州" in gmlx:
                    if gmsc == "1m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(
                            u"333元/1个月")
                    elif gmsc == "6m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(
                            u"1699元/半年")
                    elif gmsc == "1y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(
                            u"2999元/1年")
                    elif gmsc == "2y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(
                            u"5700元/2年")
                    elif gmsc == "3y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(
                            u"8100元/3年")
                    elif gmsc == "5y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(
                            u"13000元/5年")

                elif "北京" in gmlx:
                    if gmsc == "1m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(
                            u"370元/1个月")
                    elif gmsc == "6m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(
                            u"1800元/半年")
                    elif gmsc == "1y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(
                            u"3399元/1年")
                    elif gmsc == "2y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(
                            u"6460元/2年")
                    elif gmsc == "3y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(
                            u"9180元/3年")
                    elif gmsc == "5y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(
                            u"15000元/5年")

                elif "香港" in gmlx:
                    if gmsc == "1m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(
                            u"318元/1个月")
                    elif gmsc == "3m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(u"880元/季度")
                    elif gmsc == "6m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(
                            u"1680元/半年")
                    elif gmsc == "1y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(
                            u"3199元/1年")
                    elif gmsc == "2y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(
                            u"6300元/2年")
                    elif gmsc == "3y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(
                            u"9400元/3年")
                    elif gmsc == "5y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(
                            u"15500元/5年")

                try:
                    driver.find_element_by_id("buy1632").click();
                except:
                    print "豪华型加入购物车"

            if "旗舰" in gmlx:
                print "选择为旗舰型"
                sleep(2)
                if czxt == "CentOS 6.7":
                    driver.find_element_by_xpath("//div[@id='os1633']/div[2]/span[2]").click()
                elif czxt == "Windows2008-未激活":
                    driver.find_element_by_xpath("//div[@id='os1633']/div[3]/span").click()
                sleep(2)
                if "北京" in gmlx:
                    driver.find_element_by_xpath("//div[@id='dq1633']/div[2]/span").click()
                sleep(2)
                if "郑州" in gmlx:
                    if gmsc == "1m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"444元/1个月")
                    elif gmsc == "6m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"2299元/半年")
                    elif gmsc == "1y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"3999元/1年")
                    elif gmsc == "2y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"7600元/2年")
                    elif gmsc == "3y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"10800元/3年")
                    elif gmsc == "5y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"17000元/5年")

                elif "北京" in gmlx:
                    if gmsc == "1m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"480元/1个月")
                    elif gmsc == "6m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"2300元/半年")
                    elif gmsc == "1y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"4399元/1年")
                    elif gmsc == "2y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"8360元/2年")
                    elif gmsc == "3y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"11880元/3年")
                    elif gmsc == "5y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"19500元/5年")

                try:
                    driver.find_element_by_id("buy1633").click();
                except:
                    print "旗舰型加入购物车"

            if "至尊" in gmlx:
                print "选择为至尊型"
                sleep(2)
                if czxt == "CentOS 6.":
                    driver.find_element_by_xpath("//div[@id='os1634']/div[2]/span[2]").click()
                elif czxt == "Windows2008-未激活":
                    driver.find_element_by_xpath("//div[@id='os1634']/div[3]/span").click()
                sleep(2)
                if "北京" in gmlx:
                    driver.find_element_by_xpath("//div[@id='dq1634']/div[2]/span").click()
                elif "香港" in gmlx:
                    driver.find_element_by_xpath("//div[@id='dq1634']/div[3]/span").click()
                sleep(2)
                if "郑州" in gmlx:
                    if gmsc == "1m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"333元/1个月")
                    elif gmsc == "6m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"1699元/半年")
                    elif gmsc == "1y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"2999元/1年")
                    elif gmsc == "2y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"5700元/2年")
                    elif gmsc == "3y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"8100元/3年")
                    elif gmsc == "5y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"13000元/5年")

                elif "北京" in gmlx:
                    if gmsc == "1m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"660元/1个月")
                    elif gmsc == "6m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"3200元/半年")
                    elif gmsc == "1y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"5999元/1年")
                    elif gmsc == "2y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"11400元/2年")
                    elif gmsc == "3y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"16200元/3年")
                    elif gmsc == "5y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"26000元/5年")


                elif "香港" in gmlx:
                    if gmsc == "1m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"428元/1个月")
                    elif gmsc == "3m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"1200元/半年")
                    elif gmsc == "6m":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"2200元/半年")
                    elif gmsc == "1y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"4199元/1年")
                    elif gmsc == "2y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"8200元/2年")
                    elif gmsc == "3y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"12200元/3年")
                    elif gmsc == "5y":
                        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(
                            u"20000元/5年")

                try:
                    driver.find_element_by_id("buy1634").click();
                except:
                    print "至尊型加入购物车"


#======================================================================================================



#                                            支付
#=========================================================================================================

    def zhifu(self,driver):
        #driver = webdriver.Firefox()
        #driver.find_element_by_link_text(u"去支付").click()
        #sleep(2)
        #driver.find_element_by_xpath("//button[@type='button']").click()
        #driver.find_element_by_xpath("(//button[@type='button'])[3]").click()


        #driver.find_element_by_xpath("html/body/div[2]/div/div[5]/div/div[2]/div[2]/a[2]").click
        sleep(1)
        driver.find_element_by_link_text("去支付").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
#=========================================================================================================




#                                            续费升级部分
#=========================================================================================================



    def xufeishengji(self,driver):
        #driver = webdriver.Firefox()
        ywbs = "1213081"
        gongneng = "升级"
        xfsc = "1"
        sjpz = "旗舰型"
        lb = "快云VPS"
        driver.get("https://mc.kuaiyun.cn/vps/list?vpsbb=2&istm=false")
        if "香港VPS" in lb:
            driver.find_element_by_link_text(u"香港VPS").click()
        elif lb == "云VPS":
            driver.find_element_by_link_text(u"云VPS").click()
        sleep(1)
        driver.find_element_by_xpath("html/body/div[3]/div[2]/div/div[3]/div[2]/form/div/input[3]").send_keys(ywbs)
        #driver.find_element_by_xpath(".//*[@id='searchForm']/input[3]").send_keys(ywbs)
        sleep(1)
        driver.find_element_by_xpath("(//input[@value=''])[3]").click()
        if gongneng != "业务服务码" and gongneng != "故障申报" and gongneng != "日志":
            driver.find_element_by_link_text(gongneng).click()
        else:
            driver.find_element_by_css_selector("span.selected-content.text-primary").click()
            driver.find_element_by_link_text(gongneng).click()


#                续费部分
#=========================


        if gongneng == "续费":
            driver.find_element_by_css_selector("input.bk-disk-input").clear()
            driver.find_element_by_css_selector("input.bk-disk-input").send_keys(xfsc)

            # driver.find_element_by_link_text(u"快云币").click()
            # driver.find_element_by_id("kyb_input").clear()
            # driver.find_element_by_id("kyb_input").send_keys("1")
            driver.find_element_by_id("quzhifu").click()
            driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
            driver.find_element_by_xpath("(//button[@type='button'])[2]").click()

#                 升级部分（快云vps）
#============================
        if gongneng == "升级":
            # 得到当前型号pz
            pz = ""
            if sjpz == "经济型":
                cpbh = "1631"
            elif sjpz == "豪华型":
                cpbh = "1632"
            elif sjpz == "旗舰型":
                cpbh = "1633"
            elif sjpz == "至尊型":
                cpbh = "1634"
            elif sjpz == "普及型":
                cpbh = "1630"
            sleep(3)
            pz = driver.find_elements_by_xpath("html/body/div[3]/div[2]/div/div[2]/table/tbody/tr/td[1]")
            print pz[0].get_attribute('innerHTML')
            pzh = pz[0].get_attribute('innerHTML')
            print pzh
            # pzh1=str(pzh)
            Select(driver.find_element_by_xpath("//select")).select_by_visible_text(pzh + "->" + sjpz)

            # driver.find_element_by_css_selector("option[value=\""+cpbh+"\"]").click()
            # sleep(10)
            # driver.find_element_by_link_text(u"快云币").click()
            # driver.find_element_by_id("kyb_input").clear()
            # driver.find_element_by_id("kyb_input").send_keys("9873")
            sleep(3)
            # driver.find_element_by_xpath("html/body/div[3]/div[2]/div/div[2]/div[4]/div/div[2]/div[1]/a[2]").click()
            driver.find_element_by_link_text(u"去支付").click()
            driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
            sleep(10)
            driver.find_element_by_xpath("(//button[@type='button'])[4]").click()


#===============================================================================================


#                                    转正


#================================================================================================
    def zhuanzheng(self, driver):
        # driver = webdriver.Firefox()
        ywbs = "1213110"
        gongneng = "转正"
        kyb="1"
        xfsc="6"
        lb = "快云VPS"
        driver.get("https://mc.kuaiyun.cn/vps/list?vpsbb=2&istm=false")
        if "香港VPS" in lb:
            driver.find_element_by_link_text(u"香港VPS").click()
        elif lb == "云VPS":
            driver.find_element_by_link_text(u"云VPS").click()
        sleep(1)
        driver.find_element_by_xpath("html/body/div[3]/div[2]/div/div[3]/div[2]/form/div/input[3]").send_keys(ywbs)
        # driver.find_element_by_xpath(".//*[@id='searchForm']/input[3]").send_keys(ywbs)
        sleep(1)
        driver.find_element_by_xpath("(//input[@value=''])[3]").click()

        driver.find_element_by_link_text(gongneng).click()

        sleep(2)
        #driver.find_element_by_css_selector("input.bk-disk-input").clear()
        driver.find_element_by_css_selector("input.bk-disk-input").send_keys(xfsc)
        driver.find_element_by_id("kyb_input").clear()
        driver.find_element_by_id("kyb_input").send_keys(kyb)
        driver.find_element_by_id("3").click()
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        sleep(3)
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()


#=======================================================================================================






#                                               临时增值


#=====================================================================================================

    def linshizengzhi(self, driver):
        # driver = webdriver.Firefox()
        ywbs = "1213110"
        gongneng = "临时增值"
        kyb = "1"
        xfsc = "2017-11-01"
        lb = "快云VPS"
        xuanze="硬盘"
        yplx=u"标准型"#硬盘类型   u"容量型"   u"标准型"    u"性能型"
        ypdx=7    #硬盘大小
        i=0
        daikuan="5"#所需升级带宽
        driver.get("https://mc.kuaiyun.cn/vps/list?vpsbb=2&istm=false")
        if "香港VPS" in lb:
            driver.find_element_by_link_text(u"香港VPS").click()
        elif lb == "云VPS":
            driver.find_element_by_link_text(u"云VPS").click()
        sleep(1)
        driver.find_element_by_xpath("html/body/div[3]/div[2]/div/div[3]/div[2]/form/div/input[3]").send_keys(ywbs)
        # driver.find_element_by_xpath(".//*[@id='searchForm']/input[3]").send_keys(ywbs)
        sleep(1)
        driver.find_element_by_xpath("(//input[@value=''])[3]").click()

        driver.find_element_by_link_text(gongneng).click()
#======================================

#硬盘
#=====================================

        if xuanze=="硬盘":
            #driver.find_element_by_xpath("html/body/div[2]/div[2]/div/div[2]/div[2]/table[3]/tbody/tr[3]/td[2]/input").send_keys(xfsc)
            tkMessageBox.showinfo(title='提示', message='请在10s内选择硬盘临时增值时间')
            sleep(10)
            Select(driver.find_element_by_css_selector("select.ky-input-reset")).select_by_visible_text(yplx)

            while i<ypdx:
                driver.find_element_by_css_selector("input.add").click()
                i=i+1
                print i
            print i
            driver.find_element_by_id("chk_kyb3").click()
            driver.find_element_by_xpath("(//input[@name='kyb_input'])[2]").clear()
            driver.find_element_by_xpath("(//input[@name='kyb_input'])[2]").send_keys(kyb)
            driver.find_element_by_xpath(u"(//a[contains(text(),'立即购买')])[2]").click()
            driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
            sleep(10)
            driver.find_element_by_xpath("(//button[@type='button'])[6]").click()

        elif xuanze=="带宽":
            tkMessageBox.showinfo(title='提示', message='请在10s内选择带宽临时增值时间')
            sleep(10)
            driver.find_element_by_xpath("html/body/div[2]/div[2]/div/div[2]/div[2]/table[3]/tbody/tr[4]/td[2]/input").send_keys(xfsc)
            try:
                Select(driver.find_element_by_xpath("//div[@id='cl-wrapper']/div[2]/div/div[2]/div[2]/table[3]/tbody/tr[4]/td[3]/div/select")).select_by_visible_text("1Mbps->"+daikuan+"Mbps")
            except:
                print "临时增值带宽"
            try:
                Select(driver.find_element_by_xpath("//div[@id='cl-wrapper']/div[2]/div/div[2]/div[2]/table[3]/tbody/tr[4]/td[3]/div/select")).select_by_visible_text("2Mbps->"+daikuan+"Mbps")
            except:
                print "临时增值带宽"
            try:
                Select(driver.find_element_by_xpath("//div[@id='cl-wrapper']/div[2]/div/div[2]/div[2]/table[3]/tbody/tr[4]/td[3]/div/select")).select_by_visible_text("3Mbps->"+daikuan+"Mbps")
            except:
                print "临时增值带宽"
            try:
                Select(driver.find_element_by_xpath("//div[@id='cl-wrapper']/div[2]/div/div[2]/div[2]/table[3]/tbody/tr[4]/td[3]/div/select")).select_by_visible_text("4Mbps->"+daikuan+"Mbps")
            except:
                print "临时增值带宽"
            try:
                Select(driver.find_element_by_xpath("//div[@id='cl-wrapper']/div[2]/div/div[2]/div[2]/table[3]/tbody/tr[4]/td[3]/div/select")).select_by_visible_text("5Mbps->"+daikuan+"Mbps")
            except:
                print "临时增值带宽"
            try:
                Select(driver.find_element_by_xpath("//div[@id='cl-wrapper']/div[2]/div/div[2]/div[2]/table[3]/tbody/tr[4]/td[3]/div/select")).select_by_visible_text("6Mbps->"+daikuan+"Mbps")
            except:
                print "临时增值带宽"
            try:
                Select(driver.find_element_by_xpath("//div[@id='cl-wrapper']/div[2]/div/div[2]/div[2]/table[3]/tbody/tr[4]/td[3]/div/select")).select_by_visible_text("7Mbps->"+daikuan+"Mbps")
            except:
                print "临时增值带宽"
            try:
                Select(driver.find_element_by_xpath("//div[@id='cl-wrapper']/div[2]/div/div[2]/div[2]/table[3]/tbody/tr[4]/td[3]/div/select")).select_by_visible_text("8Mbps->"+daikuan+"Mbps")
            except:
                print "临时增值带宽"
            try:
                Select(driver.find_element_by_xpath("//div[@id='cl-wrapper']/div[2]/div/div[2]/div[2]/table[3]/tbody/tr[4]/td[3]/div/select")).select_by_visible_text("9Mbps->"+daikuan+"Mbps")
            except:
                print "临时增值带宽"


            sleep(1)
            driver.find_element_by_id("chk_kyb4").click()
            sleep(1)
            driver.find_element_by_xpath("(//input[@name='kyb_input'])[3]").clear()
            driver.find_element_by_xpath("(//input[@name='kyb_input'])[3]").send_keys(kyb)
            driver.find_element_by_xpath(u"(//a[contains(text(),'立即购买')])[3]").click()
            driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
            sleep(5)
            driver.find_element_by_xpath("(//button[@type='button'])[6]").click()

        elif xuanze=="ip":
            tkMessageBox.showinfo(title='提示', message='请在10s内选择ip临时增值时间')
            sleep(10)
            #driver.find_element_by_xpath("html/body/div[2]/div[2]/div/div[2]/div[2]/table[3]/tbody/tr[2]/td[2]/input").send_keys(xfsc)
            driver.find_element_by_id("chk_kyb2").click()
            driver.find_element_by_xpath("(//input[@name='kyb_input'])[1]").clear()
            driver.find_element_by_xpath("(//input[@name='kyb_input'])[1]").send_keys(kyb)
            driver.find_element_by_xpath(u"(//a[contains(text(),'立即购买')])[1]").click()
            driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
            sleep(5)
            driver.find_element_by_xpath("(//button[@type='button'])[6]").click()

