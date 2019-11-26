#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2017/11/22 9:49
import xlrd    ##需要先pip安装xlfd模块，安装方法pip install xlrd
from time import sleep

#从excel文件读取用户名和密码+参数化+
# data = xlrd.open_workbook('F:\python\TEST\lo.xlsx')
# table = data.sheets()[0]  #读取第0个表格
# login = table.cell(1, 0).value##读取第1行0列（从0开始计数的）
# password = table.cell(1, 1).value##读取第1行1列（从0开始计数的）
# url = table.cell(1, 2).value  ##读取第1行2列（从0开始计数的）

#参数固定，方便调试
# login = "luokeke00.00"
# password = "luokeke00.00"
# url = "http://www.zzidc.com"

#创建一个Login类
class Login_shiyan():
    # 登录景安站
    def Zzidc_login(self,driver,login,password):
        driver.get("http://www.zzidc.com")
        sleep(3)
        driver.find_element_by_link_text("登录").click()
        sleep(3)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        sleep(3)
        driver.find_element_by_css_selector("#loginform > div.login-name.mbottom16 > #username").clear()
        driver.find_element_by_css_selector("#loginform > div.login-name.mbottom16 > #username").send_keys(login)
        sleep(3)
        #点击登录按钮
        driver.find_element_by_xpath(".//*[@id='loginform']/div[3]/a").click()
        sleep(3)
    # 登录快云站
    def Ky_login(self,driver,login,password):
        driver.get("http://www.kuaiyun.cn")
        sleep(3)
        driver.find_element_by_link_text(u"登录").click()
        sleep(3)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(login)
        sleep(3)
        driver.find_element_by_css_selector("input.kylogin-link.fsize16").click()
        sleep(3)
    def Gl_login(self,driver):
        driver.get("http://gl.zzidc.com")
        sleep(3)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("1")
        sleep(3)
        driver.find_element_by_css_selector(
            "#loginform > div.login-name.mbottom16 > #username").clear()
        driver.find_element_by_css_selector(
            "#loginform > div.login-name.mbottom16 > #username").send_keys("systemmaster")
        sleep(3)
        # 点击登录按钮
        driver.find_element_by_xpath(".//*[@id='loginform']/div[3]/a").click()
        sleep(3)

# driver = webdriver.Firefox()
# Login().Zzidc_login(driver,"luokeke","1")