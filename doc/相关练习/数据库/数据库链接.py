#-*- coding:utf-8 -*-
import pymysql.cursors
#判断用户是否已经实名认证
# 连接配置信息
config = {
    'host' :'116.255.177.48',
    'port' :3306,
    'user' :'test',
    'password' :'ceshizu123!@#',
    'db' :'zzidc_db',
    'charset' :'utf8mb4',
    'cursorclass' :pymysql.cursors.DictCursor,
}
# 创建连接
connection = pymysql.connect(**config)
try:
    with connection.cursor() as cursor:
        # 执行sql语句，进行查询
        sql = 'SELECT member_type FROM `tabmembers` WHERE `account_id` = 289175'
        cursor.execute(sql)
        # 获取查询结果
        result = cursor.fetchone()#返回的是字典类型
        print(result)
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()
finally:
    connection.close();
type = result['member_type']
print(type)