#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
@author: MRL_Z
@file: daohang_sta.py
@time: 2018-4-01 20:56
@subject:创建红网论坛导航栏测试用例执行
"""
from time import sleep
import unittest,random,sys
#加载models目录
sys.path.append("./models")
#加载page_obj目录
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.daohang_Page import daohang

class SearchTest(myunit.MyTest):

    def test_search(self):

        n=daohang(self.driver)
        self.assertIn("学院",n.dhing())
        sleep(3)
        function.insert_img(self.driver, "dh.jpg")

if __name__=="__main__":
    unittest.main()
