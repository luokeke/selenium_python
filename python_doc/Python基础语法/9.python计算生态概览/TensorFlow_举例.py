#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/1/8 10:54
# @Author : liuhuiling
import tensorflow as tf
init = tf.global_varibales_initializer()
sess = tf.Session()
sess.run(init)
res = sess.run(result)
print("result",res)