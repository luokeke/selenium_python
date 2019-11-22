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
from vps_part import *
from denglu import *
from fwq_part import *
import sys
reload(sys)
sys.setdefaultencoding('utf8')

ceshigongneng=""
dengluexcel='F:\\flie\\denglu.xls'
vpsexcel= 'F:\\flie\\vps.xls'



driver = webdriver.Firefox()
denglu().usr_login(driver,denglufile=dengluexcel)#单元格为：账号（0.0）密码（1.0）
if "vps购买" in ceshigongneng:
    vps().goumai(driver,vpsfile = vpsexcel)
if "支付" in ceshigongneng:
    vps().zhifu(driver,vpsfile = vpsexcel)
if "vps续费" in ceshigongneng:
    vps().xufei(driver,vpsfile = vpsexcel)
if "vps升级" in ceshigongneng:
    vps().shengji(driver,vpsfile = vpsexcel)
if "vps转正" in ceshigongneng:
    vps().zhuanzheng(driver,vpsfile = vpsexcel)
if "vps临时增值" in ceshigongneng:
    vps().linshizengzhi(driver,vpsfile = vpsexcel)
if "vps服务码" in ceshigongneng:
    vps().fuwuma(driver,vpsfile = vpsexcel)
if "vps故障申报" in ceshigongneng:
    vps().guzhangshenbao(driver,vpsfile = vpsexcel)
if "vps日志" in ceshigongneng:
    vps().rizhi(driver,vpsfile = vpsexcel)
#fwq().goumai(driver)