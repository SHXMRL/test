#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
@author: MRL_Z
@file: getcookie.py
@time: 2018-4-01 20:56
@subject:创建红网论坛登录测试用例
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

base_url="https://bbs.rednet.cn/forum-1813-1.html"
browser=webdriver.Chrome()
browser.implicitly_wait(10)
browser.get(base_url)
browser.find_element(By.ID,"ls_username").send_keys('15686049638')
browser.find_element(By.ID,"ls_password").send_keys('P136y9638THON')
sleep(2)
browser.find_element(By.CSS_SELECTOR,"#lsform > div > div > table > tbody > tr:nth-child(2) > td.fastlg_l > button").click()
s=browser.get_cookies()
print(s)
for n in s:
    browser.add_cookie(n)
browser.refresh()