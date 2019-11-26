#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 用于生成随机数
# 对于需要却没有安装的包，可以使用 pip install 命令进行安装
import random
up = 1 # 定义正面向上为 1
down = 2 # 定义反面向上为 2
side = 3 # 定义侧面向上为 3
lunch_fate = random.randint(1, 3) # 生成的随机数n: 1 <= n <= 3
print ("生成的随机数为:", lunch_fate) # 打印生成的随机数
if lunch_fate == up:
    print ("今天午饭去吃山西刀削面吧，路上再想想面是不是需要过水吧……")
elif lunch_fate == down:
    print ("去吃炸酱面吧。这家炸酱面面有点少，不够吃啊！")
elif lunch_fate == side:
    print ("哈哈，硬币竟然真的立起来了，老天的旨意啊！黄焖鸡再贵也得去，老天最大嘛~")
else:
    pass # 不执行任何操作

#另外一个练习题
thirsty = 91 # 假设当我渴的程度不小于这个临界值时我会去接水喝
try_times = 0  # 记录到自己渴的受不了之前进行内心挣扎的次数
my_status = random.randint(1, 100) # 生成的随机数n: 1 <= n <= 100
# my_status = 20
print ("生成的随机数为:", my_status )# 打印生成的随机数
while (my_status < thirsty):
    print ("要告诉自己，我不渴我不渴我不渴……再坚持坚持啊")
    try_times = try_times + 1
    my_status = random.randint(1, 100)
    print ("生成的随机数为:", my_status )# 程序自动连接
print ("坚持了" + str(try_times) + "次这么久，还是别懒了，起来打水去吧~")