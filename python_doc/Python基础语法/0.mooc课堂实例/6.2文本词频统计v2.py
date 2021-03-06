#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/12 15:10
# @Author : liuhuiling
import jieba
from os.path import abspath,dirname
project_path = dirname(dirname(abspath(__file__)))
txt = open(project_path+"\\0.素材\\threekingdoms.txt","r",encoding="utf-8").read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1 #不在字典中就加入，次数加1；在次数+1
        #dict.get(k,default) 键k存在，则返回相应值，不存在则返回默认值None  或设置的default值 （默认值）
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True) #排序
for i in range(15):
    word,count = items[i] #items列表内元素是元组形式，注意赋值形式
    print("{0:<10}{1:>5}".format(word,count))

