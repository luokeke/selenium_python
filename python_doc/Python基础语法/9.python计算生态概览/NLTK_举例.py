#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/1/8 10:28
# @Author : liuhuiling
# import nltk
# nltk.download('treebank')
from nltk.corpus import treebank
t = treebank.parsed_sents("wsj_0001.mrg")[0]
t.draw()