#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/12 13:48
# @Author : liuhuiling
print()
'''
jieba是优秀的中文分词第三方库
- 中文文本需要通过分词获得单个的词语
- jieba库提供三种分词模式，精确模式、全模式、搜索引擎模式
    精确模式：把文本精确的切分开，不存在冗余单词
    全模式：把文本中所有可能的词语都扫描出来，有冗余
    搜索引擎模式：在精确模式基础上，对长词再次切分
- 安装 pip install jieba 
- 利用一个中文词库，确定汉字之间的关联概
- 汉字间概率大的组成词组，行程分词结果
- 除了分词，用户还可以添加自定义的词组

jieba库常用函数              描述
jieba.lcut(s)                精确模式，返回一个列表类型的分词结果
jieba.lcut(s,cut_all=True)   全模式，返回一个列表类型的分词结果，存在冗余 
jieba.lcut_for_search(s)     搜索引擎模式，返回一个列表类型的分词结果，存在冗余
jieba.add_word(w)            向分词词典增加新词w

'''
import jieba
jieba.add_word("结巴")
print(jieba.lcut("中国是一个伟大的国家")) #['中国', '是', '一个', '伟大', '的', '国家']
print(jieba.lcut("中国是一个伟大的国家",cut_all=True))#['中国', '国是', '一个', '伟大', '的', '国家']
print(jieba.lcut_for_search("中华人民共和国是伟大的")) #['中华', '华人', '人民', '共和', '共和国', '中华人民共和国', '是', '伟大', '的']