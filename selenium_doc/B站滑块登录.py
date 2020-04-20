#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/12 11:39
# @Author : liuhuiling
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from lxml.html import etree
from PIL import Image
from time import sleep
import re, requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

class B_login(object):
    def __init__(self):  # 初始化一些信息
        self.left = 60  # 定义一个左边的起点 缺口一般离图片左侧有一定的距离 有一个滑块
        self.url = 'https://passport.bilibili.com/login'
        self.driver = webdriver.Chrome('chromedriver')
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)  # 设置等待
        self.username = "18538028895"
        self.password = "aibilibili2015"

    def input_name_password(self):  # 输入用户名和密码
        self.driver.get(self.url)
        self.user = self.wait.until(EC.presence_of_element_located((By.ID, 'login-username')))
        self.passwd = self.wait.until(EC.presence_of_element_located((By.ID, 'login-passwd')))
        self.user.send_keys(self.username)
        self.passwd.send_keys(self.password)

    def click_login_button(self):  # 点击登录按钮,出现验证码图片
        login_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-login')))
        login_button.click()
        sleep(1)
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_refresh_1'))).click()
        sleep(1)
    #以下是获取图片验证码计算滑块移动距离代码
    def get_geetest_image(self):    # 通过截图的方式获取两张验证码图片，一张带缺口一张不带缺口
        # print(self.driver.page_source)
        #获取带缺口的图片1 geetest_canvas_bg
        gapimg = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_bg')))
        # sleep(2)
        gapimg.screenshot(r'./captcha1.png')  # 将class为geetest_canvas_bg的区域截屏保存
        # 通过js代码修改标签样式 显示图片2并截图  geetest_canvas_fullbg
        js = 'var change = document.getElementsByClassName("geetest_canvas_fullbg");change[0].style = "display:block;"'
        self.driver.execute_script(js)
        # sleep(2)
        fullimg = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_fullbg')))
        fullimg.screenshot(r'./captcha2.png')  # 将class为geetest_canvas_fullbg的区域截屏保存

    def is_similar(self, image1, image2, x, y):     #判断两张图片，各个位置的像素是否相同
        '''判断两张图片 各个位置的像素是否相同
        #image1:带缺口的图片
        :param image2: 不带缺口的图片
        :param x: 位置x
        :param y: 位置y
        :return: (x,y)位置的像素是否相同
        '''
        # 获取两张图片指定位置的像素点
        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]
        # 设置一个阈值 允许有误差
        threshold = 60
        # 彩色图 每个位置的像素点有三个通道
        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(
                pixel1[2] - pixel2[2]) < threshold:
            return True
        else:
            return False

    def get_diff_location(self):  # 获取缺口图起点，找到缺口的左侧边界 在x方向上的位置
        captcha1 = Image.open('captcha1.png')
        captcha2 = Image.open('captcha2.png')
        for x in range(self.left, captcha1.size[0]):  # 从左到右 x方向
            for y in range(captcha1.size[1]):  # 从上到下 y方向
                if not self.is_similar(captcha1, captcha2, x, y):
                    return x  # 找到缺口的左侧边界 在x方向上的位置

    def move_slider(self, track):# 移动滑块完成登录
        slider = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.geetest_slider_button')))
        ActionChains(self.driver).click_and_hold(slider).perform()
        sleep(0.5)
        ActionChains(self.driver).move_by_offset(xoffset=0.70*track, yoffset=0).perform()
        sleep(0.5)
        ActionChains(self.driver).move_by_offset(xoffset=0.30*track, yoffset=0).perform()
        sleep(0.5)
        ActionChains(self.driver).release().perform()  # 松开鼠标

    def main(self):
        self.input_name_password()#输入用户名密码
        self.click_login_button()#点击登录
        self.get_geetest_image()# 通过截图的方式获取两张验证码图片，一张带缺口一张不带缺口
        gap = self.get_diff_location()  # 计算缺口左起点位置 ， 获取缺口图起点，找到缺口的左侧边界 在x方向上的位置
        gap = gap - 8  # 减去滑块左侧距离图片左侧在x方向上的距离 即为滑块实际要移动的距离
        self.move_slider(gap)# 根据轨迹移动滑块完成登录

if __name__ == "__main__":
    bilibiliSlider = B_login()
    bilibiliSlider.main()
