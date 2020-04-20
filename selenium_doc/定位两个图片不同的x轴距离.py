#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/13 9:13
# @Author : liuhuiling
from PIL import Image
def get_diff_location():  # 获取缺口图起点，找到缺口的左侧边界 在x方向上的位置
    captcha1 = Image.open("JDJRV-bigimg.png")
    captcha2 = Image.open("code8.png")
    # captcha2 = Image.open("new-code8.png")
    left = 38
    for x in range(left, captcha1.size[0]):  # 从左到右 x方向
        for y in range(1,captcha1.size[1]):  # 从上到下 y方向
            pixel1 = captcha1.load()[x, y]
            pixel2 = captcha2.load()[x, y]
            threshold = 60
            # 彩色图 每个位置的像素点有三个通道
            if abs(pixel1[0] - pixel2[0]) > threshold and abs(pixel1[1] - pixel2[1]) > threshold and abs(
                    pixel1[2] - pixel2[2]) > threshold:
                return x


print(get_diff_location())
#
# from  selenium import  webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# usl = "https://passport.jd.com/uc/login?ltype=logout"
# driver.get(usl)
# driver.find_element_by_link_text("账户登录").click()
# driver.refresh()
# driver.refresh()
# currentPageUrl = driver.current_url
# print(currentPageUrl == usl )
