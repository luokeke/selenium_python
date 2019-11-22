#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2017/11/14 11:28 
#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2017/11/14 10:16
from  time import sleep
# ddbh = 1522351 #订单编号

class Search_orders():
    def search_orders(self,driver,ddbh):
        #点掉发票提醒弹框
        try:
            driver.find_element_by_xpath(".//*[@id='layui-layer1']/div[3]/a").click()
        except:
            pass
        sleep(3)
        #输入订单编号
        driver.find_element_by_xpath(".//*[@id='searchForm']/div[1]/input").clear()
        driver.find_element_by_xpath(".//*[@id='searchForm']/div[1]/input").send_keys(ddbh)
        # driver.find_element_by_name("conditionPage.queryCondition.logo").clear()
        # driver.find_element_by_name("conditionPage.queryCondition.logo").send_keys(ddbh)
        sleep(2)
        #查询
        driver.find_element_by_xpath(".//*[@id='searchForm']/div[1]/a").click()
        sleep(2)
        #点击开通
        driver.find_element_by_link_text("开通").click()
        sleep(2)














