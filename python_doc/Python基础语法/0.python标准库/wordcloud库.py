#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/23 18:24
# @Author : liuhuiling
print()
'''
安装：pip install wordcloud  有报错不可用
网址： https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud 
下载相应包，进入包所在文件夹，  pip install 包名 安装

wordcloud库把词云当作一个WordCloud对象
    wordcloud.WordCloud()代表一个文本对应的词云
    可以根据文本词语出现的频率等参数绘制词云
    绘制词云的形状、尺寸和颜色都可以设定

步骤：
    配置对象参数
    加载词云文本
    输出词云文件

方法                    描述
w.generate(txt)         向WordCloud对象w中加载文本txt
w.to_file(filename)     将词云输出为图像文件，.png或.jpg格式

wordcloud 操作
    分隔：以空格分隔单词
    统计：单词出现次数并过滤
    字体：根据统计配置字号
    布局：颜色环境尺寸
w = wordcloud.WordCloud() 参数
   width    指定词云生成图片宽度，默认400像素
   height   指定词云生成图片高度，默认200像素
   min_font_size    指定词云中字体的最小号，默认4号
   max_font_size    指定词云中字体的最大字号，根据高度自动调节
   font_path        指定字体文件的路径，默认None
   max_words        指定词云显示的最大单词数量，默认200
   stop_words       指定词云的排除词列表，即不显示的单词列表
   mask             指定词云形状，默认长方形，需要引用imread()函数
   background_color 指定词云图片的背景颜色，默认为黑色 
   
   参数	描述
width	        指定词云对象生成图片的宽度,默认400像素   w=wordcloud.WordCloud(width=600)
height	        指定词云对象生成图片的高度,默认200像素   w=wordcloud.WordCloud(height=400)
min_font_size	指定词云中字体的最小字号，默认4号   w=wordcloud.WordCloud(min_font_size=10)
max_font_size	指定词云中字体的最大字号，根据高度自动调节   w=wordcloud.WordCloud(max_font_size=20)
font_step	    指定词云中字体字号的步进间隔，默认为1 w=wordcloud.WordCloud(font_step=2)
font_path	    指定文体文件的路径，默认None    w=wordcloud.WordCloud(font_path="msyh.ttc")
max_words	    指定词云显示的最大单词数量,默认200 w=wordcloud.WordCloud(max_words=20)
stopwords	    指定词云的排除词列表，即不显示的单词列表    w=wordcloud.WordCloud(stopwords="Python")
mask	        指定词云形状，默认为长方形，需要引用imread()函数    
                    from imageio import imread   #安装最新scipy库  pip install scipy
                    mk=imread("pic.png")
                    w=wordcloud.WordCloud(mask=mk)
background_color 指定词云图片的背景颜色，默认为黑色   w=wordcloud.WordCloud(background_color="white")

'''
#英文文本
import wordcloud
w = wordcloud.WordCloud(width=1000,height=700,background_color="white",font_path="仿宋_GB2312.ttf",)
w.generate('''
Python and wordcloud 
pip install wordcloud 
import wordcloud
w.generate(txt)
w.to_file(filename) 
''')
w.to_file("1234.png")

# from scipy.msc import imread
# mk=imread("pic.png")
# w=wordcloud.WordCloud(mask=mk)
#中文文本
import jieba
import wordcloud
txt="程序设计语言是计算机能够理解和识别用户操作意图的一种交互体系，它按照特定规则组织计算机指令，使计算机能够自动进行各种运算处理。"
w=wordcloud.WordCloud(width=1000,height=700,font_path="仿宋_GB2312.ttf",background_color="white")
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("computerlanguage.png")
