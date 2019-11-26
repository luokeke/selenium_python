# -*- coding: UTF-8 -*-
from time import sleep

# from TEST.login import *


class Cunchu():
    def __init__(self):
        # self.dirver = webdriver.Firefox()
        self.dirver.implicitly_wait(5)
        self.dirver.maximize_window()
        self.dirver.get("http://www.kuaiyun.cn")
    #luokeke用户登录
    def test_admin_login(self):
        username = 'luokeke'
        password = '1'
        url = "http://www.kuaiyun.cn"
        # Login().user_login(self.dirver,url,username,password)
        sleep(10)
        self.dirver.quit()
    #luokeke001用户登录
    def test_guest_login(self):
        username = 'luokeke001'
        password = '1'
        url = "http://www.kuaiyun.cn"
        # Login().user_login(self.dirver,url,username,password)
        sleep(10)
        self.dirver.quit()
# Cunchu().test_admin_login()
Cunchu().test_guest_login()