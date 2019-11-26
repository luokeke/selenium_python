# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

'''
脚本作用：根据用户名证件号码，审核用户实名认证信息。（也可会员编号，不建议用会员名称有重复。）
参数  idnumber  和 i  需要执行脚本前设置
'''

idnumber = "511702197404273798" #会员证件号码，需要根据实际情况修改
i = 1  #设置审核状态   1 成功   0 失败
driver = webdriver.Firefox()
driver.get("http://gl.zzidc.com/")
driver.maximize_window()
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("systemmaster")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("1")
driver.find_element_by_css_selector("button.list-btn").click()
driver.implicitly_wait(3)

#鼠标悬停到审核管理
above = driver.find_element_by_link_text(u"审核管理")
ActionChains(driver).move_to_element(above).perform()
#鼠标悬停到半价审核管理
above1 =driver.find_element_by_link_text(u"半价活动管理")
ActionChains(driver).move_to_element(above).perform()
#点击半价审核管理
driver.find_element_by_link_text(u"半价活动管理").click()
sleep(2)
# 根据证件号码查询出来要审核的用户
driver.find_element_by_xpath(".//*[@id='loginName']").send_keys(idnumber)
driver.find_element_by_xpath(".//*[@id='chaxun']").click()
#点击审核
driver.find_element_by_link_text(u"商务审核").click()
sleep(3)
#选择审核成功,再优化下
if i == 1 :
    # 选择审核成功
    driver.find_element_by_id("state_city").click()
    driver.find_element_by_xpath("//ul[@id='ul_memberType']/li[2]/span").click()
elif i == 0:
    # 选择审核失败
    driver.find_element_by_id("state_city").click()
    driver.find_element_by_xpath("//ul[@id='ul_memberType']/li[3]/span").click()
    driver.find_element_by_id("remark").send_keys("图片不清晰，请重新提供，实名认证审核不通过")
#点击确定
driver.find_element_by_id("mass").click()
# driver.find_element_by_xpath(".//*[@id='mass']").click()
