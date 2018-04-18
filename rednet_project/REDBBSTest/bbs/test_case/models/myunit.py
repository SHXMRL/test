#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
@author: MRL_Z
@file: myunit.py
@time: 2018-4-01 20:56
@subject:创建红网论坛测试
"""


from .driver import browser
import unittest
import os
class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver=browser()
        #self.url='https://bbs.rednet.cn/forum-1813-1.html'
        self.driver.implicitly_wait(10)
        # self.title='昙花一现'
        # self.content='语言是行动的花朵'


        #self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()