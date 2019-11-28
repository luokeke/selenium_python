#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/20 18:07
# @Author : liuhuiling

name = "菲菲" # 字符类型：内容要由"或者'包裹
age = 18 # 数字类型
print("我叫 %s 今年 %d" % (name,age))
print('应发奖金为:', 3 , '(元)')

'''
print 单纯打印  参考链接：https://www.cnblogs.com/yssshiny/p/10833247.html
1)不带引号：让计算机读懂括号里面的内容，打印最终结果
print(1+2) # 3 ， 数字计算   
2)带引号：让计算机无需理解，原样复述引号中的内容，可以输出内容中的双引号
print('我是一只自由的"小鸟"')# 结果：我是一只自由的"小鸟"
3）带双引号：让计算机无需理解，原样复述引号中的内容，可以输出内容中的单引号
print("Let's piay") #  Let's piay
4)带三个单引号或三个双引号  多用来表示python的注释 '''
"""
print('''
这一周过的真快，
再过两天就是周日了，
又可以睡懒觉了！
''')
结果：
这一周过的真快，
再过两天就是周日了，
又可以睡懒觉了！
"""
for i in range (2,4):
    print("输出",i)
    '''     输出 2
            输出 3  结果带有默认的分隔符 空格  '''
for i in range(2, 4):
    print("输出"+ str(i))
    '''把int转换成str
            输出2
            输出3 用连接符+  分隔符 空格 消失'''
for i in range(3):
    print("输出",i,sep="$")
    ''' 输出$0
        输出$1
        输出$2   分隔符 空格 变为 $ '''
for i in range(3):
    print("输出",i,end="$")  #输出 0$输出 1$输出 2$
'''
print 默认的分隔符 空格，及 去掉默认分隔符方法   参考链接：神奇的print函数：https://blog.csdn.net/weixin_33894992/article/details/85120575
print("a","b","c","d","e");输出结果：a b c d e   
print("name =", "Bill")  输出结果如下：name = Bill
很明显是将这5个字符首尾相接输出了。不过这些字母之间用空格分隔，这是print函数默认的分隔符，用于分隔输出的多个参数值，

去掉默认分隔符：
1.用拼接符号 + 
2. sep="," ，可以将分隔符从空格改成逗号（,） print函数特有的方法
print("Apple", "Orange","Banana", sep=",")   输出结果：Apple,Orange,Banana
3.end=" " ，让最后一个输出字符串结尾符变成空格，而不是原来的“\n”'''

'''
print("a",end="");
print("b",end="");
print("c");                输出结果：abc
print("a",end="。");
print("b",end="。");
print("c");                输出结果：a。b。c
'''

'''
print  不同类型数据穿插 三种拼接方式  见selenium3 18页
1.用连接符 + 进行拼接  不推荐 占用多个内存 ； 连接符只能连接两个字符串
2.通过格式符/占位符 %s %d %r 替换 ，%s 指定字符串，%d用于指定数字，%r 用于不确定打印数据的类型, %f浮点数  
    更多参考python格式化字符.py  推荐 
3.格式化函数format()  推荐,程序员推荐 更多用法参见format函数
'''
name='玲玲'
age = 29
print("name is : "+name+', age is : '+str(age)) #age是int类型，需要先用str()函数转换为字符串
print("name is : %s, age is : %d "%(name,age))
print("name is : {}, age is : {}  " .format(name,age))
#结果均为：name is : 玲玲, age is : 29
'''print 用fromat()函数格式化'''
C = 3.023
print("转换后的温度值为：{: 2f}".format(C))
# format还能这样用 推荐
name = input("name:")
age = input('age:')
job = input('job:')
str3 = '''
    ------- hello word {0} -------
    Name:{0}
    Age:{1}
    Job:{2}
''' .format(name,age,job)
print(str3)

''' 参考链接：https://www.cnblogs.com/codescrew/p/8645902.html'''
# 数字 %d
print("一共 %d 个站点"%(2))
#打印浮点数%0.2f
print("i am %0.2f m" %1.785)  #打印浮点数%0.2f   打印结果为i am 1.78 m
#打印百分比 %0.2f %%
print("it is %0.2f %%" %99.852)  #  打印结果为it is 99.85 %
# 打印字符串 %s
print( "我叫 %s,my blogs is %s" % ("CodeScrew","www.cnblogs.com/codescrew"))
# 使用键值对进行拼接
print("我叫 %(name)s.  今年 %(age)d" % ({"name":"CodeScrew","age":23}))  #打印结果为i am CodeScrew.my age is 23
# format函数处理字符串
#  除了%号进行拼接，还可以使用字符串类的format函数，以下列举了常用的使用。
print("我叫 {},今年 {}".format("CodeScrew",23))  #打印结果为i am CodeScrew,age is 23
print( "我叫 {1},今年 {0}".format("CodeScrew",23))#打印结果为i am 23,age is CodeScrew
print("我叫 {name},今年 {age}".format(name="CodeScrew",age=23))  #打印结果为i am CodeScrew,age is 23
print( "我叫 {name},今年 {age}".format(**{"name":"CodeScrew","age":23}))  #打印结果为i am CodeScrew,age is 23
print( "我叫 {:s},今年 {:d}".format("CodeScrew",23))  #打印结果为i am CodeScrew,age is 23
print("我叫{:s},今年 {:d}".format(*["CodeScrew",23]))  #打印结果为i am CodeScrew,age is 23
print("Numbers:{:b},{:o},{:d},{:x},{:X}".format(15,15,15,15,15))  #打印结果为Numbers:1111,17,15,f,F




