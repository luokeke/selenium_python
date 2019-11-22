#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2017/11/14 15:15 

from TEST.login.login_zuofei import *
from TEST.mysql.database.buy_redis import *

gmlx = 2 # 1入门型 2进阶型 3通用型 4高速型
gmsc = 2  #0-36 整数
ddbh = 1522351 #订单编号
sjkmm = "123456zaqwsx"

driver = webdriver.Firefox()
driver.delete_all_cookies()
driver.maximize_window()
Login().user_login(driver,"http://ac.zzidc.com/cas/login?service=https%3A%2F%2Fwww.zzidc.com%2Fdatabase%2FbuyRedis","luokeke","1")
sleep(2)
Buy_redis().buy_redis(driver,gmlx,gmsc)