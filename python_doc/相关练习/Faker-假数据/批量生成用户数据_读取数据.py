#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/23 14:39
# @Author : liuhuiling
# 批量生成数据，用 faker rendom  生成数据，写入 excel
from faker import  Faker
import random
import string
import xlwt
import xlrd

f = Faker('zh_CN')
#新建一个文件
file = xlwt.Workbook(encoding = 'utf-8')
table = file.add_sheet('date',cell_overwrite_ok=True)
table_head = ['用户名','姓名','邮箱','手机']
for a in range(0,4):
       table.write(0, a, table_head[a])
for i in range(1,100):
    username =   ''.join(random.sample(string.ascii_letters, 8))
    name =  f.name()
    email = f.ascii_email()
    phone = f.phone_number()
    #把生成的faker写入文档
    table.write(i,0,username)
    table.write(i,1, name)
    table.write(i,2,email)
    table.write(i,3,phone)
    # print("用户名：", ''.join(random.sample(string.ascii_letters, 8)))
    # print("姓名：", f.name())    # print("邮箱：", f.ascii_email())    # print("手机号：", f.phone_number())
#保存文当为xxx.xls
file.save('data3.xls')

#读取
data = xlrd.open_workbook('data.xls')  # 打开ecxel表
table = data.sheets()[0]  # 切换到对应的sheet
for i in range(1,100):
    username = table.cell(i, 0).value   #读取第i行0列（从0开始计数的）
    name = table.cell(i, 1).value   #读取第i行1列（从0开始计数的）
    email = table.cell(i,2).value   #读取第i行2列（从0开始计数的）
    phone = table.cell(i,3).value   #读取第i行3列（从0开始计数的）
#读取出来写入txt
# nrows = table.nrows  # 获取表格行数
# with open("a.txt", "w") as f:
#     for i in range(1, nrows):
#         rows_values = table.row_values(i)  # 得到每一行的数据
#         for j in rows_values:  # 将每一行的数据写到txt文件中
#             f.write("{}\n".format(j))

