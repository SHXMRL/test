#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
@author: MRL_Z
@file: send_Page.py
@time: 2018-4-01 20:56
@subject:创建红网论坛发帖测试用例
"""
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class sends(Page):
    # 发帖按钮
    login_send_loc = (By.ID, 'newspecial')
    # 下拉框选择主题分类
    login_them_loc=(By.XPATH, '//*[@id="typeid_ctrl"]')
    login_them_loc2=(By.XPATH, '//*[@id="typeid_ctrl_menu"]/ul/li[8]')
    # 帖子标题
    login_title_loc = (By.ID, 'subject')
    # 帖子内容
    login_content_loc = (By.XPATH, '/html/body')
    # 发表
    login_post_loc = (By.ID, 'postsubmit')
    #发帖成功
    login_suc_loc=(By.XPATH,'//*[@id="thread_subject"]')
    #标题为空
    send_error_loc=(By.XPATH,'//*[@id="ntcwin"]/table/tbody/tr/td[2]/div/i')

    # 点击发帖
    def login_send(self):
        self.find_element(*self.login_send_loc).click()
    #选择主题
    def login_them(self):
        self.find_element(*self.login_them_loc).click()
    def login_them2(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.login_them_loc2)).click()
    #帖子标题
    def login_title(self,title):
        self.find_element(*self.login_title_loc).send_keys(title)
    #帖子内容
    def login_content(self,content):

        self.find_element(*self.login_content_loc).send_keys(content)
        
    #点击发表
    def login_post(self):
        self.find_element(*self.login_post_loc).click()

    #发帖成功
    # def login_suc(self):
    #     return self.find_element(*self.login_suc_loc).text
    #标题为空
    def send_non(self):
        return self.find_element(*self.send_error_loc).text
    #统一定义
    def sends_login(self,title='时光如旧',content='时间如白驹过隙,时光如画入目晚,物是人非,早已没有了那时的宁静祥和'):
        self.open()
        #隐性等待10秒
        self.driver.implicitly_wait(10)
        self.save_cookie()
        # 点击发帖
        self.login_send()
        #主题
        self.login_them()
        self.login_them2()
        #标题
        self.login_title(title)
        #内容
        self.switch_frame('e_iframe')
        self.login_content(content)
        #退出frame
        self.driver.switch_to_default_content()

        #发布帖子
        self.login_post()
        #sleep(3)



