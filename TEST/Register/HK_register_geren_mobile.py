#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2017/12/19 14:30
#此脚本针对开通手机验证码的个人注册
from selenium import webdriver
from time import sleep
from pymysql import connect,cursors
#给使用到的部分参数赋值---需要提前设定好--
login = "luokeke420"
name = u"洛可四二零"
password = "ceshi2019"
shengfen = u"湖南省"
dishi = u"株洲市"
#dishi = u"a[title=\"北京市\"]"  #北京比较特殊
email = "luokeke420@zzidc.com"
mobile = '19900037420'
#获取浏览器操作权限，打开，清理缓存并最大化
driver = webdriver.Firefox()
driver.delete_all_cookies()
driver.maximize_window()
#打开景安站注册页面
#终端注册
driver.get("https://www.zzidc.hk/main/member/initRegister")
#渠道注册
#driver.get("https://www.zzidc.hk/main/member/initRegister")
#输入用户名
driver.implicitly_wait(3)
driver.find_element_by_name("tabmembers.login").click()
driver.find_element_by_name("tabmembers.login").clear()
driver.find_element_by_name("tabmembers.login").send_keys(login)
#选择用户类型--个人
driver.implicitly_wait(3)
driver.find_element_by_css_selector("i.reg-radio").click()
#输入个人用户姓名
driver.implicitly_wait(3)
driver.find_element_by_name("tabmembers.contactname").click()
driver.find_element_by_name("tabmembers.contactname").clear()
driver.find_element_by_name("tabmembers.contactname").send_keys(name)
#设置密码并确认密码
driver.implicitly_wait(3)
driver.find_element_by_name("passwd").click()
driver.find_element_by_name("passwd").clear()
driver.find_element_by_name("passwd").send_keys(password)
driver.find_element_by_name("passwd_check").click()
driver.find_element_by_name("passwd_check").clear()
driver.find_element_by_name("passwd_check").send_keys(password)
#设置地区
driver.implicitly_wait(3)
driver.find_element_by_css_selector("span.select-value").click()
driver.find_element_by_link_text(shengfen).click()
driver.find_element_by_xpath("//form[@id='register_form']/div[10]/div[2]/div[2]/div/span").click()
# driver.find_element_by_xpath(".//*[@id='register_form']/div[7]/div[2]/div[2]/div[1]/span").click()
driver.find_element_by_link_text(dishi).click()
#设置邮箱
driver.find_element_by_id("email").click()
driver.find_element_by_id("email").clear()
driver.find_element_by_id("email").send_keys(email)
#输入手机号（此处为手机验证码）
driver.find_element_by_id("mobile").click()
driver.find_element_by_id("mobile").clear()
driver.find_element_by_id("mobile").send_keys(mobile)
#此处需要快速手动输入图片验证码
# sleep(8)
#获取手机验证码,确认已发送
driver.find_element_by_link_text(u"获取短信验证码").click()
driver.find_element_by_link_text(u"确认").click()
#获取过手机验证码之后，需要快速手动输入最新图片验证吗
sleep(8)
#链接数据库，获取手机注册验证码
conn = connect(host="10.220.129.165", user="testteam", password="f5H9B56QTW3fd5KDLCefg3kHuKefeb7D", db="db_zzidc_hk",charset="utf8mb4", cursorclass = cursors.DictCursor)
#写sql查对应手机号的验证码
sql = "SELECT code FROM smsvalidation WHERE mobile = %s and ifused = 0;"
#执行sql，并把执行结果赋值给result（此结果为字典格式）
with conn.cursor() as cursor:
    cursor.execute(sql,mobile)
    result = cursor.fetchone()
conn.close()
#在结果字典里取出来code对应的数值。
sms = result['code']
print (sms,result)
#输入手机验证码
driver.find_element_by_name("smsCode").click()
driver.find_element_by_name("smsCode").clear()
driver.find_element_by_name("smsCode").send_keys(sms)
#提交注册
driver.find_element_by_link_text(u"同意协议并提交").click()