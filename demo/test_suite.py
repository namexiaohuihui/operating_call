# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: test_suite.py
@time: 2017/7/16 16:28
@项目名称:operating
"""

from selenium import  webdriver


class demo:
    def __init__(self):
        print("开始呢？、、")

    def browser(self):
        import os
        # 实现全局变量的引用
        firefoxBin = os.path.abspath(r"E:\Program Files\Mozilla Firefox\firefox.exe")
        os.environ["webdriver.firefox.bin"] = firefoxBin

        # 代码加载火狐驱动
        firefoxgeckobdriver = os.path.abspath(r"E:\drivers\Drivers\geckodriver64.exe")

        self.browser = webdriver.Firefox(executable_path=firefoxgeckobdriver)
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

        self.browser.get("file:///C:/Users/70486/Desktop/demo.html")
    def nihaoma(self):
        print("我不好")

if __name__ == '__main__':
    a = 1
    b = 1
    assert  a != b , "1"