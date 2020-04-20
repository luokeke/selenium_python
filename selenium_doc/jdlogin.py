#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/6 16:32
# @Author : liuhuiling
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lxml.html import etree
import re, requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
from PIL import Image
import math
import operator
from functools import reduce

class JD_login(object):

    def __init__(self):  # 初始化一些信息
        self.left = 38  # 定义一个左边的起点，京东的滑块大小是38.61*38.61且是挨着边的，我们稍微差一点没问题
        self.url = 'https://passport.jd.com/new/login.aspx?'#登录页面链接
        self.driver = webdriver.Chrome('chromedriver') #赋予操作谷歌浏览器权限
        self.driver.maximize_window()#浏览器最大化
        self.username = "15290419073"#提前设置登录名和密码
        self.password = "luokeke0011"

    def input_name_password(self):#访问登录页，并输入用户名和密码
        self.driver.get(self.url)
        sleep(2) #等待页面加载后输入用户名和密码
        self.driver.find_element_by_link_text("账户登录").click()
        self.driver.find_element_by_id("loginname").clear()
        self.driver.find_element_by_id("loginname").send_keys(self.username)
        self.driver.find_element_by_id("nloginpwd").clear()
        self.driver.find_element_by_id("nloginpwd").send_keys(self.password)

    def click_login_button(self):  # 点击登录按钮,出现验证码图片
        # 点击登录
        self.driver.find_element_by_id("loginsubmit").click()
        sleep(2)

    def get_geetest_image(self):  # 通过截图的方式获取带缺口验证码图片
        # 获取带缺口的图片 JDJRV-bigimg
        gapimg = self.driver.find_element_by_class_name('JDJRV-bigimg') #先根据class_name定位
        sleep(2)
        gapimg.screenshot(r'./JDJRV-bigimg.png')  # 将定位的区域截屏保存
    def image_contrast(self,img1): # 截屏获取的图片在图片库里比对，拿到全图
        # 这个是先通过ps获取京东所有的验证码全图，然后按278*108缩小得到比对图库，放到列表里
        list1 = ["new-code0.png", "new-code1.png", "new-code2.png", "new-code3.png", "new-code4.png", "new-code5.png",
                 "new-code6.png", "new-code7.png", "new-code8.png", "new-code9.png"]
        result_list = []
        image_list = []
        for img2 in list1:
            image1 = Image.open(img1)
            image2 = Image.open(img2)
            h1 = image1.histogram()
            h2 = image2.histogram()
            # 如果两张图片完全相等，则返回结果为浮点类型“0.0”，如果不相同则返回结果值越大。
            result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
            result_list.append(result)
            image_list.append(img2)
        for i in range(len(result_list)):
            if min(result_list) == result_list[i]:
                return image_list[i]

    def get_diff_location(self):  # 获取缺口图起点，找到缺口的左侧边界 在x方向上的位置
        img1 = "JDJRV-bigimg.png"
        img2 = self.image_contrast(img1)
        print(img2)
        captcha1 = Image.open(img1)
        captcha2 = Image.open(str(img2))
        # 判断两张图片各个位置的像素是否相同
        for x in range(38, captcha1.size[0]):  # 从左到右 x方向
            for y in range(1, captcha1.size[1]):  # 从上到下 y方向
                # 获取两张图片指定位置的像素点
                pixel1 = captcha1.load()[x, y]
                pixel2 = captcha2.load()[x, y]
                # 设置一个阈值 允许有误差
                threshold = 60
                # 彩色图 每个位置的像素点有三个通道
                if abs(pixel1[0] - pixel2[0]) > threshold and abs(pixel1[1] - pixel2[1]) > threshold and abs(
                        pixel1[2] - pixel2[2]) > threshold:
                    return x

    def move_slider(self, track):  # 移动滑块完成登录
        # 定位滑块JDJRV-bigimg
        self.driver.find_element_by_xpath(".//*[@id='JDJRV-wrap-loginsubmit']/div/div/div/div[2]/div[3]").click()
        button = self.driver.find_element_by_xpath(".//*[@id='JDJRV-wrap-loginsubmit']/div/div/div/div[2]/div[3]")
        # ActionChains(self.driver).drag_and_drop(button).perform()
        ActionChains(self.driver).click_and_hold(button).perform()
        sleep(0.5)
        ActionChains(self.driver).move_by_offset(xoffset=0.7 * track, yoffset=0).perform()
        sleep(0.5)
        ActionChains(self.driver).move_by_offset(xoffset=0.3 * track, yoffset=0).perform()
        sleep(0.5)
        ActionChains(self.driver).release().perform()  # 松开鼠标
    def mc(self):
        self.driver.get("https://home.jd.com/")
    def main(self):
        self.input_name_password()  # 输入用户名密码
        self.click_login_button()  # 点击登录
        self.get_geetest_image()  # 通过截图的方式获取两张验证码图片，一张带缺口一张不带缺口
        gap = self.get_diff_location()  # 计算缺口左起点位置 ， 获取缺口图起点，找到缺口的左侧边界 在x方向上的位置
        print(gap)
        self.move_slider(gap)  # 根据轨迹移动滑块完成登录
        sleep(5)
        currentPageUrl = self.driver.current_url
        if currentPageUrl == "https://www.jd.com/":
            self.mc()
        else:
            self.main()

if __name__ == "__main__":
    bilibiliSlider = JD_login()
    bilibiliSlider.main()

