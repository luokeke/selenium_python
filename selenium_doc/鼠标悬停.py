#!/usr/bin/env python
#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
driver = webdriver.Firefox()
driver.delete_all_cookies()

above = driver.find_element_by_xpath(".//*[@id='J_common_header_menu']/li[2]/span")
ActionChains(driver).move_to_element(above).perform()

