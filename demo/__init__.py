# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: __init__.py.py
@time: 2017/6/20 21:43
@项目名称:operating
"""
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

from parameter import browser_establish
from operation import selenium_input
from operation import selenium_click

one = browser_establish.browser_confirm()
_browser_ = one.call_browser()
_browser_.get("https://www.baidu.com")

selenium_input.css_input(_browser_,"input[id=kw][name=wd]","大佬")
selenium_click.css_click(_browser_,"input[type=submit][id=su]")



