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
from excel import *

class denglu():
#                                  登录
#============================================================
    def usr_login(self,driver):
        #driver = webdriver.Firefox()
        denglufile='F:\\flie\\denglu.xls'
        login = open_excel(file=denglufile,a=0,b=0)
        password =open_excel(file=denglufile,a=1,b=0)
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
