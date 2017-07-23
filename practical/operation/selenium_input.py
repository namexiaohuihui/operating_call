# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: selenium_input.py
@time: 2017/6/21 0:01
"""
import os
# 这是元素输入类，传入相应的id，name，text，xpath，css以及内容就可以执行输入的指令
import sys

'''
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  -  /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                        `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

               佛祖保佑         永无BUG
'''
from practical.constant.browser.browser_establish import browser_confirm

def browser_data():
    bc = browser_confirm.__new__(browser_confirm)
    browser = bc.bro_wser()
    return browser


def id_input(id, data):
    try:
        browser = browser_data()
        ele = browser.find_element_by_id(id)
        ele.clear()
        ele.send_keys(data)
    except:
        writeLog()


def name_input(name, data):
    try:
        browser = browser_data()
        ele = browser.find_element_by_name(name)
        ele.clear()
        ele.send_keys(data)
    except:
        writeLog()


def css_input(css, data):
    try:
        browser = browser_data()
        ele = browser.find_element_by_css_selector(css)
        ele.clear()
        ele.send_keys(data)
    except:
        writeLog()


def xpath_input(xpath, data):
    try:
        browser = browser_data()
        ele = browser.find_element_by_xpath(xpath)
        ele.clear()
        ele.send_keys(data)
    except:
        writeLog()

def writeLog():
    basename = os.path.splitext(os.path.basename(__file__))[0]
    print("自己定义的_文件出现错误,名为名=%s"% \
          basename,)
    sys.exit(0)
    raise
