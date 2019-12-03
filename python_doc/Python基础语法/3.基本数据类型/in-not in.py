#!/usr/bin/python
# -*- coding: UTF-8 -*-

todo_list = ['培训', '交作业', '吃午饭']
print ("培训" in todo_list )# True
print ("打麻将" in todo_list )# False
print ("吃午饭" not in todo_list) # False

print (len(todo_list))

alphabets = 'abcdefghijklmnopqrstuvwxyz'
print ("2" in alphabets )# False
print ("Q" in alphabets)
print ("lmnopqrst" in alphabets) # True
print ("ac" in alphabets) # False

print (len(alphabets))

name = "Tsz"
print (name.upper())