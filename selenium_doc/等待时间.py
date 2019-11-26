#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/29 17:52
# @Author : liuhuiling
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
'''
三种等待时间：
sleep() 强制等待，设置固定休眠时间
implicitly_wait() 智能等待，隐性等待，超时等待，如果超出设置时间则抛出异常
WebDriverWait() 智能等待，显性等待，在设置时间内，默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间检测不到则抛出异常
WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
driver - WebDriver 的驱动程序(Ie, Firefox, Chrome 或远程)
timeout - 最长超时时间，默认以秒为单位
poll_frequency - 休眠时间的间隔（步长）时间，默认为 0.5 秒
ignored_exceptions - 超时后的异常信息，默认情况下抛 NoSuchElementException 异常。
WebDriverWai()一般由 unit()或 until_not()方法配合使用，下面是 unit()和 until_not()方法的说明
until(method, message=’ ’) until_not(method, message=’ ’)
'''
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
#固定休眠时间,两种方式
import time
time.sleep(6)
from time import sleep
sleep(3)
#智能等待，隐性等待
driver.implicitly_wait(3)
driver.find_element_by_id("su").click()
'''智能等待有两种，需要研究下'''
# 智能等待，显性等待，WebDriverWait()方法使用
from selenium.webdriver.support.ui import WebDriverWait
element = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_id("kw"))
#这个需要再研究下
element = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).until_not(lambda x: x.find_element_by_id("someId").is_displayed())
#另外一种    两种区别研究下
from selenium.webdriver.support import wait
wait.until(lambda driver: driver.find_element_by_id('dialog-iframe-search'))




