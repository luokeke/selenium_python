#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/24 14:03
# @Author : liuhuiling
import jieba
import wordcloud
from os.path  import abspath,dirname
project_path = dirname(dirname(abspath(__file__)))
f = open(project_path+"\\0.素材\\新时代中国特色社会主义.txt","r",encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(width=1000,height=700,background_color="white",
                        font_path="msyh.ttc")#,max_words=20
w.generate(txt)
w.to_file(project_path+"\\0.素材\\运行结果\\grwordcloud.png")
