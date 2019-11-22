#! /usr/bin/env python
# -*- coding:utf-8 -*-

import config
import MySQLdb

def execCloudSQL(sqlstr):
    if sqlstr is None or sqlstr == "":
        return None

    conn = None
    try:
        conn = MySQLdb.connect(host=config.cloud_host, user=config.cloud_user, passwd=config.cloud_pwd,
                               db=config.cloud_db, port=config.cloud_port, charset=config.cloud_charset)
    except Exception as e:
        raise e

    try:
        cur = conn.cursor()
        cur.execute(sqlstr)
        result = cur.fetchall()
        cur.close()
        conn.commit()
        conn.close()
    except Exception as e:
        raise e
    else:
        return result