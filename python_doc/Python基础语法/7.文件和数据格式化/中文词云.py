#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/24 14:01
# @Author : liuhuiling
import wordcloud
'''
基本思路
    1.读取文件、分词整理 中文分词用jieba
    2.设置并输出词云
    3.观察结果，优化迭代
'''
import jieba
import wordcloud
txt="程序设计语言是计算机能够理解和识别用户操作意图的一种交互体系，它按照特定规则组织计算机指令，使计算机能够自动进行各种运算处理。"
w=wordcloud.WordCloud(width=1000,height=700,font_path="仿宋_GB2312.ttf")
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("computerlanguage.png")
