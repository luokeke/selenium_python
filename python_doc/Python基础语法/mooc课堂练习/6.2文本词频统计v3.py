#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/13 10:39
# @Author : liuhuiling
import jieba
txt = open("threekingdoms.txt","r",encoding="utf-8").read()
excludes = {"将军","却说","荆州","二人","不可","不能","如此","商议","如何","军士"}
#,"今日","于是","东吴","天下","大喜","次日","引兵","军马","左右"
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1 #不在字典中就加入，次数加1；在次数+1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True) #排序
for i in range(15):
    word,count = items[i] #items列表内元素是元组形式，注意赋值形式
    print("{0:<10}{1:>5}".format(word,count))
