#-*- coding:UTF-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import unittest, xlrd
from time import sleep

'''实现自动化登录'''

def open_excel(file='F:\python\TEST\lo.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print (str(e))
        # 根据索引获取Excel表格中的数据 参数:file：Excel文件路径 colnameindex：表头列名所在行的所以 ，by_index：表的索引


def excel_table_byindex(file='F:\python\TEST\lo.xlsx', colnameindex=0, by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows  # 行数
    colnames = table.row_values(colnameindex)  # 某一行数据
    list = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list


def login():
    listdata = excel_table_byindex("F:\python\ceshi\lo.xlsx", 0)
    if (len(listdata) <= 0):
        assert 0, u"Excel数据异常"
    for i in range(0, len(listdata)):
        driver = webdriver.Firefox()
        driver.get("http://beta.zzidc.com")
        # 点击登录按钮
        sleep(3)
        driver.find_element_by_link_text("登录").click()
        sleep(3)
        driver.find_element_by_id('username').send_keys(listdata[i]['username'])
        driver.find_element_by_id('password').send_keys(listdata[i]['password'])
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id('username').send_keys(listdata[i]['username'])
        driver.find_element_by_id("login-loginok").click()
        sleep(2)
        try:
            elem = driver.find_element_by_xpath("//div[3]/div/div[1]/div[1]/a/img")
        except NoSuchElementException:
            assert 0, u"登录失败，找不到左上角头像"
        driver.close()
    def user(self):
        print ("123")


if __name__ == '__main__':
    login()