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
@file:      test_fixedpointLable.py.py
@time:      2018/9/11 17:28
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import MovementUser
from CenterBackground.Commodities.soldLable import SoldLable
from tools.excelname.Center.consumers import Consumers

_box = 'box'
_tabs = 'tabs'
class TestStoreLable(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        config = MovementUser.add_key(MovementUser.fixedPoint, MovementUser.page)
        cls.sLable = SoldLable(config, cls.basename, Consumers)

    def setUp(self):
        # 获取运行文件的类名
        self.sLable.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.sLable.openingProgram()
        self.sLable._rou_background()
        pass

    def tearDown(self):
        self.sLable.driver.quit()
        self.sLable.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_showTitle(self):
        self.sLable.setFunctionName(inspect.stack()[0][3])
        self.sLable.title_execute()
        pass

    def test_showSurface(self):
        self.sLable.setFunctionName(inspect.stack()[0][3])
        self.sLable.INSERTION_SITE = 2
        self.sLable.surface_execute()
        pass

    def test_affiliatedTitle(self):
        self.sLable.setFunctionName(inspect.stack()[0][3])
        self.sLable.designated_tab_box(_tabs, 3)
        self.sLable.title_execute()
        pass

    def test_affiliatedSurface(self):
        self.sLable.setFunctionName(inspect.stack()[0][3])
        self.sLable.INSERTION_SITE = -1
        self.sLable.designated_tab_box(_tabs, 3)
        self.sLable.surface_execute()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
