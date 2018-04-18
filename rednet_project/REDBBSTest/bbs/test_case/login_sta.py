#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
@author: MRL_Z
@file: login_sta.py
@time: 2018-4-01 20:56
@subject:创建红网论坛登录测试用例执行
"""
from time import sleep
import unittest,random,sys
#sys.path是一个列表,加载models目录
sys.path.append('./models')
#加载page_obj目录
sys.path.append('./page_obj')
from models import function,myunit,driver
from page_obj.login_Page import loginPage
class loginTest(myunit.MyTest):
    def user_login_verify(self,username='',password=''):
        loginPage(self.driver).user_login(username,password)
    #测试用户名密码为空
    def test_login1(self):
        po=loginPage(self.driver)
        po.user_login()
        self.assertIn('抱歉，密码空或包含非法字符',po.user_error_hint())
        function.insert_img(self.driver,'user_empty.png')
    #测试用户名密码错误
    def test_login2(self):
        character=random.choice('abcdefghijklmnopqrstuvwxyz')
        username='15686049638'+character
        password='db1142gfdbcs'
        po=loginPage(self.driver)
        po.user_login(username=username,password=password)
        self.assertIn('登录失败，您还可以尝试',po.pwd_error_hint())
        function.insert_img(self.driver,'user_pwd_error.jpg')
    #登陆成功
    def test_login3(self):
        self.user_login_verify(username='15686049638',password='P136y9638THON')
        po=loginPage(self.driver)
        self.assertEqual(po.user_login_success(),'欢迎您回来，论坛新兵 15686049638，现在将转入登录前页面')
        function.insert_img(self.driver,'login_success.jpg')
if __name__=="__main__":
    unittest.main()
