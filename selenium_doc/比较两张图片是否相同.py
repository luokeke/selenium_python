#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/13 13:59
# @Author : liuhuiling


from PIL import ImageChops
from PIL import Image
import math
import operator
from functools import reduce

# 适用于对比两张图片是否完全相同
# 需要两张图片的大小完全一致
def compare_images(path_one, path_two):
    """
    比较图片
    :param path_one: 第一张图片的路径
    :param path_two: 第二张图片的路径
    :return: 相同返回 success
    """
    image_one = Image.open(path_one)
    image_two = Image.open(path_two)
    try:
        diff = ImageChops.difference(image_one, image_two)
        if diff.getbbox() is None:
            # 图片间没有任何不同则直接退出
            return "success"
        else:
            return "ERROR: 匹配失败！"
    except ValueError as e:
        return "{0}\n{1}".format(e, "图片大小和box对应的宽度不一致!")


# 如果两张图片完全相等，则返回结果为浮点类型“0.0”，如果不相同则返回结果值越大。
def image_contrast(img1, img2):
  image1 = Image.open(img1)
  image2 = Image.open(img2)
  h1 = image1.histogram()
  h2 = image2.histogram()
  result = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
  return result


list2 = ["new-code0.png", "new-code1.png", "new-code2.png", "new-code3.png", "new-code4.png", "new-code5.png",
        "new-code6.png", "new-code7.png", "new-code8.png", "new-code9.png"]
# img1 = "JDJRV-bigimg.png" # 指定图片路径
# for image in list2:
#     img2 =image
#     print(image_contrast(img1,img2))

#从一堆图片里找出跟样本图片最像的一张图
def image_contrast(img1):
    list1 = ["new-code0.png", "new-code1.png", "new-code2.png", "new-code3.png", "new-code4.png", "new-code5.png",
             "new-code6.png", "new-code7.png", "new-code8.png", "new-code9.png"]
    for img2 in list1 :
        image1 = Image.open(img1)
        image2 = Image.open(img2)
        h1 = image1.histogram()
        h2 = image2.histogram()
        # 如果两张图片完全相等，则返回结果为浮点类型“0.0”，如果不相同则返回结果值越大。
        result = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
        if result < 100:
            return img2

img1 = "JDJRV-bigimg.png" # 指定图片路径
print(image_contrast(img1))
kl = Image.open(image_contrast(img1))
