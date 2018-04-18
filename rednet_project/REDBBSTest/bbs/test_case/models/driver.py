#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
@author: MRL_Z
@file: driver.py
@time: 2018-4-01 20:56
@subject:创建红网论坛测试
"""
from selenium.webdriver import Remote
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
def browser():
   # lists={
   #     'http://127.0.0.1:4444/wd/hub':'chrome',
   #     'http://127.0.0.1:5555/wd/hub':'chrome',
   #     # 'http://192.168.0.109:5555/wd/hub':'chrome',
   #     # 'http://192.168.0.112:5555/wd/hub':'chrome',
   #     # 'http://192.168.0.114:5555/wd/hub':'chrome',
   #  }
   # for host,browser in lists.items():
   #     driver= Remote(command_executor=host,
   #                    desired_capabilities={'platform':'ANY',
   #                                     'browserName':browser,
   #                                     'version': '',
   #                                     'javascriptEnabled':True
   #                                    }
   #                )
    # return driver
   driver=webdriver.Chrome()
   return driver
#测试
if __name__=="__main__":
    dr=browser()
    dr.get("https://bbs.rednet.cn/forum-1813-1.html")
    dr.quit()
