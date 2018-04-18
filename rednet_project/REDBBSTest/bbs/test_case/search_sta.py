#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
@author: MRL_Z
@file: search_sta.py
@time: 2018-4-01 20:56
@subject:创建红网论坛搜索测试用例执行
"""
from time import sleep
import unittest,random,sys
#加载models目录
sys.path.append("./models")
#加载page_obj目录
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.search_Page import search

class SearchTest(myunit.MyTest):
    #测试搜索为空
    def test_search1(self):

        n=search(self.driver)
        self.assertEqual("",n.searching())
        sleep(3)
        function.insert_img(self.driver, "search1.jpg")
    #测试搜索输入的内容
    def test_search2(self):
        n=search(self.driver)
        self.assertIn("爱心",n.searching())
        sleep(3)
        function.insert_img(self.driver, "search.jpg")


if __name__=="__main__":
    unittest.main()
