# -*- coding:utf8 -*-


"""
@author: MJ
@file: test_baidu.py
@time: 2017-10-16 19:01
Project:登录百度测试用例
"""
from selenium import webdriver
import unittest, time

class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30) #隐性等待时间为30秒
        self.base_url = "https://www.baidu.com"

    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        title=driver.title
        self.assertEqual(title, "unittest_百度搜索")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()