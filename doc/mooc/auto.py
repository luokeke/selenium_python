#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/28 11:33
# @Author : liuhuiling

from w import  Widget
import unittest
# 执行测试的类
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()
    def testSize(self):
        self.assertEqual(self.widget.getSize(), (40, 40))
    def tearDown(self):
        self.widget = None
# 构造测试集
    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(WidgetTestCase("testSize"))
        return suite
if __name__ == "__main__":
    unittest.main(defaultTest = 'suite')