#-*- coding:UTF-8 -*-
from time import  sleep
from selenium import webdriver

# from TEST.cunchu.login import *

driver = webdriver.Firefox()
# Login().user_login(driver, "https://mc.kuaiyun.cn/storage/bucketList.action", "luokeke", "1")
#进入某一空间，luokeke12
driver.find_element_by_link_text("luokeke12").click()
sleep(3)
#点击上传文件按钮，出现上传文件弹框
driver.find_element_by_id("dropDiv").click()
sleep(3)
#点击弹框里上传文件按钮，出现上传文件的选择框
# driver.find_element_by_id("addFile").click()
# above = driver.find_element_by_id("layui-layer1")
# ActionChains(driver).move_to_element(above).perform()
# driver.find_element_by_id("idFile").clear()
# driver.find_element_by_id("idFile").send_keys("C:\\Users\\Administrator\\Pictures\\834KB.JPG")
upload = driver.find_element_by_id("addFile")
upload.clear()
upload.send_keys("C:\\Users\\Administrator\\Pictures\\834KB.JPG")


#<a id="addFile" class="add-btn" style="position: relative; z-index: 1;">上传文件</a>
#<input id="idFile" name="idCard" onchange="previewImage(this,1)" class="uplod-txt" style="display:block" type="file">