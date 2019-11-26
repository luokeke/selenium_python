#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2019/07/24 14:25

# $ curl -H 'X-API-Key: YOUR_API_KEY'
#        -F 'image_file=@/path/to/file.jpg'
#        -f https://api.remove.bg/v1.0/removebg -o no-bg.png
#文章里示例的
from PIL import Image
from removebg import RemoveBg
import os

rmbg = RemoveBg("U1aFbWQEDYMpPLT6ZdTeaqYK","error.log")
path = '%s/picture'%os.getcwd()

for pic in os.listdir(path):
    rmbg.remove_background_from_img_file("%s\%s"%(path,pic))


im = Image.open('timg (11).jfif_no_bg.png')
x,y = im.size
try:
  # 使用白色来填充背景 from：www.jb51.net
  # (alpha band as paste mask).
  p = Image.new('RGBA', im.size, (255,255,255))
  p.paste(im, (0, 0, x, y), im)
  p.save('timg (11).04.png')
except:
  pass

# remove.bg官网给的python接口举例
import requests

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('/path/to/file.jpg', 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': 'INSERT_YOUR_API_KEY_HERE'},
)
if response.status_code == requests.codes.ok:
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)