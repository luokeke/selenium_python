#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2018/10/25 19:32 
#此脚本针对手机验证码注册的个人用户
from selenium import webdriver
from time import sleep
from pymysql import connect,cursors
#给使用到的部分参数赋值---需要提前设定好--
login = "luokeke422"
name = u"洛可四二二"
password = "ceshi2019"
shengfen = u"河南省"
dishi = u"信阳市"
#dishi = u"a[title=\"北京市\"]"  #北京比较特殊
email = "luokeke422@zzidc.com"
mobile = '19900037422'
shangwu =u"李跃华"
qudao = u"杨云会"
useshangwu = 3
'''1 指定商务 0 不指定商务 3 渠道经理'''
zhuceleixing = 15
# 11 终端首页注册 12 商务程新杰邀请终端注册chengxinjie  1
# 13 代理aicoco邀请终端注册，商务跟随代理 景安站没有 14 推广返佣邀请注册 15IDC推广返佣邀请注册
# 21 渠道注册

#获取浏览器操作权限，打开，清理缓存并最大化
driver = webdriver.Firefox()
driver.delete_all_cookies()
driver.maximize_window()
#打开景安站注册页面
if zhuceleixing == 11:
    # 1 终端首页注册
    driver.get("https://www.zzidc.com/main/member/initRegister")
elif zhuceleixing == 12:
    #12  商务程新杰邀请终端注册chengxinjie
    driver.get("https://www.kuaiyun.cn/chengxinjie.htm")
elif zhuceleixing == 14:
    #13 代理aicoco邀请终端注册，商务跟随代理 景安站没有
    #14 推广返佣luokeke01邀请注册
   driver.get("http://www.zzidc.com/index.action?pand=KzXp2P4zCAY=")
elif zhuceleixing == 15:
    #15IDC推广返佣邀请注册
   driver.get("")
elif zhuceleixing == 21:
    #渠道注册
    driver.get("https://www.zzidc.com/main/member/agentsInitRegister")
else :
    # 1 终端首页注册
    driver.get("https://www.zzidc.com/main/member/initRegister")

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
#设置地区省份
driver.implicitly_wait(3)
driver.find_element_by_css_selector("span.select-value").click()
driver.find_element_by_link_text(shengfen).click()
driver.implicitly_wait(3)
#设置地区地市
if zhuceleixing != 21:
    driver.find_element_by_xpath(".//*[@id='register_form']/div[10]/div[2]/div[2]/div[1]/span").click()
else :
    driver.find_element_by_xpath(".//*[@id='register_form']/div[7]/div[2]/div[2]/div[1]/span").click()
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
sleep(8)
#获取手机验证码,确认已发送
driver.find_element_by_link_text(u"获取短信验证码").click()
#获取过手机验证码之后，需要快速手动输入最新图片验证吗
sleep(8)
#链接数据库，获取手机注册验证码
conn = connect(host="10.220.129.249", user="testteam", password="f5H9B56QTW3fd5KDLCefg3kHuKefeb7D", db="zzidc_db",charset="utf8mb4", cursorclass = cursors.DictCursor)
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
while zhuceleixing != 21:
    if useshangwu ==0 or zhuceleixing == 12:
        # 选择咨询产品
        driver.find_element_by_xpath(".//*[@id='choosedproduct']").click()
        driver.find_element_by_link_text(u"域名、虚拟主机、vps、云服务器").click()
        sleep(3)
    elif useshangwu ==1 :
        # 选择咨询产品
        driver.find_element_by_xpath(".//*[@id='choosedproduct']").click()
        driver.find_element_by_link_text(u"域名、虚拟主机、vps、云服务器").click()
        #指定商务
        driver.find_element_by_id("showsale").clear()
        driver.find_element_by_id("showsale").send_keys(shangwu)
        sleep(3)
else :
    # 指定渠道经理
    driver.find_element_by_id("showsale").clear()
    driver.find_element_by_id("showsale").send_keys(qudao)
    sleep(3)
# if  zhuceleixing != 21 and useshangwu ==0:
#     # 选择咨询产品
#     driver.find_element_by_xpath(".//*[@id='choosedproduct']").click()
#     driver.find_element_by_link_text(u"域名、虚拟主机、vps、云服务器").click()
#     sleep(3)
# elif zhuceleixing != 21 and useshangwu ==1:
#     # 选择咨询产品
#     driver.find_element_by_xpath(".//*[@id='choosedproduct']").click()
#     driver.find_element_by_link_text(u"域名、虚拟主机、vps、云服务器").click()
#     driver.find_element_by_id("showsale").clear()
#     driver.find_element_by_id("showsale").send_keys(shangwu)
#     sleep(3)
# elif zhuceleixing == 21 and useshangwu == 3:
#     driver.find_element_by_id("showsale").clear()
#     driver.find_element_by_id("showsale").send_keys("杨云会")
#     # driver.find_element_by_id("showsale").click()
#     # driver.find_element_by_xpath(".//*[@id='register_form']/div[12]/div[2]/div/div/ul/li").click()

#提交注册
driver.find_element_by_link_text(u"同意协议并提交").click()