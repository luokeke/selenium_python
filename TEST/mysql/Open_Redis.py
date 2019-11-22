#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2017/11/14 10:16
from TEST.search_orders import *
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
        # driver.find_element_by_name("conditionPage.queryCondition.logo").clear()
        # driver.find_element_by_name("conditionPage.queryCondition.logo").send_keys(ddbh)
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


# # ddbh = 1522351 #订单编号
# sjkmm = "123456zaqwsx"
# driver = webdriver.Firefox()
# driver.delete_all_cookies()
# driver.maximize_window()
# #引用登录脚本
# Login().user_login(driver,"http://mc.zzidc.com/order/list?s=total","luokeke","1")
# sleep(3)
# #引用搜索订单脚本
# Search_orders().search_orders(driver,"")
# sleep(2)
# Open_redis().Open_redis(driver,sjkmm)








# #点掉发票提醒弹框
# try:
#     driver.find_element_by_xpath(".//*[@id='layui-layer1']/div[3]/a").click()
# except:
#     pass
# #输入订单编号
# driver.find_element_by_name("conditionPage.queryCondition.logo").clear()
# driver.find_element_by_name("conditionPage.queryCondition.logo").send_keys(ddbh)
# sleep(2)
# #查询
# driver.find_element_by_xpath(".//*[@id='searchForm']/div[1]/a").click()
# sleep(2)
# #点击开通
# driver.find_element_by_link_text("开通").click()
# sleep(2)













