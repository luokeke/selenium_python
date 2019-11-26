#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/20 14:30
# @Author : liuhuiling
from PIL import Image
import qrcode
def first_demo():#生成二维码图片
    qr = qrcode.make('Hello World')# 存储的字符串
    qr.get_image().show()
def second_demo():#把生成二维码图片保存到本地
    text = 'Python专栏'
    qr = qrcode.make(text)
    qr.save('imgcode.png')# 需要传一个参数 文件名
    qr.show()
# first_demo()
# second_demo()
def create_icon_qrcode():#使用qrcode库生成带有内嵌图片的二维码
    qr = qrcode.QRCode(
        version=1,# 二维码size尺寸大小。官方称为version
        error_correction=qrcode.constants.ERROR_CORRECT_H,# 二维码错误处理级别，有四种方式，稍后给出解释
        box_size=10,# 二维码图片的大小
        border=2# 二维码白色边框的大小
    )
    qr.add_data(u'♥＾▽＾♥')# 添加数据
    qr.make(fit=True) # 填充数据
    img = qr.make_image(fill_color='grey',back_color='white') # 生成二维码图片 指定填充颜色 指定背景颜色
    img_w,img_h = img.size# 得到生成的二维码图片的宽，高
    icon = Image.open('12.png')# 添加图片到二维码中，使用pillow的Image打开图片
    factor = 3# 设置icon的大小,为二维码图片大小的6分之一
    size_w = img_w // factor
    size_h = img_h // factor
    icon_w,icon_h = icon.size# 得到icon图片的大小
    # 只有当我们icon图片的大小超过了二维码图片的3分之一的时候，才对icon图片大小重新定义大小。
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w,icon_h),Image.ANTIALIAS) # 重新设置icon的尺寸
    w =  (img_w - icon_w) // 2 # 得到在二维码中显示的位置，坐标。
    h =  (img_h - icon_h) // 2
    img.paste(icon,(w,h),mask=None)
    img.save('1214.png')
create_icon_qrcode()