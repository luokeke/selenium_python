# -*- coding:utf-8 -*-
#安装好mysql后，安装pymysql模块，pip install pymysql
from pymysql import connect,cursors
#链接数据库
conn = connect(host="116.255.177.48", user="test", password="ceshizu123!@#", db="zzidc_db",charset="utf8mb4", cursorclass = cursors.DictCursor)
try:
    with conn.cursor() as cursor:
        # 执行一个查询
        sql = "SELECT * from tabmembers where name='刘花花';"
        cursor.execute(sql)
        # 取得上个查询的结果，是单个结果
        result = cursor.fetchone()
        print (str(result).decode(encoding='unicode_escape'))
        # print ("Database version : %s ") % result
        # print (result)
        sms = result['name']
        email = result['email']
        real_email = result['real_email']
        account_id = result['account_id']
        print ('你好',sms,email,real_email,account_id)
        # 此程序向屏幕输出一句话而已。
    conn.commit()
finally:
    conn.close()

# #-*- coding:utf-8 -*-
# import pymysql.cursors
# # 连接配置信息
# config = {
#     'host' :'192.168.67.135',
#     'port' :3306,
#     'user' :'root',
#     'password' :'root',
#     'db' :'zzidc_db',
#     'charset' :'utf8mb4',
#     'cursorclass' :pymysql.cursors.DictCursor,
# }
# # 创建连接
# connection = pymysql.connect(**config)
# try:
#     with connection.cursor() as cursor:
#         # 执行sql语句，进行查询
#         sql = 'SELECT id FROM tabmembers WHERE login = "luokeke"'
#         cursor.execute(sql)
#         # 获取查询结果
#         result = cursor.fetchone()
#         print(result)
#     # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
#     connection.commit()
# finally:
#     connection.close();


#-*- coding:utf-8 -*-
# import datetime
# import pymysql.cursors
# # 连接配置信息
# config = {
#     'host' :'192.168.67.135',
#     'port' :3306,
#     'user' :'root',
#     'password' :'root',
#     'db' :'zzidc_db',
#     'charset' :'utf8mb4',
#     'cursorclass' :pymysql.cursors.DictCursor,
# }

# # 创建连接
# connection = pymysql.connect(**config)
# # 获取雇佣日期
# # create_on = datetime.date(2006, 1, 1)
#
# hire_start = datetime.date(1999, 1, 1)
# hire_end = datetime.date(2016, 12, 31)
# # 执行sql语句
#
# try:
#     with connection.cursor() as cursor:
#         # 执行sql语句，进行查询create_on
#         sql = 'SELECT id, name, create_on FROM tabmembers WHERE create_on BETWEEN %s AND %s'
#         # sql = 'SELECT first_name, last_name, hire_date FROM employees WHERE hire_date BETWEEN %s AND %s'
#         cursor.execute(sql, (hire_start, hire_end))
#         # 获取查询结果
#         result = cursor.fetchone()
#         print(result)
#     # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
#     connection.commit()
# finally:
#     connection.close();