#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
@author: MRL_Z
@file: base.py
@time: 2018-4-01 20:56
@subject:创建红网论坛测试
"""
'''
页面基础类，用于所有页面的继承,根据情况自行增加
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import json,os
from time import sleep
class Page(object):
    bbs_url="https://bbs.rednet.cn/forum-1813-1.html"
    def __init__(self,selenium_driver,base_url=bbs_url,parent=None):
        self.base_url=base_url
        self.driver=selenium_driver
        self.timeout=30
        self.parent=parent
    def _open(self,url):
        #url=self.base_url
        self.driver.get(url)
        #使用断言打开页面
        assert self.on_page(), "无法打开%s" % url
    #点击
    def click(self, *loc):
        self.driver.find_element(*loc).click()
    #元素定位
    def find_element(self,*loc):
        return self.driver.find_element(*loc)
    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)
    #定位文本
    def find_element_text(self, *loc):
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(loc))
        return self.driver.find_element(*loc).text
    #打开网页
    def open(self):
        self._open(self.base_url)
    def on_page(self):
        return self.driver.current_url == (self.base_url)
    #滑动滚动条
    def scripts(self,src):
        return self.driver.execute_script(src)
    # 鼠标悬停
    def move_element(self,*loc):
        element = self.driver.find_element(*loc)
        ActionChains(self.driver).move_to_element(element).perfrom()

# 重写switch_frame方法
    def switch_frame(self, loc):
        self.driver.switch_to.frame(loc)

#重写定义send_keys方法
    def send_keys(self, loc, vaule, clear_first=True, click_first=True):
        try:
            print("使用send_keys")
            #loc = getattr(self,"_%s"% loc)  #getattr相当于实现self.loc
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            print ("%s 页面中未能找到 %s 元素"%(self, loc))
#读取cookie
    def save_cookie(self):
        self.driver.delete_all_cookies()
        with open('save_cookie.txt','r',encoding='utf8') as f:
            s=eval(f.read())
            #print(s)
        for n in s:
            self.driver.add_cookie(n)
        self.driver.refresh()
        sleep(3)

