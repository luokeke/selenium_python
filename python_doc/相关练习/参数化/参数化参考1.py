#-*- coding:UTF-8 -*-
'''注释：参数化读取excel文件里数值'''
import xlrd
# 打开exlce表格，参数是文件路径
data = xlrd.open_workbook('F:\python\ceshi\lo.xlsx')

# table = data.sheets()[0]           #  通过索引顺序获取
# table = data.sheet_by_index(0)     #  通过索引顺序获取
table = data.sheet_by_name(u'Sheet1')  # 通过名称获取

nrows = table.nrows  # 获取总行数
ncols = table.ncols  # 获取总列数

#　获取一行或一列的值，参数是第几行
print (table.row_values(0)) # 获取第一行值
print (table.row_values(1))  # 获取第er行值
print (table.row_values(2))  # 获取第er行值
print (table.col_values(0))  # 获取第一列值
print (table.col_values(1)) # 获取第er列值


def rwExcel():
    global table
    data = xlrd.open_workbook('e:\\pythonlearn\\basefenpei.xlsx')
    table = data.sheets()[0]
    cell00 = table.cell(0, 0).value
    cell01 = table.cell(0, 1).value
    cell10 = table.cell(1, 0).value
    cell11 = table.cell(1, 1).value
    print (cell00, cell01, cell10, cell11)
    table.cell(2, 1).value = "hello"
    table.cell(2, 2).value = "realmadrid"
    table.cell(2, 3).value = "yang"

