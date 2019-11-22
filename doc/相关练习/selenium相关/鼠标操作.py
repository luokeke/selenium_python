#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/29 16:53
# @Author : liuhuiling
from selenium import webdriver
driver =webdriver.Firefox()
'''
webdriver 的  ActionChains() 类 提供鼠标操作的常用方法：
 context_click() 右击 
 double_click() 双击
 drag_and_drop() 拖动
 move_to_element() 鼠标悬停在一个元素上
 click_and_hold() 按下鼠标左键在一个元素上
'''
from selenium.webdriver.common.action_chains import ActionChains
element = driver.find_element_by_name("xxx")#定位到元素
#右击：
ActionChains(driver).context_click(element).perform()#对定位到的元素执行鼠标右键操作
#双击：
ActionChains(driver).double_click(element).perform()
# 拖动drag_and_drop(source, target)
# source: 鼠标按下的源元素。
# target: 鼠标释放的目标元素。
target = driver.find_element_by_name("xxx")
ActionChains(driver).drag_and_drop(element,target).perform()
#悬停
ActionChains(driver).move_to_element(element).perform()
#选中元素左击
ActionChains(driver).click_and_hold(element).perform()
'''
键盘事件   webdriver 的 Keys()类提供键盘上所有按键的操作，甚至可以模拟一些组合按键的操作，Ctrl+A/C/V
删除键 BACK_SPACE 空格键 SPACE 制表键 TAB 回退键 ESCAPE 回车键 ENTER 
全选 CONTROL,'a' 复制 CONTROL,'c'  剪切 CONTROL,'x' 粘贴 CONTROL,'v'
'''
from selenium.webdriver.common.keys import Keys
import time
driver.find_element_by_id("kw").send_keys("seleniumm")#输入框输入内容
time.sleep(3)#点击清除，删除最后输入的m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
time.sleep(3)#输入空格键+"教程"
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys("教程")
time.sleep(3)#ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(3)#ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(3)#ctrl+v  粘贴进入内容，搜索
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
time.sleep(3)#回车代替点击操作
driver.find_element_by_id("kw").send_keys(Keys.ENTER)
time.sleep(3)
driver.quit()
'''
打印信息
'''
#获取当前页面title并打印
title = driver.title
print(title)
#与预期title比较并输出结果
if title == u"快云":
    print("title ok!")
else:
    print("title on!")
#获取当前页面URL,打印
now_url = driver.current_url
#获得登录成功的用户，打印
now_user = driver.find_element_by_id("user").text
