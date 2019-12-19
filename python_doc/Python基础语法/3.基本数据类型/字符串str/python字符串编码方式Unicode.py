#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/26 13:34
# @Author : liuhuiling
print()
'''
python 字符串编码方式
- 统一字符编码，即覆盖几乎所有字符的编码方式
- 从0到1114111 （0x10FFFF）空间，每个编码对应一个字符
- Python字符串每个字符都是Unicode编码字符

chr(x) -- u为Unicode编码，返回其对应的字符
ord(x)  -- x为字符，返回其对应的Unicode编码
'''
print ("1+1=2"+chr(10004))  #结果：1+1=2✔
print("这个字符♉的Unicode值是："+str(ord("♉")))  # +  连接符只能连接两个字符串  这个字符♉的Unicode值是：9801
print("这个字符♉的Unicode值是：",ord("♉"))  #这个字符♉的Unicode值是： 9801  有空格
# print(ord("♉")) #9801
# print (chr(9801))  #♉
u = "白羊座、金牛座、双子座、巨蟹座、狮子座、处女座、天秤座、天蝎座、射手座、摩羯座、水瓶座、双鱼座"
list = u.split("、")
for i in range(12):
    print(list[i] + chr(9800+i) ,end="  ") #end="  "循环输出，把结尾换行变成两个空格
#结果：♉  ♊  ♋  ♌  ♍  ♎  ♏  ♐  ♑  ♒  ♓  ♔