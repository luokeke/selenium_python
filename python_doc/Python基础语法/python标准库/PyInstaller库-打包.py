#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/3 13:57
# @Author : liuhuiling
'''
PyInstaller库概述
- 将.py源代码转换成无需源代码的可执行文件
                                    - Windows(exe文件)
.py文件   ---->  PyInstaller  --->  - Linux
                                    - Mac OS X
PyInstaller库是第三方库
- 官方网站 ： http://www.pyinstaller.org
- 第三方库 ： 使用前需要额外安装
- 安装第三方库需要使用pip工具 pip install pyinstaller

使用说明：
cmd命令行：pyinstaller -F <文件名.py>
会生成三个文件夹 __pycache__  build dist 其中  __pycache__ build  可以安全的删除
dist里可以找到与源文件同名的exe文件
举例：
cmd进入 E:\GITHUB\selenium_python\python_doc\相关练习\打包成exe文件\
pyinstaller -F "sevendigitdraw.py"
参数              描述
-h                  查看帮助
--clean             清理打包过程中的临时文件
-D,--onedir         默认值，生成dist文件夹，文件夹中所有文件都需要
-F,--onefile        在dist文件夹中只生成独立的打包文件
-i<图标文件名.io>    指定打包程序使用的图标(icon)文件

'''