#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
@author: MRL_Z
@file: ainfo_sta.py
@time: 2018-4-01 20:56
@subject:创建红网论坛个人信息修改测试用例执行
"""
from time import sleep
import unittest,random,sys
#加载models目录
sys.path.append("./models")
#加载page_obj目录
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.info_Page import info

class InfoTest(myunit.MyTest):

    def test_info(self):

        ju=info(self.driver)
        self.assertEqual(ju.infoing(),"我提交的内容")
        function.insert_img(self.driver, "info.jpg")
        sleep(3)

if __name__=="__main__":
    unittest.main()