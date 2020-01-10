#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/1/8 15:19
# @Author : liuhuiling
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "Hello,World!"