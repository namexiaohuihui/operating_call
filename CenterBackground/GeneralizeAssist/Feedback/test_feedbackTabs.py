# -*- coding: utf-8 -*-
"""
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
@author:    ln_company
@license:   (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@Software:  PyCharm
@file:      test_feedbackTabs.py
@time:      2018/9/19 16:44
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import GeneralizeAssist
from CenterBackground.commoditiesJude import CommoditiesJude
from tools.excelname.Center.generalize import Generalize

basepath = os.path.split(os.path.dirname(__file__))[1]
basename = os.path.splitext(os.path.basename(__file__))[0]
basename = basepath + "-" + basename

# 传入子集的key，以及Excel文档中的sheet名字
config = GeneralizeAssist.add_key(GeneralizeAssist.feedback, GeneralizeAssist.tabs)
f_tab = CommoditiesJude(config, basename, Generalize)


class TestFeedbackTabs(unittest.TestCase):
    """
    城市tab切换用例所在地
    """
    # 定义头部button中，后面N位不需要
    BUTTON_REDUCE_NUMBER = 0

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        f_tab.openingProgram()
        f_tab._rou_background()
        f_tab.log.info("%s ---setup: 每个用例开始前后执行" % basename)
        pass

    def tearDown(self):
        f_tab.driver.quit()
        f_tab.log.info("%s ---teardown: 每个用例结束后执行" % basename)
        pass

    def test_active_tab(self):
        """
        寻找默认值
        :return:
        """
        f_tab.setFunctionName(inspect.stack()[0][3])
        f_tab.active_city('class')
        pass

    def test_already_tabs(self):
        """
        比较tabs中的全部信息
        :return:
        """
        f_tab.setFunctionName(inspect.stack()[0][3])
        f_tab.already_citys(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_switch_tab(self):
        """
        遍历点击tab
        :return:
        """
        f_tab.setFunctionName(inspect.stack()[0][3])
        f_tab.switch_city(reduce=self.BUTTON_REDUCE_NUMBER)
        pass

    def test_switch_url(self):
        """
        通过tabs的url进行切换
        :return:
        """
        f_tab.setFunctionName(inspect.stack()[0][3])
        f_tab.switch_url('class', reduce=self.BUTTON_REDUCE_NUMBER)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
