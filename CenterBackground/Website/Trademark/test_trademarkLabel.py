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
@file:      test_trademarkLabel.py
@time:      2018/9/19 16:43
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import Website
from CenterBackground.surfacejude import SurfaceJude
from tools.excelname.Center.officialwebsite import OfficialWebsite


class TestTrademarkLabel(unittest.TestCase):
    """
    页面展示项的标题
    """

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        config = Website.add_key(Website.trademark, Website.page)
        cls.t_page = SurfaceJude(config, cls.basename, InteractionController)

    def setUp(self):
        # 获取运行文件的类名
        self.t_page.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.t_page.openingProgram()
        self.t_page._rou_background()
        pass

    def tearDown(self):
        self.t_page.driver.quit()
        self.t_page.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_showSurface(self):
        """
        页面内容
        :return:test_addtrademark
        """
        self.t_page.setFunctionName(inspect.stack()[0][3])
        self.t_page.surface_execute()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
