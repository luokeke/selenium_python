#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/13 9:44
# @Author : liuhuiling

from PIL import Image
def produceImage(file_in, width, height):
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save('new-'+file_in)
list = ["code0.png", "code1.png", "code2.png", "code3.png", "code4.png", "code5.png", "code6.png", "code7.png","code8.png", "code9.png", ]
for file_in in list:
    produceImage(file_in, 278, 108,)

