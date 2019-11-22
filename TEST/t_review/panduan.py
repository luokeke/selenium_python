#-*- coding:utf-8 -*-
import pymysql.cursors


'''
脚本作用 ：根据登录用户名查询账号类型，是个人还是企业
'''
login = "luokeke00.00"  #登录用户名，请修改为实际可以用的

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
        # sql = 'SELECT member_type FROM `tabmembers` WHERE `account_id` = 289175'
        # "SELECT * FROM EMPLOYEE  WHERE INCOME > '%d'" % (1000)
        sql = "SELECT member_type,account_id FROM `tabmembers` WHERE `login` = '%s'" % (login)
        cursor.execute(sql)
        # 获取查询结果
        result = cursor.fetchone()
        #获取查询结果赋值给type
        type = result['member_type']  #获取查询结果字典里的member_type值
        # print result  #查询结果是字典的形式
        hybh  = result['account_id']
        if type == 1:
            print "属于个人认证"
        elif type == 2:
            print "属于企业认证"
        # print type
        print "%s的会员编号是：%d" %(login,hybh)
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()
finally:
    connection.close();
