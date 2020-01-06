#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/1/6 14:02
# @Author : liuhuiling
import os
libs = {"numpy","matplotlib","pillow","sklearn","requests"}
for lib in libs:
    try:
        os.system("pip install"+lib)
        print("Successful")
    except:
        print("Failed Somhow")