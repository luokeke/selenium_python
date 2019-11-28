#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/22 16:12
# @Author : liuhuiling

import uuid
import hashlib
import time
def create_uuid():   #通过UUID的方式创建
    return str(uuid.uuid1())
def create_md5():    #通过MD5的方式创建
    m=hashlib.md5()
    m.update(bytes(str(time.time()),encoding='utf-8'))
    return m.hexdigest()
if __name__ == '__main__':
    print(create_uuid())
    print(create_md5())



