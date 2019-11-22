#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2017/11/14 10:16
from TEST.login import *

username = "luokeke"
password = "1"
ddbh = 1522834 #订单编号
sjkmm = 1 #数据库密码 字母、数字或下划线组成，长度6~32位
driver = webdriver.Firefox()
driver.delete_all_cookies()
driver.maximize_window()
Test_login().Zzidc_login(driver,username,password)
sleep(2)
driver.get("https://www.zzidc.com/database/buyRedis")
try:
    driver.find_element_by_xpath(".//*[@id='layui-layer1']/div[3]/a").click()
except:
    pass
sleep(3)
#输入订单编号
driver.find_element_by_xpath(".//*[@id='searchForm']/div[1]/input").clear()
driver.find_element_by_xpath(".//*[@id='searchForm']/div[1]/input").send_keys(ddbh)
sleep(2)
#查询
driver.find_element_by_xpath(".//*[@id='searchForm']/div[1]/a").click()
sleep(2)
#点击开通
driver.find_element_by_link_text("开通").click()
sleep(2)
#开通
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys(sjkmm)
sleep(1)
driver.find_element_by_id("password1").clear()
driver.find_element_by_id("password1").send_keys(sjkmm)
sleep(2)
driver.find_element_by_link_text("确定").click()
sleep(2)
#点掉开通成功提示
driver.find_element_by_xpath(".//*[@id='layui-layer1']/div[3]/a").click()
sleep(2)


class Open_redis():
    def Open_redis(self,driver,ddbh,sjkmm):
        #点掉发票提醒弹框
        try:
            driver.find_element_by_xpath(".//*[@id='layui-layer1']/div[3]/a").click()
        except:
            pass
        sleep(3)
        #输入订单编号
        driver.find_element_by_xpath(".//*[@id='searchForm']/div[1]/input").clear()
        driver.find_element_by_xpath(".//*[@id='searchForm']/div[1]/input").send_keys(ddbh)
        sleep(2)
        #查询
        driver.find_element_by_xpath(".//*[@id='searchForm']/div[1]/a").click()
        sleep(2)
        #点击开通
        driver.find_element_by_link_text("开通").click()
        sleep(2)
        #开通
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(sjkmm)
        sleep(1)
        driver.find_element_by_id("password1").clear()
        driver.find_element_by_id("password1").send_keys(sjkmm)
        sleep(2)
        driver.find_element_by_link_text("确定").click()
        sleep(2)
        #点掉开通成功提示
        driver.find_element_by_xpath(".//*[@id='layui-layer1']/div[3]/a").click()
        sleep(2)