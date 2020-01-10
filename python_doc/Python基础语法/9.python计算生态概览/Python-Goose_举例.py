#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/1/8 14:35
# @Author : liuhuiling

#pip install goose3
# 参考资料：https://blog.csdn.net/zhusongziye/article/details/83152816
from goose3 import Goose
url = "http://www.elmundo.es/elmundo/2012/10/28/espana/1351388909.html"
g =Goose({"use_name_language":False,"target_language":"es"})
article = g.extract(url=url)
print(article.cleaned_text[:150])