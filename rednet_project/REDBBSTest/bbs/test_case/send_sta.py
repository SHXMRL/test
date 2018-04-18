#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
@author: MRL_Z
@file: send_sta.py
@time: 2018-4-01 20:56
@subject:创建红网论坛发帖测试用例执行
"""
from time import sleep
import unittest,random,sys
#加载models目录
sys.path.append("./models")
#加载page_obj目录
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.send_Page import sends

class SendTest(myunit.MyTest):
    #测试不填写标题及内容时发表帖子
    def test_send1(self,title='',content=''):
        send_page=sends(self.driver)
        send_page.sends_login(title,content)
    #测试填写标题不填写内容发表帖子
    def test_send2(self):
        self.test_send1(title='时光如旧',content='')
        sleep(3)
        po = sends(self.driver)
        self.assertEqual(po.send_non(),"抱歉，您尚未输入标题或内容")
        function.insert_img(self.driver, "send1.jpg")
        sleep(3)

    #测试不填写标题填写内容发表帖子
    def test_send3(self):
        self.test_send1(title='',content='时间如白驹过隙,时光如画入目晚,物是人非,早已没有了那时的宁静祥和')
        sleep(3)
        po = sends(self.driver)
        self.assertEqual(po.send_non(),"抱歉，您尚未输入标题或内容")
        function.insert_img(self.driver, "send2.jpg")
        sleep(3)
   #测试填写标题及内容后发表帖子
    def test_send4(self):
        self.test_send1(title='时光如旧',content='时间如白驹过隙,时光如画入目晚,物是人非,早已没有了那时的宁静祥和')
        sleep(3)
        po = sends(self.driver)
        self.assertEqual(po.login_post(), "时光如旧")
        function.insert_img(self.driver, "send.jpg")
        sleep(3)


if __name__=="__main__":
    unittest.main()
