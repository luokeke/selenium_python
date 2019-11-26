# coding:utf-8
'''安装MYSQL DB for python
载 MySQL for Python
地址：http://sourceforge.net/projects/mysql-python/files/mysql-python/ '''
import MySQLdb

# con = None
#dbpath='E:\Databases'
#修改为数据库所在路径
try:
    #连接mysql的方法：connect('ip','user','password','port')     
    con = MySQLdb.connect(host='116.255.177.48', user='test', passwd='ceshizu123!@#', port=3306, charset='utf8',db="zzidc_db")
    #修改为你自己安装的MySQL用户名和密码，数据库名称
    #所有的查询，都在连接con的一个模块cursor上面运行的
    cur = con.cursor()
    #执行一个查询
    cur.execute("SELECT id from tabmembers where login=12212212224")
    #取得上个查询的结果，是单个结果
    data = cur.fetchone()
    num =data[0]
    # i = data.id
    print ("Database version : %s ") % data
    print (num)
#此程序向屏幕输出一句话而已。
finally:
    if con:
        #无论如何，连接记得关闭
        cur.close()
        con.close()