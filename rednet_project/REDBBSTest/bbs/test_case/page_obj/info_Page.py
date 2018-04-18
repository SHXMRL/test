#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
@author: MRL_Z
@file: info_Page.py
@time: 2018-4-01 20:56
@subject:创建红网论坛个人信息修改测试用例
"""
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class info(Page):
    #点击设置
    info_click_loc=(By.LINK_TEXT,'设置')
    #填写姓名
    info_name_loc=(By.XPATH,'//*[@id="realname"]')
    #填写性别
    info_sex_loc=(By.XPATH,'//*[@id="gender"]/option[2]')
    #选择年份
    info_year_loc=(By.XPATH,'//*[@id="birthyear"]/option[27]')
    # 选择月份
    info_month_loc = (By.XPATH, '//*[@id="birthmonth"]/option[13]')
    # 选择天
    info_day_loc = (By.XPATH, '//*[@id="birthday"]/option[20]')
    #出生地(省)
    info_prov_loc = (By.XPATH, '//*[@id="birthprovince"]/option[28]')
    #出生地(市)
    info_city_loc = (By.XPATH, '//*[@id="birthcity"]/option[9]')
    #保存
    info_save_loc=(By.XPATH,'//*[@id="profilesubmitbtn"]/strong')
    #提交审核
    info_wait_loc = (By.XPATH, '//*[@id="td_birthday"]/p[1]/strong/a')
    def info_click(self):
        self.find_element(*self.info_click_loc).click()
    def info_name(self,name):
        self.find_element(*self.info_name_loc).send_keys(name)
    def info_sex(self):
        self.find_element(*self.info_sex_loc).click()
    def info_year(self):
        self.find_element(*self.info_year_loc).click()
    def info_month(self):
        self.find_element(*self.info_month_loc).click()
    def info_day(self):
        self.find_element(*self.info_day_loc).click()
    def info_prov(self):
        self.find_element(*self.info_prov_loc).click()
    def info_city(self):
        self.find_element(*self.info_city_loc).click()
    def info_save(self):
        self.find_element(*self.info_save_loc).click()
    def info_wait(self):
        return self.find_element(*self.info_wait_loc).text

    def infoing(self,name='李振'):
        self.open()
        # 隐性等待10秒
        self.driver.implicitly_wait(10)
        self.save_cookie()
        self.info_click()
        self.info_name(name)
        sleep(3)
        self.info_sex()
        self.info_year()
        self.info_month()
        self.info_day()
        self.info_prov()
        self.info_city()
        self.info_save()
        sleep(3)
        return self.info_wait()


