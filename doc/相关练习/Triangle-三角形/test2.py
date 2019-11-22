#!/usr/bin/env python
#-*- coding:utf8 -*-
#@author: 刘慧玲  2018/5/22 19:16 
def test2():
    print("test2")

# 直角三角形判断
def ispositive(num):
    try:
        int(num)
    except:
        return False
    else:
        if int(num) <= 0 or int(num)  > 200:
            return False
        else:
            return True

def isRightTriangle(num1,num2,num3):
    if num1**2 + num2**2 == num3**2 or num1**2 + num3**2 == num2**2 or num2**2 + num3**2 == num1**2:
        return True
    else:
        return False

a = input("请输入第1个数字:")
while not ispositive(a):
    a = input("不是有效数字,请重新输入:")
b = input("请输入第2个数字:")
while not ispositive(b):
    b = input("不是有效数字,请重新输入:")
c = input("请输入第3个数字:")
while not ispositive(c):
    c = input("不是有效数字,请重新输入:")

# a = int(a)
# b = int(b)
# c = int(c)

# 判断是否可以组成三角形
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('%s,%s,%s能组成等边三角形 '%(a,b,c))
    elif a == b or a == c or b == c:
        if isRightTriangle(a,b,c):
            print('%s,%s,%s能组成等腰直角三角形'%(a,b,c))
        else:
            print('%s,%s,%s能组成等腰三角形'%(a,b,c))
    elif isRightTriangle(a,b,c):
        print('%s,%s,%s能组成直角三角形'%(a,b,c))
    else:
        print('%s,%s,%s能组成普通三角形'%(a, b, c))
else:
    print('%s,%s,%s不能组成三角形'%(a,b,c))