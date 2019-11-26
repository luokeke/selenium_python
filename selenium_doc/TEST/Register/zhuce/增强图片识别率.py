# -*- coding: utf-8 -*-

# from pytesser import *  需要下载安装这个模块
from  PIL import ImageEnhance,Image
file_in = "11yanzhengma.png"
img = Image.open(file_in)
file_out = "2yanzhengma.png"
# print len(img.split())  # test
if len(img.split()) == 4:
    #prevent IOError: cannot write mode RGBA as BMP
    r, g, b, a = img.split()
    img = Image.merge("RGB", (r, g, b))
    img.save(file_out)
else:
    img.save(file_out)

image = Image.open('2yanzhengma.png')
#
##使用ImageEnhance可以增强图片的识别率
enhancer = ImageEnhance.Contrast(image)
image_enhancer = enhancer.enhance(4)
# a = image_to_string(image_enhancer)
print  (a)



