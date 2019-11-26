#-*- coding:UTF-8 -*-

from lib2to3.pgen2 import driver
from  selenium import webdriver
import xlrd    ##需要先pip安装xlfd模块，安装方法pip install xlrd
from time import sleep
#从excel文件读取用户名和密码+参数化+
data = xlrd.open_workbook('F:\python\TEST\lo.xlsx')
table = data.sheets()[0]  #读取第0个表格
username = table.cell(1, 0).value##读取第1行0列（从0开始计数的）
password = table.cell(1, 1).value##读取第1行1列（从0开始计数的）
url = table.cell(1, 2).value  ##读取第1行2列（从0开始计数的）

url1 = [ "http://www.zzidc.com", "http://beta.zzidc.com","http://www.kuaiyun.cn"]
#参数固定，方便调试
# username = "luokeke00.00"
# password = "luokeke00.00"
# url = "http://www.zzidc.com"

#创建一个Login类
class Login_zuofei():
    # 创建登录函数，封装登录，参数化
    def login(self, driver):
        # 获取需要访问的url
        driver.get(url)
        driver.implicitly_wait(3)
        # 判断url是否直接是登录页面，是就直接走下去，不是就点击下登录，都不是就输出url不正确提示
        if url in url1:
            driver.find_element_by_link_text("登录").click()
        else:
            pass
        # 在登录页面输入用户名和密码
        driver.find_element_by_id("username").send_keys(username)
        driver.implicitly_wait(3)  # 如果元素存在立即执行，如果不存在就等三秒
        driver.find_element_by_id("password").send_keys(password)
        driver.implicitly_wait(3)
        driver.find_element_by_id("username").clear()
        driver.implicitly_wait(3)
        driver.find_element_by_id("username").send_keys(username)
        driver.implicitly_wait(3)
        # 点击登录按钮，因为快云站和景安站点登录方式不一样，写了try尝试。
        try:
            driver.find_element_by_id("login-loginok").click()
            driver.implicitly_wait(3)
        except:
            driver.find_element_by_xpath(".//*[@id='loginform']/div[3]/a").click()
            # driver.find_element_by_xpath(".//*[@id='login-form']/div[5]/input").click()
            driver.implicitly_wait(3)
    # 创建登录函数，调用时给参数赋值
    def user_login(self,driver,url,username,password):
        driver.get(url)
        driver.implicitly_wait(3)
        # 判断url是否直接是登录页面，是就直接走下去，不是就点击下登录，都不是就输出url不正确提示
        if url in url1:
            driver.find_element_by_link_text("登录").click()
        else:
            pass
        # 在登录页面输入用户名和密码
        driver.find_element_by_id("username").send_keys(username)
        driver.implicitly_wait(3)  # 如果元素存在立即执行，如果不存在就等三秒
        driver.find_element_by_id("password").send_keys(password)
        driver.implicitly_wait(3)
        driver.find_element_by_id("username").clear()
        driver.implicitly_wait(3)
        driver.find_element_by_id("username").send_keys(username)
        driver.implicitly_wait(3)
        # 点击登录按钮，因为快云站和景安站点登录方式不一样，写了try尝试。
        try:
            driver.find_element_by_id("login-loginok").click()
            driver.implicitly_wait(3)
        except:
            # sleep(2)
            # driver.find_element_by_xpath(".//*[@id='login-form']/div[5]/input").click()
            driver.find_element_by_xpath(".//*[@id='loginform']/div[3]/a").click()
            driver.implicitly_wait(3)
