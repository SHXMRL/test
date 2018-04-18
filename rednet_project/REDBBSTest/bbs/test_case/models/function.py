#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
@author: MRL_Z
@file: login_sta.py
@time: 2018-4-01 20:56
@subject:创建红网论坛测试
"""
from selenium import webdriver
import os

def insert_img(driver,file_name):
    base_dir=os.path.dirname(os.path.dirname(__file__))
    base_dir=str(base_dir)
    base_dir=base_dir.replace("\\","/")
    base=base_dir.split('/test_case')[0]
    #print(base_dir)
    #print(base)
    file_path=base+"/report/images/"+file_name
    #print(file_path)
    driver.get_screenshot_as_file(file_path)


if __name__=="__main__":
    driver=webdriver.Chrome()
    driver.get("https://bbs.rednet.cn/forum-1813-1.html")
    insert_img(driver,'hongw.jpg')
    driver.quit()

