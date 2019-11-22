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
import sys

reload(sys)

sys.setdefaultencoding('utf8')


driver = webdriver.Firefox()


login=u"wyf.mir"
password=u"1"
ywbs="1213081"
gongneng="升级"
xfsc="1"
sjpz="旗舰型"

driver.get("https://www.kuaiyun.cn")
driver.maximize_window()


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


usr_login(driver)

driver.get("https://mc.kuaiyun.cn/vps/list?vpsbb=2&istm=false")

driver.find_element_by_xpath(".//*[@id='searchForm']/input[3]").send_keys(ywbs)
sleep(1)
driver.find_element_by_xpath("(//input[@value=''])[3]").click()
if gongneng!="业务服务码" and gongneng!="故障申报" and gongneng!="日志":
    driver.find_element_by_link_text(gongneng).click()
else:
    driver.find_element_by_css_selector("span.selected-content.text-primary").click()
    driver.find_element_by_link_text(gongneng).click()

#==============================================================================================================
if gongneng=="续费":
    driver.find_element_by_css_selector("input.bk-disk-input").clear()
    driver.find_element_by_css_selector("input.bk-disk-input").send_keys(xfsc)

    #driver.find_element_by_link_text(u"快云币").click()
    #driver.find_element_by_id("kyb_input").clear()
    #driver.find_element_by_id("kyb_input").send_keys("1")
    driver.find_element_by_id("quzhifu").click()
    driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
    driver.find_element_by_xpath("(//button[@type='button'])[2]").click()














#=================================================================================================================
if gongneng=="升级":
    #得到当前型号pz
    pz=""
    if sjpz=="经济型":
        cpbh="1631"
    elif sjpz=="豪华型":
        cpbh="1632"
    elif sjpz == "旗舰型":
        cpbh = "1633"
    elif sjpz=="至尊型":
        cpbh="1634"
    elif sjpz=="普及型":
        cpbh="1630"
    sleep(3)
    pz = driver.find_elements_by_xpath("html/body/div[3]/div[2]/div/div[2]/table/tbody/tr/td[1]")
    print pz[0].get_attribute('innerHTML')
    pzh = pz[0].get_attribute('innerHTML')
    print pzh
    #pzh1=str(pzh)
    Select(driver.find_element_by_xpath("//select")).select_by_visible_text(pzh+"->"+sjpz)

    #driver.find_element_by_css_selector("option[value=\""+cpbh+"\"]").click()
    #sleep(10)
    #driver.find_element_by_link_text(u"快云币").click()
    #driver.find_element_by_id("kyb_input").clear()
    #driver.find_element_by_id("kyb_input").send_keys("9873")
    sleep(3)
    #driver.find_element_by_xpath("html/body/div[3]/div[2]/div/div[2]/div[4]/div/div[2]/div[1]/a[2]").click()
    driver.find_element_by_link_text(u"去支付").click()
    driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
    sleep(10)
    driver.find_element_by_xpath("(//button[@type='button'])[4]").click()