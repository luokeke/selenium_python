# -*- coding:utf-8 -*-
#安装好mysql后，安装pymysql模块，pip install pymysql
from pymysql import connect,cursors
email = "asdfasdf@zzidc.com1"
mobile = '14710658820'
#链接数据库
conn = connect(host="10.220.129.249", user="testteam", password="f5H9B56QTW3fd5KDLCefg3kHuKefeb7D", db="zzidc_db",charset="utf8mb4", cursorclass = cursors.DictCursor)
#写sql查对应手机号的验证码
#sql = "SELECT code FROM smsvalidation WHERE email = %s and ifused = 0;"
sql = "SELECT code FROM smsvalidation WHERE mobile = %s and ifused = 1;"

#执行sql，并把执行结果赋值给result（此结果为字典格式）
with conn.cursor() as cursor:
    cursor.execute(sql,email)
    result = cursor.fetchone()
conn.close()
#在结果字典里取出来code对应的数值。
sms = result['code']
print (sms,result)




