# -*- coding:UTF-8 -*-

import os

file_dir = 'D:\\Pictures'
for root, dirs, files in os.walk(file_dir):
    # print(root)  # 当前目录路径
   # print(dirs)  # 当前路径下所有子目录
    print(files)  # 当前路径下所有非目录子文件
path = files[1]
pt = 'D:\\Pictures\\' + path
print  (path , pt)
