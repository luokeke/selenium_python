#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2019/3/18 18:06 

from TEST.login01 import *

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