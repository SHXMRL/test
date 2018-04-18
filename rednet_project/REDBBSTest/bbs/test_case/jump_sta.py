#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
@author: MRL_Z
@file: jump_sta.py
@time: 2018-4-01 20:56
@subject:创建红网论坛页面跳转测试用例执行
"""
from time import sleep
import unittest,random,sys
#加载models目录
sys.path.append("./models")
#加载page_obj目录
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.jump_Page import jump

class JumpTest(myunit.MyTest):

    def test_jump2(self):

        jump1=jump(self.driver)
        self.assertEqual(jump1.jump_wh2(), "文化艺术")
        function.insert_img(self.driver, "jump.jpg")
        sleep(2)

if __name__=="__main__":
    unittest.main()