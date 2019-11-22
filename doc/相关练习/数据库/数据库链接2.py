#-*- coding：UTF-8 -*-
#-*- coding:UTF-8 -*-
#
from pymysql import connect
from pymysql import cursors
class Database:
    def __init__(self):
        conn= connect(   # 连接数据库
        host='135',   # 连接你要取出数据库的ip，如果是本机可以不用写
        port = 3306,
        user='root',     # 你的数据库用户名
        passwd='root',# 你的数据库密码
        db ='test',
        charset='utf8mb4',)
        self.user_list = []

    def get_mysql_user(self,begin,end):   #取出数据库
        with self.conn:
            # 获取连接上的字典cursor，注意获取的方法，
            # 每一个cursor其实都是cursor的子类
            cur = self.conn.cursor(cursors.DictCursor)
            # 执行MySQL语句,这里获取id从begin 到 end 的数据
            cur.execute("SELECT * FROM tabmembers WHERE ID >= "+str(begin) +" AND ID <= "+str(end) )
            # 获取数据方法
            rows = cur.fetchall()
            # 遍历数据（比上一个更直接一点）
            dict_uid = dict()
            # print rows
            for row in rows:
                # 这里，可以使用键值对的方法，由键名字来获取数据
                # print "%s %s" % (row["user_id"], row["user_name"])
                # print "%s" % (row["user_id"])
                self.user_list.append(row["user_id"])
            # print user_list
            # dict_uid[row["user_id"]]=row["user_name"]
            return self.user_list
Database().get_mysql_user('129381','129382')