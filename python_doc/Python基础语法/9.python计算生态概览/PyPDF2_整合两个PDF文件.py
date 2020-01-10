#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/1/8 10:16
# @Author : liuhuiling

from PyPDF2 import PdfFileReader,PdfFileMerger
merger = PdfFileMerger()
input1 = open("","rb")
input2 = open("","rb")
merger.append(fileobj= input1,page = (0,3))
merger.merge(position= 2, fileobj= input2, pages=(0,1))
output = open("","wb")
merger.write(output)
