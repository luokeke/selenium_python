#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2017/11/14 14:32


from TEST.login.login_zuofei import *
class Redis():
    def buy_redis(self,url,username,password,driver,gmlx,gmsc):
        Login().user_login(driver,url,username,password)
        #选型号
        if gmlx == 1:
            driver.find_element_by_xpath(".//*[@id='pzul']/li[1]/a").click()
        elif gmlx == 2:
            driver.find_element_by_xpath(".//*[@id='pzul']/li[2]/a").click()
        elif gmlx == 3:
            driver.find_element_by_xpath(".//*[@id='pzul']/li[3]/a").click()
        elif gmlx == 4:
            driver.find_element_by_xpath(".//*[@id='pzul']/li[4]/a").click()
        sleep(2)
        #购买时长
        driver.find_element_by_id("timeinput").clear()
        driver.find_element_by_id("timeinput").send_keys(gmsc)
        sleep(2)
        #购买
        driver.find_element_by_id("buy").click()
        sleep(2)
        #支付
        driver.find_element_by_xpath("./html/body/div[2]/div/div[5]/div/div[2]/div[2]/a[2]").click()
        sleep(2)
        #确认支付
        driver.find_element_by_xpath(".//*[@id='layui-layer1']/div[3]/a[1]").click()
        sleep(2)
        #确认支付成功
        driver.find_element_by_xpath(".//*[@id='layui-layer3']/div[3]/a[1]").click()
        sleep(2)
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