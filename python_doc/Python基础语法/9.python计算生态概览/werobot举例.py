#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/1/9 14:19
# @Author : liuhuiling
'''
WeRoBot     微信公众号开发框架
    提供了解析微信服务器消息及反馈消息的功能
    建立微信机器人的重要技术手段
    pip install werobot
    https://github.com/offu/WeRoBot
'''

#对微信每个消息反馈一个Hello World!
import werobot
robot = werobot.WeRoBot(token="tokenhere")
@robot.handler
def hello(message):
    return 'Hello World!'