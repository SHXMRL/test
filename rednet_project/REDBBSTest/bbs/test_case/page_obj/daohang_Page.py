#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
@author: MRL_Z
@file: daohang_Page.py
@time: 2018-4-01 20:56
@subject:创建红网论坛导航栏测试用例
"""
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class daohang(Page):
    #高校论坛
    dh_gx_loc=(By.LINK_TEXT,'高校论坛')
    #我的大学
    dh_mys_loc=(By.XPATH,'//*[@id="lf_521"]/dd[1]/a')
    #出现大学名字
    dh_find_loc = (By.PARTIAL_LINK_TEXT, '学院')

    def dh_gx(self):
        self.find_element(*self.dh_gx_loc).click()
    def dh_mys(self):
        self.find_element(*self.dh_mys_loc).click()
    def dh_find(self):
        return self.find_element(*self.dh_find_loc).text

    def dhing(self):
        self.open()
        sleep(5)
        self.save_cookie()
        self.dh_gx()
        self.dh_mys()
        return self.dh_find()



