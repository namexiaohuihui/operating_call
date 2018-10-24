# -*- coding: utf-8 -*-
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
@author:  ln_company
@license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@software: PyCharm
@file: platformTabs.py
@time: 2018/8/20 16:08
@desc:
'''
import os
import inspect
import unittest
from CenterBackground import Commodities
from CenterBackground.commoditiesJude import CommoditiesJude
from tools.excelname.Center.bundledItems import BundledItems

basename = os.path.splitext(os.path.basename(__file__))[0]
# 传入子集的key，以及Excel文档中的sheet名字
config = Commodities.add_key(Commodities.platform, Commodities.city)
cJude = CommoditiesJude(config, basename, BundledItems)


class TestPlatformTabs(unittest.TestCase):
    # 定义头部button中，后面2位不需要
    BUTTON_REDUCE_NUMBER = 2

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        cJude.openingProgram()
        cJude._rou_background()
        print("%s ---setup: 每个用例开始前后执行" % basename)

    def tearDown(self):
        cJude.driver.quit()
        print("%s ---teardown: 每个用例结束后执行" % basename)
        pass

    def test_active_city(self):
        cJude.setFunctionName(inspect.stack()[0][3])
        cJude.active_city()
        pass

    def test_active_code(self):
        cJude.setFunctionName(inspect.stack()[0][3])
        cJude.active_code()
        pass

    def test_already_citys(self):
        cJude.setFunctionName(inspect.stack()[0][3])
        cJude.already_citys(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_already_codes(self):
        cJude.setFunctionName(inspect.stack()[0][3])
        cJude.already_codes(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_switch_city(self):
        cJude.setFunctionName(inspect.stack()[0][3])
        cJude.switch_city(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_switch_url(self):
        cJude.setFunctionName(inspect.stack()[0][3])
        cJude.switch_url(reduce=self.BUTTON_REDUCE_NUMBER)
        pass