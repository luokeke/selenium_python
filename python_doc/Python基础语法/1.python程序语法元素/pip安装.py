#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/21 22:33
# @Author : liuhuiling
import time
time.sleep(2)
'''
pip install selenium                #正常安装
pip install -u  selenium            #升级
pip uninstall selenium              # 卸载selenium

pip install selenium==3.11.0        #安装指定版本号

pip show selenium                   #查看当前包的版本信息

python -m pip install --upgrade pip  #升级pip
pip更多用法：https://www.cnblogs.com/mmdy0106/p/9705572.html

参考链接： 批量安装、卸载 https://blog.csdn.net/tymatlab/article/details/78738715
pip批量安装package
将需要安装的包保存在aa.txt中  可以在aa中指定版本号
cd到aa.txt所在目录，运行：
$ pip install -r aa.txt

pip批量卸载package
将需要卸载的包保存在aa.txt中
cd到aa.txt所在目录，运行：
$ pip uninstall -r aa.txt   #注意 -r

需要卸载的包可从pip freeze得到
$ pip freeze                   # 显示已安装的包名及版本
$ pip freeze > aa.txt          # 将已安装的包名及版本写入aa.txt
'''
'''
参考链接：https://blog.csdn.net/zx_water/article/details/86597500
pip安装多个模块
pip install gevent==1.4.0 sh==1.12.14 thrift==0.10.0 thrift-sasl==0.2.0
pip install gevent sh

更多参考链接： pip被玩坏了
https://www.cnblogs.com/ice-image/p/10598985.html
'''
