# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Buycloudtwo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.kuaiyun.cn/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_buycloudtwo(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("luokeke")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("1")
        driver.find_element_by_css_selector("input.kylogin-link.fsize16").click()
        driver.find_element_by_css_selector("a.nav-link").click()
        driver.find_element_by_link_text(u"立即购买").click()
        driver.find_element_by_link_text(u"快云服务器Ⅰ型").click()
        driver.find_element_by_xpath("(//button[@value='2'])[2]").click()
        driver.find_element_by_css_selector("button.right-btn-select").click()
        driver.find_element_by_xpath("(//button[@value='1'])[2]").click()
        driver.find_element_by_link_text(u"下一步选择时长与镜像").click()
        driver.find_element_by_xpath("//body/div[3]/div/div/ul/li[2]").click()
        driver.find_element_by_xpath("//input[@value='1']").click()
        driver.find_element_by_xpath("//input[@value='1']").click()
        driver.find_element_by_xpath("//input[@value='1']").clear()
        driver.find_element_by_xpath("//input[@value='1']").send_keys("12")
        driver.find_element_by_css_selector("cite").click()
        driver.find_element_by_link_text(u"win2012-R2-数据版-x64-未激活").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
