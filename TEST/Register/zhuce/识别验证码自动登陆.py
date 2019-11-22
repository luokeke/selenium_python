# -*- coding: utf-8 -*-
#Author：哈士奇说喵
from selenium import webdriver
import os
import pytesser
import sys,time
from PIL import Image,ImageEnhance

#shift+tab多行缩进(左)
reload(sys)
PostUrl = "http://beian.zzidc.com"
driver=webdriver.Firefox()
driver.get(PostUrl)
i=0
while 1:#sb登录系统，即使输对所有消息还是登不进去的，需要登录两次及以上
    i=i+1
    try:
        elem_user = driver.find_element_by_name("userName")
        elem_psw = driver.find_element_by_name("passWord")
        elem_code = driver.find_element_by_name("codeNum")
    except:
        break
    #-------------------对验证码进行区域截图------------------
    code = driver.find_element_by_id("verifyCode")
    code.screenshot("11yanzhengma.png")
    #--------------------图片增强+自动识别简单验证码-----------------------------
    time.sleep(3)#防止由于网速，可能图片还没保存好，就开始识别
    def image_file_to_string(file):
        cwd = os.getcwd()
        try :
            os.chdir("C:\Users\MrLevo\Anaconda2\Lib")
            return pytesser.image_file_to_string(file)
        finally:
            os.chdir(cwd)
    im=Image.open("11yanzhengma.png")
    imgry = im.convert('L')#图像加强，二值化
    sharpness =ImageEnhance.Contrast(imgry)#对比度增强
    sharp_img = sharpness.enhance(2.0)
    sharp_img.save("E:\\image_code.jpg")
    #http://www.cnblogs.com/txw1958/archive/2012/02/21/2361330.html
    #imgry.show()#这是分布测试时候用的，整个程序使用需要注释掉
    #imgry.save("E:\\image_code.jpg")

    code= pytesser.image_file_to_string("E:\\image_code.jpg")#code即为识别出的图片数字str类型
    print (code)
    #打印code观察是否识别正确


    #----------------------------------------------------------------------
    if i <= 2: # 根据自己登录特性，我这里是验证码失败一次，重填所有，失败两次，重填验证码
        elem_user.send_keys('S315080092')
        elem_psw.send_keys('xxxxxxxxxx')

    elem_code.send_keys(code)
    click_login = driver.find_element_by_xpath("//img[@src='main_images/images/loginbutton.gif']")
    click_login.click()


#time.sleep(5)#搜索结果页面停留片刻
#driver.save_screenshot('C:\Users\MrLevo\image.jpg')
#driver.close()
#driver.quit()


