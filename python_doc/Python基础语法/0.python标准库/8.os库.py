#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/1/3 9:48
# @Author : liuhuiling
print()
'''
os库提供通用的、基本的操作系统交互功能
    路径操作：os.path子库，处理文件路径及信息
    进程管理：启动系统中其他程序
    环境参数：获得系统软件硬件信息等环境参数

路径操作  import os.path
os.path子库里path为入口，用于操作和处理文件路径

os.path.abspath(path)       返回path在当前系统中的绝对路径
os.path.relpath(path)       返回当前程序与文件之前的相对路径
os.path.dirpath(path)       返回path中的目录名称
os.path.basepath(path)      返回path中最后的文件名称
os.path.join(path,*paths)   组合path与paths，返回一个路径字符串
os.path.normpath(path)      归一化path的表示形式，统一用\\分隔路径 （不是用\\分隔的）
os.path.normcase(path)      统一小写及用\\分隔路径

os.path.exists(path)        判断path对应文件或目录是否存在，返回True或False
os.path.isfile(path)        判断path所对应是否为已存在的文件，返回True或False
os.path.isdir(path)         判断path所对应是否为已存在的目录，返回True或False

os.path.getatime(path)      返回path对应文件或目录上一次的访问时间 a access
os.path.getmtime(path)      返回path对应文件或目录最近一次的修改时间 m modify
os.path.getctime(path)      返回path对应文件或目录的创建时间 c create
os.path.getsize(path)       返回path对应文件的大小，以字节为单位

进程管理 import os
os.system(command)执行程序或命令command
os.system("c:\\windows\\system32\\calc.exe")  运行正确返回0

环境参数  获取或改变操作系统环境信息
os.chdir(path)      修改当前程序操作的路径
os.getcwd()         返回程序的当前路径
os.getlogin()       获得当前系统登录用户名
os.cpu_count()      获得当前系统的cpu数量
os.urandom(n)       获得n个字节长度的随机字符串，通常用于加密解密运算

'''
import os.path
t = os.path.normcase("C://Windows//System32//calc.exe")
m = os.path.normpath("C://Windows//System32//calc.exe")
print(t) #c:\\windows\\system32\\calc.exe
print(m) #C:\Windows\System32\calc.exe



