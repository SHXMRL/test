#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
@author: MRL_Z
@file: jump_Page.py
@time: 2018-4-01 20:56
@subject:创建红网论坛页面跳转测试用例
"""
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class jump(Page):
    #点击文化跳转至文化艺术页面
    jump_wh_loc=(By.XPATH,'// *[@id="hd"]/div/div[6]/ul/li[5]/a')
    #页面跳转成功
    jump_wh1_loc=(By.XPATH,'//*[@id="ct"]/div/div[1]/div/div[1]/h2/a')
    def jump_wh(self):
        self.find_element(*self.jump_wh_loc).click()
    def jump_wh1(self):
        return self.find_element(*self.jump_wh1_loc).text


    def jump_wh2(self):
        self.open()
        # 隐性等待10秒
        self.driver.implicitly_wait(10)
        self.save_cookie()
        self.jump_wh()
        return self.jump_wh1()




