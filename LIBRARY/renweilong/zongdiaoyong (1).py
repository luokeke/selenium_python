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
from diaoyongbufen import *

import sys
reload(sys)
sys.setdefaultencoding('utf8')
driver = webdriver.Firefox()
diaoyongbufen().usr_login(driver)
#diaoyongbufen().goumai(driver)
#diaoyongbufen().zhifu(driver)
#diaoyongbufen().xufei(driver)
#diaoyongbufen().shengji(driver)
#diaoyongbufen().zhuanzheng(driver)
#diaoyongbufen().linshizengzhi(driver)
#diaoyongbufen().fuwuma(driver)
#diaoyongbufen().guzhangshenbao(driver)
#diaoyongbufen().rizhi(driver)
