#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/29 17:33
# @Author : liuhuiling
from selenium import webdriver
driver =webdriver.Firefox()
'''
webdriver 中比较常用的操作元素的方法
 clear 清除元素的内容，如果可以的话
 send_keys 在元素上模拟按键输入
 click 单击元素
 submit 提交表单
WebElement 接口常用方法
size:返回元素的尺寸 
text:获取元素的文本 
get_attribute(name) 获得属性值 
is_displayed() 设置该元素是否用户可见,返回True /False 
'''
size = driver.find_element_by_id("kw").size
text = driver.find_element_by_id("cp").text
attribute = driver.find_element_by_id("kw").get_attribute('type')
result = driver.find_element_by_id("kw").is_displayed()