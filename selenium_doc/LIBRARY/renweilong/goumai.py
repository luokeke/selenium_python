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
driver = webdriver.Firefox()
login=u"12212212224"
password=u"4429836q"
dlzt="1"#1为登录，0为不登录

driver.get("http://www.kuaiyun.cn/")
driver.maximize_window()
gmlx="vps经济型北京"#举例快云vps香港机房经济型,服务器郑州机房
#====================================================================================================================================
#vps参数
if "vps" in gmlx:
    gmsc="6m"#1m,1y月年
    czxt="CentOS 6.7"#	Windows2003,CentOS 6.7,Windows2008-未激活         使用时请复制后面三种类型


#====================================================================================================================================
#服务器参数
if "服务器" in gmlx:
    pz=""#1,2,3,4,5,自选
    gmsc=""
    czxt=""#windows,centos,debian,ubuntu
    #当为自选时，参数
    sjp=""#大小
    cpu=""#1,2,4,8,16
    nc=""#cpu为1时1,2,4,8,12；2时2,4,8,12,16；4时4,8，12，16，24；8时8,12，，16，24，32，16时12，16，24，32，64
    gwdk=""#1-100M
#====================================================================================================================================
#数据库
if "数据库" in gmlx:
    a=1

#====================================================================================================================================
#登录
#d定义登录函数
def usr_login(self):

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

if dlzt=="1":
    usr_login(driver)




    #driver.usr_login()
    print "1111111"

if "vps" in gmlx:
    #driver.find_element_by_css_selector("div.menu-dropdown-down-item.mtop26 > a.nav-link").click()
    driver.get("http://www.kuaiyun.cn/vps/kyvpsindex")
    #driver.find_element_by_xpath("//ul[@id='J_common_header_menu']/li[2]/div/div/div[2]/div/div/div[4]/a").click()



    if "基础" in gmlx:
        print "选择为基础型"
        sleep(2)
        if czxt=="CentOS 6.7":
            driver.find_element_by_xpath("//div[@id='os1629']/div[2]/span[2]").click()
        elif czxt == "Windows2008-未激活":
            driver.find_element_by_xpath("//div[@id='os1629']/div[3]/span").click()
        sleep(2)
        if gmsc=="1m":
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
        if czxt=="CentOS 6.7":
            driver.find_element_by_xpath("//div[@id='os1630']/div[2]/span[2]").click()
        elif czxt=="Windows2008-未激活":
            driver.find_element_by_xpath("//div[@id='os1630']/div[3]/span").click()
        sleep(2)
        if "北京" in gmlx:
            driver.find_element_by_xpath("//div[@id='dq1630']/div[2]/span").click()
        elif "香港" in gmlx:
            driver.find_element_by_xpath("//div[@id='dq1630']/div[3]/span").click()
        sleep(2)
        if gmsc=="1m":
            Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[2]")).select_by_visible_text(u"111元/1个月")
        elif gmsc=="6m":
            Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[2]")).select_by_visible_text(u"599元/半年")
        elif gmsc=="1y":
            Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[2]")).select_by_visible_text(u"999元/1年")
        elif gmsc=="2y":
            Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[2]")).select_by_visible_text(u"1900元/2年")
        elif gmsc == "3y":
            Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[2]")).select_by_visible_text(u"2700元/3年")
        elif gmsc == "5y":
            Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[2]")).select_by_visible_text(u"4400元/5年")

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
    if gmsc == "1m":
        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(u"222元/1个月")
    elif gmsc == "6m":
        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(u"1199元/半年")
    elif gmsc == "1y":
        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(u"1999元/1年")
    elif gmsc == "2y":
        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(u"3800元/2年")
    elif gmsc == "3y":
        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(u"5400元/3年")
    elif gmsc == "5y":
        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[3]")).select_by_visible_text(u"8800元/5年")
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
    if gmsc == "1m":
        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(u"333元/1个月")
    elif gmsc == "6m":
        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(u"1699元/半年")
    elif gmsc == "1y":
        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(u"2999元/1年")
    elif gmsc == "2y":
        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(u"5700元/2年")
    elif gmsc == "3y":
        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(u"8100元/3年")
    elif gmsc == "5y":
        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[4]")).select_by_visible_text(u"13000元/5年")
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
    if gmsc == "1m":
        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(u"444元/1个月")
    elif gmsc == "6m":
        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(u"2299元/半年")
    elif gmsc == "1y":
        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(u"3999元/1年")
    elif gmsc == "2y":
        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(u"7600元/2年")
    elif gmsc == "3y":
        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(u"10800元/3年")
    elif gmsc == "5y":
        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(u"17000元/5年")


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
    if gmsc == "1m":
        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(u"333元/1个月")
    elif gmsc == "6m":
        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(u"1699元/半年")
    elif gmsc == "1y":
        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(u"2999元/1年")
    elif gmsc == "2y":
        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(u"5700元/2年")
    elif gmsc == "3y":
        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(u"8100元/3年")
    elif gmsc == "5y":
        Select(driver.find_element_by_xpath("(//select[@id='gmqx'])[5]")).select_by_visible_text(u"13000元/5年")

    try:
        driver.find_element_by_id("buy1634").click();
    except:
        print "至尊型加入购物车"



#支付
driver.find_elements_by_xpath("html/body/div[2]/div/div[5]/div/div[2]/div[2]/a[2]").click()




























