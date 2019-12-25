#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/24 14:35
# @Author : liuhuiling

import wordcloud
f = open("hamlet.txt","r")
t = f.read()
f.close()
# w = wordcloud.WordCloud(width=1000,height=700,background_color="white",stopwords="and to of that the")
w  = wordcloud.WordCloud(width=1000,height=700,background_color="white")
w.generate(t)
w.to_file("hamlet.png")