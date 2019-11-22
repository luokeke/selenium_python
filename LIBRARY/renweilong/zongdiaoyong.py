#!/usr/bin/env python
#coding=utf-8

from vps_part import *
from TEST.LIBRARY.jiaoben.denglu import *

reload(sys)
sys.setdefaultencoding('utf8')
driver = webdriver.Firefox()
denglu().usr_login(driver)
#vps().goumai(driver)
#vps().zhifu(driver)
vps().xufei(driver)
#vps().shengji(driver)
#vps().zhuanzheng(driver)
#vps().linshizengzhi(driver)
#vps().fuwuma(driver)
#vps().guzhangshenbao(driver)
#vps().rizhi(driver)
#fwq().goumai(driver)