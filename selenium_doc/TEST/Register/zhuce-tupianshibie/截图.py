#-*- coding:UTF-8 -*-
from selenium import  webdriver
from time import sleep
#自动识别验证码模拟登陆，注意是自动
driver = webdriver.Firefox()
driver.delete_all_cookies()
driver.maximize_window()
driver.get("http://www.zzidc.com/main/member/initRegister")
driver.implicitly_wait(3)
# #整个页面截图
driver.save_screenshot("1wangye.png")
# #整个页面截图
driver.get_screenshot_as_file("1error_png.png")
#把图片验证码截图下来
brow = driver.find_element_by_id("p_registerValiImage")
brow.click()
sleep(3)
brow.screenshot("00test.png")
# driver.close()