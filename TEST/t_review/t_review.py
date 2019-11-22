#-*- coding:UTF-8 -*-
from time import sleep
from TEST.login import *
from selenium import webdriver
'''
执行此脚本前请先确定账号类型：个人 or 企业，之后设置需要的参数。
如果需要清理掉账号实名认证记录，可以执行clear_jl.py 脚本清理。
'''

member_type = 1 # 1 个人认证 2 #企业认证
#个人和企业相同的参数
diqu = u"港澳" #选择地区，u"大陆" u"港澳"   u"台湾"  u"海外"
email = "jingan02@zzidc.com" #邮箱，可以修改
login = u"jingan02"
password = u"ceshi2015"
path1 =  "C:\\Users\\Administrator\\Pictures\\1A.jpg"
path2 =  "C:\\Users\\Administrator\\Pictures\\1A.jpg"
#可先执行 panduan.py脚本确认用户账号类型。再来修改member_type值
if member_type == 1:
    idnum = '511702197404273798'  # 个人身份证件号，可以修改。
    reviewname = u"景安个人二"  # 个人名称，可以修改
elif member_type == 2:
    idnum = '54648798945S656D4-7'  # 公司营业执照号码，可以修改。
    reviewname = u"神马集团有限公司"  # 公司名称，可以修改

#账号实名认证  景安站
driver = webdriver.Firefox()
driver.maximize_window()
driver.delete_all_cookies()
#登录景安会员中心,直接进入实名认证界面
login().Zzidc_login(driver,"http://mc.zzidc.com/auth/torealname",login,password)
sleep(3)
driver.implicitly_wait(3)
#输入实名认证信息
#选择地区
driver.find_element_by_link_text(diqu).click()
sleep(1)
driver.find_element_by_name("businessName").clear()
driver.find_element_by_name("businessName").send_keys(reviewname)
sleep(1)
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys(email)
sleep(1)
driver.find_element_by_name("buslicenseCode").clear()
driver.find_element_by_name("buslicenseCode").send_keys(idnum)
#上传实名认证图片，使用send_keys方式
driver.implicitly_wait(3)
driver.find_element_by_id("idFile").clear()
driver.find_element_by_id("idFile").send_keys(path1)#图片路径可以修改
#个人多一张身份证背面图片
try:
    sleep(1)
    driver.find_element_by_id("idFile3").send_keys(path2)
except:
    pass
#提交实名认证信息
driver.implicitly_wait(3)
driver.find_element_by_link_text(u"下一步").click()
#信息确认
driver.implicitly_wait(3)
driver.find_element_by_link_text(u"确认").click()
#提交成功
sleep(2)
driver.find_element_by_link_text(u"确认").click()

