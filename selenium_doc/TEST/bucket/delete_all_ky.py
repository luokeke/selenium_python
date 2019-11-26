# -*- coding: utf-8 -*-
from TEST.bucket.login import *
from selenium import webdriver
from time import sleep

'''
脚本作用 ：批量删除 第一个or指定  存储空间内文件（不包含文件夹），快云站
删除指定空间文件：需设定 i 为1 确保bucketname参数正确
'''
i = 0  # 1  批量删除指定存储空间下文件  0 批量删除第一个存储空间内文件
bucketname = u'u123'  #存储空间名称，可修改
login  = "luokeke"
password = 1

driver = webdriver.Firefox()
driver.delete_all_cookies()
driver.maximize_window()
# 进入存储空间
#前提：批量删除只能一次性删除30个文件，请确保空间内文件少于30个
login().Zzidc_login(driver,login,password)
sleep(3)
driver.get("http://storage.kuaiyun.cn/storage/listObjects?bucketName=sdfkja456")
sleep(3)
if i == 1:
    driver.find_element_by_link_text(bucketname).click()
elif i == 0:
    driver.find_element_by_partial_link_text(u"查看").click()
sleep(3)
driver.find_element_by_id("selectAllBucket").click()
sleep(3)
driver.find_element_by_link_text("批量删除").click()
sleep(2)
driver.find_element_by_xpath("html/body/div[13]/div[3]/div/button[1]").click()
sleep(2)