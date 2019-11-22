# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Fapshenting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://ac.zzidc.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_fapshenting(self):
        driver = self.driver
        driver.get(self.base_url + "/cas/login?service=https%3A%2F%2Fmc.zzidc.com%2Fmember.action%3Bjsessionid%3D8DE9DAB193CD6AC16A2E6382BBE4E8C0")
        driver.find_element_by_css_selector("#loginform > div.login-name.mbottom16 > #username").clear()
        driver.find_element_by_css_selector("#loginform > div.login-name.mbottom16 > #username").send_keys("luokeke")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("1")
        driver.find_element_by_link_text(u"登    录").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'发票申请')])[2]").click()
        driver.find_element_by_id("famount").clear()
        driver.find_element_by_id("famount").send_keys("1")
        Select(driver.find_element_by_name("tabinvoice.fylbmc")).select_by_visible_text(u"机柜租用gggg")
        driver.find_element_by_name("tabinvoice.recipient").clear()
        driver.find_element_by_name("tabinvoice.recipient").send_keys(u"厉害")
        driver.find_element_by_name("tabinvoice.phoneno").clear()
        driver.find_element_by_name("tabinvoice.phoneno").send_keys("18538028895")
        Select(driver.find_element_by_id("shengid")).select_by_visible_text(u"北京市")
        Select(driver.find_element_by_id("shiid")).select_by_visible_text(u"北京市")
        Select(driver.find_element_by_id("xianid")).select_by_visible_text(u"东城区")
        driver.find_element_by_name("tabinvoice.postAddress").clear()
        driver.find_element_by_name("tabinvoice.postAddress").send_keys(u"东城区是都按三个都")
        driver.find_element_by_name("tabinvoice.postcode").clear()
        driver.find_element_by_name("tabinvoice.postcode").send_keys("450000")
        driver.find_element_by_id("idFile1").clear()
        driver.find_element_by_id("idFile1").send_keys(u"C:\\Users\\Administrator\\Pictures\\数字\\1A.jpg")
        driver.find_element_by_id("idFile2").clear()
        driver.find_element_by_id("idFile2").send_keys(u"C:\\Users\\Administrator\\Pictures\\数字\\2B.jpg")
        driver.find_element_by_link_text(u"确认").click()
        driver.find_element_by_css_selector("a.layui-layer-btn0").click()
    
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
