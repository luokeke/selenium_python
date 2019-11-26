#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2017/12/19 14:30

#此脚本针对开通邮箱验证码的个人注册

from selenium import webdriver
from time import sleep
from pymysql import connect,cursors

#给使用到的部分参数赋值---需要提前设定好--
login = "luokeke405"
name = u"洛可四零五"
password = "ceshi2019"
shengfen = u"河南省"
dishi = u"济源市"
email = "luokeke405@zzidc.com"
mobile = '19913837405'


#获取浏览器操作权限，打开，清理缓存并最大化
driver = webdriver.Firefox()
driver.delete_all_cookies()
driver.maximize_window()
#打开景安站注册页面
# driver.get("http://www.zzidc.com/main/member/initRegister")
driver.get("https://www.zzidc.com/main/member/agentsInitRegister")
# driver.get("https://www.zzidc.hk/main/member/initRegister")
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
driver.implicitly_wait(3)
driver.find_element_by_xpath(".//*[@id='register_form']/div[7]/div[2]/div[2]/div[1]/span").click()
driver.find_element_by_link_text(dishi).click()
#输入手机号
driver.find_element_by_id("mobile").click()
driver.find_element_by_id("mobile").clear()
driver.find_element_by_id("mobile").send_keys(mobile)
#设置邮箱（此处为邮箱验证码）
driver.find_element_by_id("email").click()
driver.find_element_by_id("email").clear()
driver.find_element_by_id("email").send_keys(email)

sleep(8)
#此处需要快速手动输入图片验证码
#获取手机验证码,确认已发送
driver.find_element_by_link_text(u"获取邮箱验证码").click()
driver.find_element_by_link_text(u"确认").click()
#获取过手机验证码之后，需要快速手动输入最新图片验证吗
sleep(8)
#获取手机注册验证码
#链接数据库
conn = connect(host="10.220.129.249", user="testteam", password="f5H9B56QTW3fd5KDLCefg3kHuKefeb7D", db="zzidc_db",charset="utf8mb4", cursorclass = cursors.DictCursor)
#写sql查对应手机号的验证码
sql = "SELECT code FROM smsvalidation WHERE email = %s and ifused = 0;"
#执行sql，并把执行结果赋值给result（此结果为字典格式）
with conn.cursor() as cursor:
    cursor.execute(sql,email)
    result = cursor.fetchone()
conn.close()
#在结果字典里取出来code对应的数值。
sms = result['code']
print (sms,result)

#输入手机验证码
driver.find_element_by_name("smsCode").click()
driver.find_element_by_name("smsCode").clear()
driver.find_element_by_name("smsCode").send_keys(sms)
#选择咨询产品
driver.find_element_by_xpath(".//*[@id='choosedproduct']").click()
driver.find_element_by_link_text(u"域名、虚拟主机、vps、云服务器").click()
#提交注册
driver.find_element_by_link_text(u"同意协议并提交").click()