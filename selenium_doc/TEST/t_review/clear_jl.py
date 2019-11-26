#-*- coding:utf-8 -*-
import pymysql.cursors
'''
脚本作用 ： 清理账号实名认证记录
执行前需要修改sql 里的 login 字段值，或者hybh
'''

'''
更改数据
根据用户名清理，具体sql如下：
UPDATE t_review AS t LEFT JOIN tabmembers AS tab ON tab.account_id = t.hybh set t.hybh = '2891750' , t.msgzt = '0' WHERE tab.login = 'luokeke00.00'
根据会员编号清理，具体sql如下：
"UPDATE t_review SET  hybh = '2891750' WHERE hybh = '289175'"

删除数据：
DELETE  t  FROM  t_review AS t LEFT JOIN tabmembers AS tab ON tab.account_id = t.hybh   WHERE tab.login = 'luokeke00.00'
'''

login  =  "luokeke00.00"
hybh = 289571
idnum = '511702197404273798'

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
        # 执行sql语句
        #根据login，删除会员实名认证记录
        # sql = "DELETE  t  FROM  t_review AS t LEFT JOIN tabmembers AS tab ON tab.account_id = t.hybh   " \
        #       "WHERE tab.login = '%s'" % (login)
        #根据login，修改t_review表对应记录的hybh，（把实名认证记录修改到别的hybh下）
        # sql = "UPDATE t_review AS t LEFT JOIN tabmembers AS tab ON tab.account_id = t.hybh " \
        #       "set t.hybh = '2891750' , t.msgzt = '0' WHERE tab.login = '%s'" % (login)
        #根据hybh，修改t_rebiew表对应记录（把实名认证记录修改到别的hybh下）
        # sql = "UPDATE t_review SET  hybh = '2891750' WHERE hybh = '%d'" %(hybh)
        #根据证件号，修改t_review表认证证件号
        sql = "UPDATE t_review SET  buslicense_code = '123456' WHERE buslicense_code = '%s' " %(idnum)
        cursor.execute(sql)
        print "实名认证信息已清理掉"
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()
finally:
    connection.close();
