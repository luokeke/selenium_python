#!/usr/bin/env python
#coding:utf-8

import os
import re
import cv2
import time
import random
import string
import urllib2
import base64
import colorsys
import pytesseract
import requests
import numpy as np
from PIL import Image
from selenium import webdriver

URL = 'http://www.kuaiyun.cn/kyunmember/kuaiyunregister'

class DataFactory(object):
    def __init__(self):
        self.strbuf = list(string.ascii_uppercase) + list(string.digits) + list(string.ascii_lowercase)
        self.last_names = [
            '赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
            '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
            '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
            '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
            '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
            '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
            '熊', '纪', '舒', '屈', '项', '祝', '董', '梁'
        ]
        self.first_names = [
            '修', '松', '善', '卫', '森', '祖', '云', '适', '铁', '博', '雷', '超', '琴', '良', '娜', '银', '康', '健', '财', '杰',
            '江', '顺', '秋', '浪', '凡', '雄', '升', '典', '莱', '含', '盛', '济', '蒙', '棋', '乾', '坤', '波', '涛', '辉', '胜'
        ]
        self.provinces = [
            '410000河南省', '430000湖南省', '450000广西壮族自治区', '460000海南省', '500000重庆市',
            '510000四川省', '520000贵州省', '530000云南省', '540000西藏自治区', '610000陕西省',
            '620000甘肃省', '630000青海省', '640000宁夏回族自治区', '650000新疆维吾尔自治区', '710000台湾省',
            '810000香港特别行政区', '440000广东省', '110000北京市', '420000湖北省', '120000天津市',
            '130000河北省', '140000山西省', '150000内蒙古自治区', '210000辽宁省', '220000吉林省',
            '230000黑龙江省', '310000上海市', '320000江苏省', '330000浙江省', '340000安徽省',
            '350000福建省', '360000江西省', '370000山东省', '820000澳门特别行政区'
        ]

    def chinesename(self):
        return self.last_names[random.randint(0, len(self.last_names)-1)] + self.first_names[random.randint(0, len(self.first_names) - 1)]

    def username(self):
        return ''.join(random.sample(self.strbuf, 8))

    def password(self, len):
        return ''.join(random.sample(self.strbuf, len))

    def province(self):
        return self.provinces[random.randint(0, len(self.provinces)-1)]

class Captcha(object):
    def __init__(self, img):
        self.img = img
        self.crop = 0

    def resize(self):
        image = cv2.imread(self.img)
        resize_image = cv2.resize(image, (160, 70), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(self.img, resize_image)

    def split_line(self):
        split = None
        thl = []
        derta = [0, 0, 0]
        tmp = 127
        while tmp != 67:
            thl.append(tmp)
            tmp = tmp - 1
        for th in thl:
            img = cv2.imread(self.img)
            rows, columns, alpha = img.shape
            ret, img = cv2.threshold(img, th, 255, cv2.THRESH_BINARY)
            split = []
            start = False
            for c in range(columns):
                for r in range(rows):
                    if not (img[r, c][0] == 255 and img[r, c][1] == 255 and img[r, c][2] == 255):
                        if start == False:
                            start = True
                        break

                    if start == True and r == rows - 1:
                        split.append(c)
                        start = False
            if len(split) >= 4:
                derta[0] = split[1] - split[0]
                derta[1] = split[2] - split[1]
                derta[2] = split[3] - split[2]
                if derta[0] >= 15 and derta[1] >= 15 and derta[2] >= 15:
                    break

        if derta[0] < 15 or derta[1] < 15 or derta[2] < 15:
            split = []
        return split

    def partition_decode(self, sx, ex, sy, ey):
        # crop image
        img = cv2.imread(self.img)
        crop = img[sy:ey, sx:ex]
        self.crop += 1
        slice = 'slice%s.png' % self.crop
        cv2.imwrite(slice, crop)
        cv2.imwrite('org_%s' % slice, crop)

        # domainant color
        img = Image.open(slice)
        img = img.convert('RGBA')
        img.thumbnail((200, 200))
        max_score = None
        dominant_color = None
        for count, (r, g, b, a) in img.getcolors(img.size[0] * img.size[1]):
            if a == 0:
                continue
            saturation = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)[1]
            y = min(abs(r * 2104 + g * 4130 + b * 802 + 4096 + 131072) >> 13, 235)
            y = (y - 16.0) / (235 - 16)
            if y > 0.9:
                continue

            score = (saturation + 0.1) * count
            if score > max_score:
                max_score = score
                dominant_color = (r, g, b)

        # reduce noise
        red, green, blue = dominant_color
        code_list = []
        for bias in [30, 25, 20, 15, 10, 5, 2]:  # [5, 10, 20, 30]:
            img = cv2.imread(slice)
            # bias = 15  # Do not modify this value by yourself, unless you know what you do
            w, h, ch = img.shape
            for i in range(w):
                for j in range(h):
                    if not (img[i, j][0] >= (blue - bias) and img[i, j][0] <= (blue + bias)):
                        img[i, j][0] = 255
                    if not (img[i, j][1] >= (green - bias) and img[i, j][1] <= (green + bias)):
                        img[i, j][1] = 255
                    if not (img[i, j][2] >= (red - bias) and img[i, j][2] <= (red + bias)):
                        img[i, j][2] = 255
            cv2.imwrite(slice, img)
            img = cv2.imread(slice)
            code = None
            for i in [13, 11, 9, 7, 5, 3, 1]:  # [9, 7, 5, 3, 1]:
                code = ''
                blur = cv2.GaussianBlur(img, (i, i), 0)
                cv2.imwrite(slice, blur)
                # decode
                try:
                    code = pytesseract.image_to_string(Image.open(slice))
                except Exception:
                    code = ''
                # print code
                if code.isalnum() and len(code) == 1:
                    code_list.append(code)

        # print code_list
        if len(code_list) >= 32 and set(['Q']).issubset(set(code_list[:32])):
            return 'Q'
        elif set(['6', '8']).issubset(set(code_list)):
            return 'B'
        elif set(['7', 'Y', 'I']).issubset(set(code_list)):
            return 'J'
        elif len(code_list):
            return code_list[0]
        else:
            return ''

    def decode(self):
        #self.resize()
        split = self.split_line()
        if split == None or len(split) < 4:
            return ''
        code1 = self.partition_decode(0, split[0], 0, 70)
        code2 = self.partition_decode(split[0], split[1], 0, 70)
        code3 = self.partition_decode(split[1], split[2], 0, 70)
        code4 = self.partition_decode(split[2], split[3], 0, 70)
        return '%s%s%s%s' % (code1, code2, code3, code4)

