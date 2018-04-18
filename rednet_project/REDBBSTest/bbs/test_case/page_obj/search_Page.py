#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
@author: MRL_Z
@file: search_Page.py
@time: 2018-4-01 20:56
@subject:创建红网论坛搜索测试用例
"""
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class search(Page):
    #搜索框输入内容
    search_con_loc=(By.XPATH,'//*[@id="scbar_txt"]')
    #点击搜索
    search_cl_loc=(By.XPATH,'//*[@id="scbar_btn"]')
    #页面出现搜索内容
    search_find_loc=(By.PARTIAL_LINK_TEXT,'爱心')

    def search_con(self,content):
        self.find_element(*self.search_con_loc).send_keys(content)
    def search_cl(self):
        self.find_element(*self.search_cl_loc).click()
    #搜索的内容找到
    def search_find(self):
        return self.find_element(*self.search_find_loc).text
    #统一定义
    def searching(self,content='爱心'):
        self.open()
        sleep(5)
        self.save_cookie()
        self.search_con(content)
        self.search_cl()
        #等待,,,手动输入验证码
        sleep(5)
        return self.search_find()


