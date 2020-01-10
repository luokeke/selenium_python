#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/1/8 11:34
# @Author : liuhuiling
import os
'''
Web网络爬虫
Requests        最友好的网络爬虫功能库
    提供了简单易用的类HTTP协议网络爬虫功能
    支持连接池、SSL、Cookies、HTTP(S)代理等
    python最主要的页面级网络爬虫功能库
    http://www.python-requests.org/
Scrapy      优秀的网络爬虫框架
    提供了构建网络爬虫系统的框架功能，功能半成品
    支持批量和定时网页爬取、提供数据处理流程等
    python最主要且最专业的网络爬虫框架
    http://scrapy.org
pyspider        强大的Web页面爬取系统
    提供了完整的网页爬取系统构建功能
    支持数据库后端、消息队列、优先级、分布式架构等
    http://docs.pyspider.org

Web信息提取
Beautiful Soup      HTML和XML的解析库
    提供了解析HTML和XML等Web信息的功能
    又名beautifulsoup4或bs4，可以加载多种解析引擎
    常与网络爬虫库搭配使用，如在Scrapy、requests等
Re      正则表达式解析和处理功能库
    提供了定义和解析正则表达式的一批通用功能
    可用于各类场景，包括定点的Web信息提取
    Python最主要的标准库之一，不需要安装
    re.search()         re.split()
    re.match()          re.findter()
    re.findall()        re.sub()
Python-Goose        提取文章类型Web页面的功能库     
    提供了对Web页面中文章信息/视频等元数据的提取功能
    针对特定类型Web页面，应用覆盖面较广
    Python最主要的Web信息提取库
    http://github.com/grangier/python-goose
    pip install goose3
    参考资料：https://blog.csdn.net/zhusongziye/article/details/83152816

Web网站开发
Django:最流行的Web应用框架
    提供了构建Web系统的基本应用框架
    MTV模式：模型(model)、模板(Template)、视图(Views)
Pyramid：    规模适中的Web应用框架
    提供了简单方便构建Web系统的应用框架
    不大不小，规模适中，适合快速构建并适度扩展类应用
    Python产品级Wwb应用框架，起步简单可扩展性好
    详见Pyramid_举例.py
    https://trypyramid.com/
    pip install pyramid
Flask   Web应用开发微框架
    提供了最简单构建Web系统的应用框架
    特点是：简单、规模小、快速
    pip install flask
    https://palletsprojects.com/p/flask/

网络应用开发
    WeRoBot     微信公众号开发框架
        提供了解析微信服务器消息及反馈消息的功能
        建立微信机器人的重要技术手段
        pip install werobot
        https://github.com/offu/WeRoBot
    aip:百度AI开放平台接口
        提供了访问百度AI服务的Python功能接口
        语音、人脸、OCR、NLP、知识图谱、图像搜索等领域
    MyQR    二维码生成第三方库
        提供了生成二维码的系列功能
        基本二维码、艺术二维码和动态二维码
        https://github.com/syinsfar/qrcode
        
        
'''
