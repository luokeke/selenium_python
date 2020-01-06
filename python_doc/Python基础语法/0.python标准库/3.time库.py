#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/26 17:27
# @Author : liuhuiling
import time
"""
--获取时间：time() ctime() gmtime() localtime()
--时间格式化：strftime() strptime()
--程序计时：sleep() perf_counter()


-------获取时间 -------
-- time()  获取当前时间戳，即计算机内部的时间值，是浮点数
-- ctime() 获取当前时间，并以易读方式返回，返回字符串
-- gmtime() 获取UTC时区（0时区）的struct_time，表示计算机可处理的时间格式
        需要注意的是，我们计算机显示的是东八区时间（+8），所以的得到的struct_time+8即为现在计算机显示的时间（按照所处不同时区计算）。
-- localtime() 获取本地时区(我们是东八区)的struct_time，注意gmtime和localtime获取时区不同
"""
print(time.time()) #1574761388.243139
print(time.ctime()) #Tue Nov 26 17:43:08 2019
print(time.gmtime()) #time.struct_time(tm_year=2019, tm_mon=11, tm_mday=26, tm_hour=9, tm_min=45, tm_sec=15, tm_wday=1, tm_yday=330, tm_isdst=0)
time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
"""
-------时间格式化 -------
-- strftime(format,t)  format 是格式化模板字符串，用来定义输出效果，t是计算机内部时间变量
-- strptime(string,format) string 是字符串形式的时间值，format是格式化模板字符串，用来定义输入效果

t=time.gmtime()
print(time.strftime("%Y-%m-%d %H:%M:%S",t)) #2019-11-26 09:48:36  注意大小写

strftime(format,t)   strptime(string,format)  互补，效果刚好相反。

时间格式化控制符：
格式化字符串    日期/时间说明     值范围和实例
%Y              年份              0000-9999，例如：1900
%m              月份              01-12例如：10
%d              日期              01-31 例如：25
%H              小时（24h制）     00-23，例如：22
%M              分钟              00-59，例如：26
%S              秒                00-59，例如：28

%B              月份名称          January-December，例如：April
%b              月份缩写          jan-Dec，例如：Apr
%A              星期              Monday-Sunday，例如：Wednesday
%a              星期缩写          Mon-Sun,例如：Wed
%I              小时（12h制）     01-12，例如：7
%p              上/下午            AM,PM,例如：PM
"""
t=time.gmtime()
print(time.strftime("%Y-%m-%d %H:%M:%S",t)) #2019-11-27 01:24:56  注意大小写
timeStr = '2019-11-26 09:48:36'
print(time.strptime(timeStr,"%Y-%m-%d %H:%M:%S"))
#time.struct_time(tm_year=2019, tm_mon=11, tm_mday=26, tm_hour=9, tm_min=48, tm_sec=36, tm_wday=1, tm_yday=330, tm_isdst=-1)
'''
------   程序计时 ------
--  指测量起止动作所经历时间的过程
--  测量时间 perf_counter() 返回一个CPU级别的精确时间计数值，单位为秒，由于这个计数值
    起点不确定，连续调用差值才有意义 
--  产生时间 sleep(s) s 拟休眠的时间，单位是秒，可以是浮点数。
'''
#定义一个起始时间，后面的每一次调用都是基于最开始一次调用的时间之后，两次差值得到流逝时间
start = time.perf_counter()
end = time.perf_counter()
print(end - start)
time.sleep(3.3) #休眠3.3秒
