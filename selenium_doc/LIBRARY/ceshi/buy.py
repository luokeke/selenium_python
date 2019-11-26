#!/usr/bin/env python
#-*- coding:utf8 -*-
#购买服务器
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
from time import  sleep
#购买服务器产品
class buy():
    def buy(self,driver):
        above = driver.find_element_by_xpath(".//*[@id='J_common_header_menu']/li[2]/span")
        ActionChains(driver).move_to_element(above).perform()
        above1 = driver.find_element_by_xpath(".//*[@id='J_common_header_menu']/li[2]/div/div/div[1]/a[1]")
        ActionChains(driver).move_to_element(above1).perform()
        driver.find_element_by_xpath(".//*[@id='J_common_header_menu']/li[2]/div/div/div[2]/div[1]/div/div[1]/a").click()
        time.sleep(3)
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/a[1]").click()
        time.sleep(3)
        peizhi = "自选配置"
        jifang = "郑州机房"#郑州机房、香港机房
        #服务器配置（快云服务器Ⅱ型、快云服务器Ⅲ型、快云服务器Ⅳ型、快云服务器Ⅴ型、自选配置)
        # driver.find_element_by_link_text(u"快云服务器Ⅰ型").click()
        if "自选配置" in peizhi:
            if "香港机房" in jifang:
                #机房（香港机房）
                driver.find_element_by_link_text(u"香港机房").click()
                #系统盘不用选择（SSD云磁盘）
                #数据盘
                # driver.find_element_by_xpath("html/body/div[4]/div[1]/div[1]/div[2]/div[3]/div[2]/div/ul/li[2]/div[1]/input").clear()
                # a = int(input("请输入数据盘大小："))
                a = 40
                driver.find_element_by_xpath("html/body/div[4]/div[1]/div[1]/div[2]/div[3]/div[2]/div/ul/li[2]/div[1]/input").clear()
                driver.find_element_by_xpath("html/body/div[4]/div[1]/div[1]/div[2]/div[3]/div[2]/div/ul/li[2]/div[1]/input").send_keys(a)
                #cpu(1核、2核、4核、8核、16核)
                driver.find_element_by_xpath("html/body/div[4]/div[1]/div[1]/div[2]/div[4]/div[2]/button[2]").click()
                #内存(2G、4G、8G、12G、16G)
                driver.find_element_by_xpath("html/body/div[4]/div[1]/div[1]/div[2]/div[5]/div[2]/button[1]").click()
                #公网带宽
                # driver.find_element_by_xpath("html/body/div[4]/div[1]/div[1]/div[2]/div[6]/div[2]/div[2]/input").clear()
                # c = int(input("请输入公网带宽："))
                c = 4
                driver.find_element_by_xpath("html/body/div[4]/div[1]/div[1]/div[2]/div[6]/div[2]/div[2]/input").clear()
                driver.find_element_by_xpath("html/body/div[4]/div[1]/div[1]/div[2]/div[6]/div[2]/div[2]/input").click()
                driver.find_element_by_xpath("html/body/div[4]/div[1]/div[1]/div[2]/div[7]").click()
                time.sleep(3)
                driver.find_element_by_link_text(u"下一步选择时长与镜像").click()
                #时长
                # driver.find_element_by_xpath("html/body/div[4]/div[1]/div[2]/div[1]/div[2]/div[3]/input").clear()
                # e = int(input("请输入购买时长："))
                e = 12
                driver.find_element_by_xpath("html/body/div[4]/div[1]/div[2]/div[1]/div[2]/div[3]/input").clear()
                driver.find_element_by_xpath("html/body/div[4]/div[1]/div[2]/div[1]/div[2]/div[3]/input").click()
                driver.find_element_by_xpath("html/body/div[4]/div[1]").click()
                time.sleep(2)
                #操作系统(Windows、CentOS、Debian、Ubuntu)
                driver.find_element_by_link_text("CentOS").click()
                # driver.find_element_by_css_selector("cite").click()
                time.sleep(3)
                # driver.find_element_by_xpath("//body/div[3]/div/div/ul/li[2]").click()
                driver.find_element_by_css_selector("cite").click()
                time.sleep(3)
                driver.find_element_by_link_text(u"CentOS-7.2-x86_64").click()
                time.sleep(2)
                driver.find_element_by_link_text(u"立即购买").click()
                time.sleep(1)
            elif "郑州机房" in jifang:
                # a = int(input("请输入数据盘大小："))
                B = 40
                driver.find_element_by_xpath("html/body/div[4]/div[1]/div[1]/div[2]/div[3]/div[2]/div/ul/li[2]/div[1]/input").clear()
                b = driver.find_element_by_xpath("html/body/div[4]/div[1]/div[1]/div[2]/div[3]/div[2]/div/ul/li[2]/div[1]/input").send_keys(B)
                # cpu(1核、2核、4核、8核、16核)
                driver.find_element_by_xpath("html/body/div[4]/div[1]/div[1]/div[2]/div[4]/div[2]/button[2]").click()
                # 内存(2G、4G、8G、12G、16G)
                driver.find_element_by_xpath("html/body/div[4]/div[1]/div[1]/div[2]/div[5]/div[2]/button[1]").click()
                # 公网带宽
                # c = int(input("请输入公网带宽："))
                C = 6
                driver.find_element_by_xpath("html/body/div[4]/div[1]/div[1]/div[2]/div[6]/div[2]/div[2]/input").clear()
                d = driver.find_element_by_xpath("html/body/div[4]/div[1]/div[1]/div[2]/div[6]/div[2]/div[2]/input").send_keys(C)
                driver.find_element_by_xpath("html/body/div[4]/div[1]/div[1]/div[2]/div[7]").click()
                time.sleep(3)
                driver.find_element_by_link_text(u"下一步选择时长与镜像").click()
                # 时长
                # e = int(input("请输入购买时长："))
                E = 12
                driver.find_element_by_xpath("html/body/div[4]/div[1]/div[2]/div[1]/div[2]/div[3]/input").clear()
                f = driver.find_element_by_xpath("html/body/div[4]/div[1]/div[2]/div[1]/div[2]/div[3]/input").send_keys(E)
                driver.find_element_by_xpath("html/body/div[4]/div[1]").click()
                time.sleep(2)
                # 操作系统(Windows、CentOS、Debian、Ubuntu)
                driver.find_element_by_link_text("CentOS").click()
                # driver.find_element_by_css_selector("cite").click()
                time.sleep(3)
                # driver.find_element_by_xpath("//body/div[3]/div/div/ul/li[2]").click()
                driver.find_element_by_css_selector("cite").click()
                time.sleep(3)
                driver.find_element_by_link_text(u"CentOS-7.2-x86_64").click()
                time.sleep(2)
                driver.find_element_by_link_text(u"立即购买").click()
                time.sleep(1)
        else:
            driver.find_element_by_xpath("html/body/div[4]/div[1]/div[1]/div[2]/div[7]/div[2]/a").click()
            time.sleep(2)
            driver.find_element_by_link_text(u"立即购买")
        print ("加入购物车")

        # #直接结算（未使用优惠抵扣）
        # driver.find_element_by_link_text(u"立即结算").click()
        # time.sleep(1)
        #
        #
        # #使用优惠
        # i = 3 #1代金券；2创业基金；3快云币
        # if i == 3:
        #     driver.find_element_by_xpath(".//*[@id='kyb-dikou']").clear()
        #     g = int(input("请输入使用快云币数量："))
        #     h = driver.find_element_by_xpath(".//*[@id='kyb-dikou']").click()
        #     driver.find_element_by_xpath(".//*[@id='tab5_03']/div").click()
        #     time.sleep(2)
        #
        # elif i == 2:
        #     driver.find_element_by_xpath(".//*[@id='fund-dikou']").clear()
        #     k = int(input("请输入创业基金数量："))
        #     l = driver.find_element_by_xpath(".//*[@id='fund-dikou']").click()
        #     driver.find_element_by_xpath(".//*[@id='tab5_02']/div").click()
        #     time.sleep(2)
        # elif i == 1:
        #     m = driver.find_element_by_xpath(".//*[@id='tab5_01']/ul/li[2]/div[2]/p[1]/span[2]")
        #     n = int(m)








