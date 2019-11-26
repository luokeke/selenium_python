#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2018/5/22 19:15
# encoding:utf-8
from PIL import Image
from removebg import RemoveBg

while True:
    print("请输入：1或2（1为只能抠图每月限制50张，2为建议照片换底:")
    gongneng = input()
    if gongneng == "1":
        while True:

            print("========================")
            dizhi = input("请输入图片地址：(退出输入0）")
            diyanse = input("请输入无或白:")
            if dizhi == "0":
                break
            else:
                # rmbg = RemoveBg("e6b2c4iZG4hzzzxU6B9MLNWP", "error.log") # 引号内是你获取的API
                rmbg = RemoveBg("U1aFbWQEDYMpPLT6ZdTeaqYK", "error.log")  # 引号内是你获取的API

                rmbg.remove_background_from_img_file(dizhi)  # 图片地址

            if diyanse == "无":
                dizhi = "0"
                break
            else:
                dizhi = dizhi + "_no_bg.png"

                im = Image.open(dizhi)
                x, y = im.size
                p = Image.new('RGBA', im.size, (255, 255, 255))
                p.paste(im, (0, 0, x, y), im)
                p.save(dizhi)

                img = Image.open(dizhi)
                # print(img.size)
                # print(img.getpixel((4,4)))

                width = img.size[0]
                height = img.size[1]
                # print("333333333333")
                for i in range(0, width):
                    for j in range(0, height):
                        data = (img.getpixel((i, j)))
                        # print(data)
                        # print(data[0])
                        if (data[0] == 255 and data[1] == 255 and data[2] == 255):  # RGBA的r值大于170，并且g值大于170,并且b值大于170

                            if diyanse == "红色":
                                img.putpixel((i, j), (225, 15, 15, 255))
                            if diyanse == "蓝色":
                                img.putpixel((i, j), (37, 129, 228, 255))
                        img = img.convert("RGB")
                        # print(dizhi+"====================")
                        img.save(dizhi)
                        # print("=========================")
                        break
                    break
    if gongneng == "2":
        while True:
            print("========================")
            i = 1
            j = 1
            a = input("请输入图片地址：(退出输入0）")
            if a == "0":
                break
            else:
                b = input("请输入红换蓝、蓝换红、白换蓝、白换红：")
                img = Image.open(a)
                # print(img.size)
                # print(img.getpixel((4,4)))

                width = img.size[0]
                height = img.size[1]
                if b == "红换蓝":
                    for i in range(0, width):
                        for j in range(0, height):
                            data = (img.getpixel((i, j)))
                            # print(data)
                            # print(data[0])
                            if (data[0] >= 180 and data[1] <= 65 and data[2] <= 65):  # RGBA的r值大于170，并且g值大于170,并且b值大于170
                                img.putpixel((i, j), (37, 129, 228, 255))

                if b == "蓝换红":
                    for i in range(0, width):
                        for j in range(0, height):
                            data = (img.getpixel((i, j)))
                            # print(data)
                            # print(data[0])
                            if (data[0] <= 60 and data[1] <= 140 and data[
                                2] >= 200):  # RGBA的r值大于170，并且g值大于170,并且b值大于170
                                img.putpixel((i, j), (225, 15, 15, 255))

                if b == "白换红":
                    for i in range(0, width):
                        for j in range(0, height):
                            data = (img.getpixel((i, j)))
                            # print(data)
                            # print(data[0])
                            if (data[0] == 255 and data[1] == 255 and data[
                                2] == 255):  # RGBA的r值大于170，并且g值大于170,并且b值大于170
                                img.putpixel((i, j), (225, 15, 15, 255))
                if b == "白换蓝":
                    for i in range(0, width):
                        for j in range(0, height):
                            data = (img.getpixel((i, j)))
                            # print(data)
                            # print(data[0])
                            if (data[0] == 255 and data[1] == 255 and data[
                                2] == 255):  # RGBA的r值大于170，并且g值大于170,并且b值大于170
                                img.putpixel((i, j), (37, 129, 228, 255))

                img = img.convert("RGB")
                img.save(a)
