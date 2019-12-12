#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/12 14:02
# @Author : liuhuiling

'''
文本词频统计
- 英文文本：Hamet 分析词频
https://python123.io/resources/pye/hamlet.txt
- 中文文本：《三国演义》 分析人物
https://python123.io/resources/pye/threekingdoms.txt
'''

def getText():
    txt = open("hamlet.txt","r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~ ':
        txt = txt.replace(ch, " ")  #特殊字符替换成空格
    return txt
hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1 #不在字典中就加入，次数加1；在次数+1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True) #排序
for i in range(10):
    word,count = items[i] #items列表内元素是元组形式，注意赋值形式
    print("{0:<10}{1:>5}".format(word,count))
