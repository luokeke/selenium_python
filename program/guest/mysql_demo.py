#-*- coding:UTF-8 -*-
from pymysql import cursors,connect
conn = connect(host='127.0.0.1',
               user='root',
               passwd='root',
               db='guest',
               charset='utf8mb4',
               cursorclass=cursors.DictCursor)
cursor = conn.cursor()
sql = """CREATE TABLE IF NOT EXISTS TABLEONE (
         `id` int(11) NOT NULL AUTO_INCREMENT,
         `title` varchar(255) COLLATE utf8_bin NOT NULL,
         `vote_count` int(255) COLLATE utf8_bin NOT NULL,
         `answer_count` int(255) COLLATE utf8_bin NOT NULL,
         `scan_count` int(255) COLLATE utf8_bin NOT NULL,
         PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1 ;"""
creatResult = cursor.execute(sql)
sql = "INSERT INTO `TABLEONE` (`title`, vote_count, answer_count, scan_count) VALUES (%s, %s, %s, %s)"
cursor.execute(sql, ('webmaster@python.org', -1,1,30))
conn.commit()
