# -*- coding:UTF-8 -*-
# import random
# i = random.choice('abcdefghijklmnopqrstuvwxyz')
# print i
#
# import string #This was a design above but failed to print. I remodled it.
# import random
# irandom = random.choice(string.ascii_letters)
# print irandom


import string
import random
salt = ''.join(random.sample(string.ascii_letters + string.digits, 16))
# salt = ''.join(random.sample(string.ascii_letters, 5))
bucketname = salt.lower()
print (salt)
print (bucketname)



import random
import string

# 第一种方法



# import uuid
# print(uuid.uuid1())
# print(uuid.uuid1())
# print(uuid.uuid1())

# import uuid
# import hashlib
# import time
#
# def create_uuid():   #通过UUID的方式创建
#     return str(uuid.uuid1())
#
# def create_md5():    #通过MD5的方式创建
#     m=hashlib.md5()
#     m.update(bytes(str(time.time()),encoding='utf-8'))
#     return m.hexdigest()
#
# if __name__ == '__main__':
#     print(create_uuid())
#     print(create_md5())