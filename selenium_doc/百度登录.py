#coding=utf-8
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.maximize_window()
driver.delete_all_cookies()
#点击登录链接
sleep(2)
driver.find_element_by_xpath(".//*[@id='u1']/a[7]").click()
# driver.find_element_by_name("tj_login").click()
#通过二次定位找到用户名输入框
div=driver.find_element_by_xpath(".//*[@id='u1']/a[7]").find_element_by_id("TANGRAM__PSP_10__userName")
div.send_keys("18538028895")
#输入登录密码
driver.find_element_by_name("password").send_keys("18538028895..")
#点击登录
driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
driver.quit()