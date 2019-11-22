# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class mianfei(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.zzidc.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("luokeke")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("1")
        driver.find_element_by_css_selector("button.list-btn").click()
        driver.find_element_by_xpath("//li[5]/div/div/div/div/ul/li/a/h5").click()
        driver.find_element_by_css_selector("cite[name=\"citeP\"]").click()
        driver.find_element_by_link_text(u"0元/5年").click()
        driver.find_element_by_link_text(u"立即购买").click()
        driver.find_element_by_link_text(u"去支付").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
    
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
