#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
@author: MRL_Z
@file: jump_Page.py
@time: 2018-4-01 20:56
@subject:创建红网论坛登录测试用例
"""
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep
class loginPage(Page):
    #url='/'
    #点击登陆跳转登陆页面
    click_loc=(By.XPATH,'//*[@id="lsform"]/div/div/table/tbody/tr[2]/td[3]/button/em')
    #用户名输入框
    username_loc=(By.XPATH,'//input[@name="username"][1]')
    #密码输入框
    password_loc=(By.XPATH,'//input[@name="password"][1]')
    #登录按钮
    submit_loc=(By.NAME,'loginsubmit')
    def bbs_login(self):
        self.click(*self.click_loc)
    def login_username(self,username):
        self.send_keys(self.username_loc,username)
    def login_password(self,password):
        self.send_keys(self.password_loc,password)
    def login_submit(self):
        self.click(*self.submit_loc)
    #登陆
    def user_login(self,username='',password=''):
        self.open()
        self.bbs_login()
        self.login_username(username)
        self.login_password(password)
        self.login_submit()
        sleep(3)
    #用户名错误提示
    user_error_hint_loc=(By.XPATH,'//div[@class="pc_inner"]/i')
    pwd_error_hint_loc=(By.XPATH,'//div[@class="pc_inner"]/i')
    #用户名登陆成功提示
    user_login_success_loc=(By.XPATH,'//*[@id="succeedlocation"]')
    #用户名错误提示
    def user_error_hint(self):
        return self.find_element_text(*self.user_error_hint_loc)
    def pwd_error_hint(self):
        return self.find_element_text(*self.pwd_error_hint_loc)
    def user_login_success(self):
        return self.find_element_text(*self.user_login_success_loc)
