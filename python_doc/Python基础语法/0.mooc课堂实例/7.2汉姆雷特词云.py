#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/24 14:35
# @Author : liuhuiling
# from 0.素材 import *
import wordcloud
from os.path import dirname,abspath
project_path = dirname(dirname(abspath(__file__))) #获得文件所在的绝对目录
f = open(project_path+"\\0.素材\\hamlet.txt","r")  #绝对路径拼接相对路径，读取文件
t = f.read()
f.close()
# w = wordcloud.WordCloud(width=1000,height=700,background_color="white",stopwords="and to of that the")
w  = wordcloud.WordCloud(width=1000,height=700,background_color="white")
w.generate(t)
w.to_file(project_path+"\\0.素材\\运行结果\\hamlet.png")