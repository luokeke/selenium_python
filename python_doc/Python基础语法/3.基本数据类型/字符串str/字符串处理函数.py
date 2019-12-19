#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/26 12:00
# @Author : liuhuiling
type(str)
'''
python 字符串编码方式
- 统一字符编码，即覆盖几乎所有字符的编码方式
- 从0到1114111 （0x10FFFF）空间，每个编码对应一个字符
- Python字符串每个字符都是Unicode编码字符

len(x)  --  长度，返回字符串x的长度 数字标点符号英文字母汉字都是一个字符，长度相同

str(x)  -- 任意类型x所对应的字符串形式；任意类型x增加引号，使它变为字符串，
eval(x) -- 去掉字符串x两侧的引号，使它变为python可以运行的类型或语句

hex(x)/oct(x)  -- 整数x的十六进制或八进制小写形式字符串

chr(x) -- u为Unicode编码，返回其对应的字符
ord(x)  -- x为字符，返回其对应的Unicode编码
'''
