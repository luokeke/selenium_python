#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/13 9:31
# @Author : liuhuiling


import os
from PIL import Image

ext = ['png']
files = os.listdir('.')
def process_image(imagename,mwidth=270, mheight=108):
# def process_image(imagename, mwidth=270, mheight=108):
    image = Image.open(imagename)
    w, h = image.size
    new_im = image.resize(mwidth,mheight, Image.ANTIALIAS)
    new_im.save('new-' + imagename)
    new_im.close()
    # if w <= mwidth and h <= mheight:
    #     print(imagename, 'is OK.')
    #     return
    # if (1.0 * w / mwidth) > (1.0 * h / mheight):
    #     scale = 1.0 * w / mwidth
    #     new_im = image.resize((int(w / scale), int(h / scale)), Image.ANTIALIAS)
    # else:
    #     scale = 1.0 * h / mheight
    #     new_im = image.resize((int(w / scale), int(h / scale)), Image.ANTIALIAS)
    # new_im.save('new-' + imagename)
    # new_im.close()

list = ["code0.png", "code1.png", "code2.png", "code3.png", "code4.png", "code5.png", "code6.png", "code7.png","code8.png", "code9.png", ]
for image in list:
    print(image.split('.')[-1])
    if image.split('.')[-1] in ext:
        process_image(image)
