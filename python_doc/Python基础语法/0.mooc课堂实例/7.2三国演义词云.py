#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/24 15:21
# @Author : liuhuiling
import jieba
import wordcloud
from os.path import abspath,dirname
project_path = dirname(dirname(abspath(__file__)))
f = open(project_path+"\\0.素材\\threekingdoms.txt","r",encoding="utf-8")
t = f.read()
f.close()
txt = jieba.lcut(t)
w = wordcloud.WordCloud(width=1000,height=800,background_color="white",font_path="msyh.ttc")
w.generate(" ".join(txt))
w.to_file(project_path+"\\0.素材\\运行结果\\threekingdoms.png")