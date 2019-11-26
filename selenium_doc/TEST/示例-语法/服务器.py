#-*- coding:UTF-8 -*-
from selenium import webdriver
import xlrd,time
# from login import *
from selenium.webdriver.common.action_chains import ActionChains   #引入需要的包
#打开浏览器
driver = webdriver.Firefox()
time.sleep(2)
driver.get("http://www.kuaiyun.cn")
#调用登录函数，进行登录
#Login().login(driver)
driver.maximize_window()
time.sleep(2)
#进入到服务器产品页面，需要鼠标先指向产品，再指向计算，之后点击服务器产品。（涉及到鼠标事件里的鼠标悬停在一个元素上move_to_element()，需要先引入需要的第三方包吧 ）
#定位到产品按钮
above = driver.find_element_by_xpath(".//*[@id='J_common_header_menu']/li[2]/span")
#执行鼠标悬停命令，使鼠标悬停到产品按钮上，显示出来产品导航
ActionChains(driver).move_to_element(above).perform()
#定位到产品导航里的计算按钮
above1 = driver.find_element_by_xpath(".//*[@id='J_common_header_menu']/li[2]/div/div/div[1]/a[1]")
#执行鼠标悬停命令，使鼠标悬停到计算按钮上，显示出来计算下的产品导航
ActionChains(driver).move_to_element(above1).perform()
#点击计算下的产品导航上的服务器产品，进入服务器产品介绍页面
driver.find_element_by_xpath(".//*[@id='J_common_header_menu']/li[2]/div/div/div[2]/div[1]/div/div[1]/a").click()
time.sleep(2)
#在服务器介绍页面点击立即购买，跳转到服务器购买页面
driver.find_element_by_link_text(u"立即购买").click()
driver.implicitly_wait(3)
#选择产品类型，不动其他配置了
driver.find_element_by_link_text("快云服务器Ⅰ型").click()
#在购买页面点击下一步，跳转到选择购买时长和系统类型页面
driver.find_element_by_link_text(u"下一步选择时长与镜像").click()
#在选择购买时长和系统类型页面
#选择购买时间，这里选了一年
driver.find_element_by_xpath("//input[@value='1']").click()
driver.find_element_by_xpath("//input[@value='1']").clear()
driver.find_element_by_xpath("//input[@value='1']").send_keys("12")

# #选择操作系统，这里选择了Centos系统
# driver.find_element_by_link_text("CentOS").click()
# #点击选择系统版本
# driver.find_element_by_css_selector("cite").click()
# #选择系统具体版本
# driver.find_element_by_link_text("CentOS-7.2-x86_64").click()
# #点击立即购买
# driver.find_element_by_link_text(u"立即购买").click()







# driver.find_element_by_xpath("//body/div[3]/div/div/ul/li[2]").click()
# driver.find_element_by_css_selector("cite").click()
# time.sleep(3)
# driver.find_element_by_link_text(u"win2k12-R2-数据版-x64-未激活").click()
# time.sleep(3)
# driver.find_element_by_link_text(u"立即购买").click()
# time.sleep(3)
# driver.find_element_by_link_text(u"去支付").click()
# driver.find_element_by_xpath("//button[@type='button']").click()
# driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
# time.sleep(3)
# #开通
# driver.find_element_by_link_text(u"开通").click()
# time.sleep(3)
# driver.find_element_by_id("ydxy").click()
# time.sleep(3)
# driver.find_element_by_id("nextbutton").click()
# time.sleep(3)
# driver.find_element_by_id("choosext").click()
# time.sleep(3)
# Select(driver.find_element_by_id("choosext")).select_by_visible_text("CentOS")