#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/24 14:03
# @Author : liuhuiling
import jieba
import wordcloud
f = open("新时代中国特色社会主义.txt","r",encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(width=1000,height=700,background_color="white",
                        font_path="msyh.ttc")#,max_words=20
w.generate(txt)
w.to_file("grwordcloud.png")
