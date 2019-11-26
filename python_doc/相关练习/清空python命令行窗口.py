#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/22 9:40
# @Author : liuhuiling
import os               # 导入os模块
os.system('cls')        # 执行cls命令清空Python控制台
'''
参考链接：Python从菜鸟到高手（2）：清空Python控制台  https://blog.51cto.com/androidguy/2169235
在Windows下，如果要清空Windows控制台，执行cls命令即可。
cmd命令行窗口清空，直接输入cls即可

在命令上窗口输入以上内容，回车即可。
执行这两行代码，是把以前在Python控制台中输入的内容都清空了，
但在Python控制台的第1行会输出一个“0”。
其实这个“0”是os.system函数的返回值。Python控制台会输出每一条执行语句的返回值。
os.system函数如果成功执行命令，返回“0”，如果执行命令失败，返回“1”。
不过为了最求完美，现在就把这个“0”去掉。

下面的例子会编写一个Python程序，用于清空Python控制台。
清空Python控制台不输出“0”的步骤如下：

（1）导入os模块和sys模块。
（2）使用open函数以可写的方式打开一个文件，本例是out.log。
（3）为了不影响在Python控制台输出其他语句的执行结果，应先将Python默认的标准输出保存到一个变量中，
以便以后恢复默认的Python标准输出。使用sys.stdout可以获取Python标准输出的句柄（Handler）
（4）将Python标准输出指向第2步打开的文件。
（5）使用os.system函数执行cls命令。
（6）恢复Python默认的标准输出。

完整的实现代码如下。读者可以在Python控制台一行行输入这些代码，
当执行到os.system(‘cls’)语句时，Python控制台被清空，不会再显示“0”。
'''
import os                           # 导入os模块
import sys                          # 导入sys模块
f_handler=open('out.log', 'w')      # 打开out.log文件
oldstdout = sys.stdout              # 保存默认的Python标准输出
sys.stdout=f_handler                # 将Python标准输出指向out.log
os.system('cls')                    # 清空Python控制台
sys.stdout = oldstdout              # 恢复Python默认的标准输出
