#-*- coding:UTF-8 -*-

# from TEST.cunchu.login import *
from selenium import webdriver



#账号实名认证
driver = webdriver.Firefox()
driver.maximize_window()
driver.delete_all_cookies()
#登录or调用登录模块，访问景安站并登录。
# Login().user_login(driver,"http://www.zzidc.com","用户名","密码")
#UPDATE t_review SET  hybh = '2891750' WHERE hybh = '289175'
#例子
# Login().user_login(driver,"http://www.zzidc.com","luokeke00.00","luokeke00.00")
#进入会员中心
driver.implicitly_wait(3)
driver.find_element_by_link_text(u"管理中心").click()
#进入实名认证界面
driver.implicitly_wait(3)
driver.find_element_by_xpath(u"(//a[contains(text(),'实名认证')])[2]").click()
#判断是个人认证还是企业认证  参数 idnum  reviewname email可以修改
try:
    driver.find_element_by_link_text(u"个人认证")
    idnum = '511702197404273798'  # 个人身份照，可以修改
    reviewname = u"洛可可"  # 个人名称，可以修改
except:
    idnum = '46546asdfajsdf'  # 企业营业执照号码，可以修改
    reviewname = u"斑斓本有限公司"  # 企业名称，可以修改
email = "luokeke00.00@zzidc.com" #邮箱，可以修改
# idpo = idnum
driver.implicitly_wait(3)
driver.find_element_by_name("businessName").clear()
driver.find_element_by_name("businessName").send_keys(reviewname)
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("buslicenseCode").clear()
driver.find_element_by_name("buslicenseCode").send_keys(idnum)
#上传图片
driver.implicitly_wait(3)
driver.find_element_by_id("idFile").clear()
driver.find_element_by_id("idFile").send_keys("C:\\Users\\Administrator\\Pictures\\834KB.JPG")
#提交实名认证信息
driver.implicitly_wait(3)
driver.find_element_by_link_text(u"下一步").click()
#信息确认
driver.implicitly_wait(3)
driver.find_element_by_link_text(u"确认").click()
#提交成功
# time.sleep(2)
driver.find_element_by_link_text(u"确认").click()