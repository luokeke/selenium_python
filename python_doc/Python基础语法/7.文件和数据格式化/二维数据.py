#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/23 16:27
# @Author : liuhuiling
print()
'''
二维数据的存储
    按行存或者按列存都可以，具体由程序决定
    一般索引习惯，ls[row][column],先行后列
    根据一般习惯，外层列表每个元素是一行，按行存

CSV数据存储格式  
    Comma-Separated Values  由逗号分隔的值
    国际通用的一二维数据存储格式，一般.csv扩展
    每行一个一维数据，采用逗号分隔，无空行
    如果某个元素缺失，逗号仍要保留
    二维数据的表头可以作为数据存储，也可以另行存储
    逗号为英文半角符号，逗号和数据之前无空格

二维数据的表示
    使用列表类型可以表达二维数据
    使用二维列表，列表中每一个元素又是一个列表，其中每个元素可以代表二维数据的一行或者一列
    使用两层for循环遍历每个元素
    外层里列表中每个元素可以对应一行，也可以对应一列
    
二维数据的处理
    从CSV格式的文件中读入数据
        fo = open(filename)
        ls = []
        for line in fo:
            line = line.replace("\n","")
            ls.append(line.split(","))
        fo.close()
    将数据写入CSV格式的文件
        ls = [[],[],[]]#二维列表
        f = open(fname,"w")
        for item in ls:
            f.write(",".join(item)+"\n")
        f.close()
    逐一遍历
        ls = [[1,2],[3,4],[5,6]]
        for row in ls:
            for column in row:
                print(column)



'''