def save_elementshot(driver, element, path):
    location = element.location
    size = element.size
    driver.save_screenshot(path)
    image = Image.open(path)
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    image = image.crop((left, top, right, bottom))
    image.save(path, 'png')

def kuaiyun_register():
    driver = webdriver.Chrome()
    driver.get(URL)

    # username
    e_username = driver.find_element_by_xpath('//input[@placeholder=\'请设置您的会员登录账号\']')
    pp = e_username.find_element_by_xpath('..').find_element_by_xpath('..')
    username = DataFactory().username()
    while True:
        e_username.clear()
        e_username.send_keys(username)
        pp.find_element_by_class_name('kyregister-left').click()
        time.sleep(2)
        tips = pp.find_element_by_xpath('//span[@class=\'gf00\']').text
        if tips == u'通过信息验证！':
            break

    # chinesename
    e_chinesename = driver.find_element_by_xpath('//input[@placeholder=\'请填写您身份证上真实中文姓名\']')
    pp = e_chinesename.find_element_by_xpath('..').find_element_by_xpath('..')
    chinesename = DataFactory().chinesename()
    while True:
        e_chinesename.clear()
        e_chinesename.send_keys(chinesename.decode('utf-8'))
        pp.find_element_by_class_name('kyregister-left').click()
        time.sleep(2)
        tips = pp.find_element_by_xpath('//span[@class=\'gf00\']').text
        if tips == u'通过信息验证！':
            break

    # password
    e_password1 = driver.find_element_by_xpath('//input[@placeholder=\'设置您的登录密码\']')
    pp = e_password1.find_element_by_xpath('..').find_element_by_xpath('..')
    password = 'a1'.join(DataFactory().password(6))
    while True:
        e_password1.clear()
        e_password1.send_keys(password)
        pp.find_element_by_class_name('kyregister-left').click()
        time.sleep(2)
        tips = pp.find_element_by_xpath('//span[@class=\'gf00\']').text
        if tips == u'通过信息验证！':
            e_password2 = driver.find_element_by_xpath('//input[@placeholder=\'请再次输入您的密码\']')
            e_password2.send_keys(password)
            break

    # province and city
    e_province = driver.find_element_by_id('shengid')
    e_province.click()
    province = DataFactory().province()
    driver.find_element_by_xpath('//option[@value=\'%s\']' % province).click()
    time.sleep(2)
    e_city = driver.find_element_by_id('shiid')
    citys = []
    for item in e_city.find_elements_by_tag_name('option'):
        tmp =  item.get_property('value')
        if len(tmp):
            citys.append(tmp)
    e_city.click()
    city = citys[random.randint(0, len(citys)-1)]
    driver.find_element_by_xpath('//option[@value=\'%s\']' % city).click()
    time.sleep(2)

    # captcha
    e_captcha_input = driver.find_element_by_xpath('//input[@placeholder=\'请输入图片验证码\']')
    e_captcha_img = driver.find_element_by_id('p_registerValiImage')
    e_captcha_refresh = driver.find_element_by_id('shuaxin')
    t = driver.find_element_by_xpath('//input[@placeholder=\'请选择商务经理\']')
    e_captcha_input.click()
    t.click()
    time.sleep(2)
    e_captcha_tips = driver.find_element_by_xpath('//span[text()=\'请输入图片验证码\']')
    captcha_code = None
    while True:
        js = 'var q=document.getElementById(\"p_registerValiImage\");q.width=\"160\";q.height=\"70\";'
        driver.execute_script(js)
        save_elementshot(driver, e_captcha_img, 'captcha.png')
        js = 'var q=document.getElementById(\"p_registerValiImage\");q.width=\"80\";q.height=\"30\";'
        driver.execute_script(js)

        # encoded_string = ''
        # with open("captcha.png", "rb") as f:
        #     encoded_string = base64.b64encode(f.read())
        # js = 'var q=document.getElementById(\"p_registerValiImage\");q.src=\"data:image/png;base64,' + encoded_string + '\";'
        # driver.execute_script(js)

        captcha_code = Captcha('captcha.png').decode()
        if captcha_code != '':
            e_captcha_input.clear()
            t.click()
            time.sleep(2)
            e_captcha_input.send_keys(captcha_code)
            t.click()
            time.sleep(2)
            tips = e_captcha_tips.text
            print (captcha_code)
            print (tips)
            if tips == u'图像验证码通过验证':
                break
        e_captcha_refresh.click()
    # mobile phone number

    # check code

    # product

    # manager

    input('Press any key to stop: ')
    driver.quit()

if __name__ == '__main__':
    kuaiyun_register()
