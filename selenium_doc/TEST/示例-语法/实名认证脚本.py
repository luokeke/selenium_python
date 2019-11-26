#-*- coding:UTF-8 -*-
import time

from selenium import webdriver

#公司账号实名认证
driver = webdriver.Firefox()
driver.maximize_window()
driver.delete_all_cookies()
#调用登录模块，访问景安站并登录
Login().login(driver,"http://www.zzidc.com","luokeke00.00","luokeke00.00")
#进入会员中心
driver.implicitly_wait(3)
driver.find_element_by_link_text(u"管理中心").click()
#进入实名认证界面
driver.implicitly_wait(3)
driver.find_element_by_xpath(u"(//a[contains(text(),'实名认证')])[2]").click()
#公司实名认证，输入公司信息
driver.implicitly_wait(3)
driver.find_element_by_name("businessName").clear()
driver.find_element_by_name("businessName").send_keys(u"斑斓本有限公司")
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("luokeke00.00@zzidc.com")
driver.find_element_by_name("buslicenseCode").clear()
driver.find_element_by_name("buslicenseCode").send_keys("luokeke00004654")
#上传图片
driver.implicitly_wait(3)
driver.find_element_by_id("idFile").clear()
driver.find_element_by_id("idFile").send_keys("C:\\Users\\Administrator\\Pictures\\834KB.JPG")
#提交实名认证信息
driver.implicitly_wait(3)
driver.find_element_by_link_text(u"下一步").click()
#信息确认
driver.implicitly_wait(3)
driver.find_element_by_link_text(u"确认").click()
#提交成功
time.sleep(2)
driver.find_element_by_link_text(u"确认").click()



