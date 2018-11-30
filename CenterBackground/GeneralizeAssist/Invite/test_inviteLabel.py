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
@file:      test_inviteLabel.py
@time:      2018/9/19 16:43
@desc:
"""
import os
import inspect
import unittest

from CenterBackground import GeneralizeAssist
from CenterBackground.surfacejude import SurfaceJude
from tools.excelname.Center.generalize import Generalize


class TestInviteLabel(unittest.TestCase):
    """
    页面展示项的标题
    """

    INVITE_DESIGNATED_BOX = "邀请人管理"

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename

        # 传入子集的key，以及Excel文档中的sheet名字
        config = GeneralizeAssist.add_key(GeneralizeAssist.invite, GeneralizeAssist.page)
        cls.i_label = InviteOperateJude(config, cls.basename, Generalize)

        cls.INVITE_DESIGNATED_TABS = cls.i_label.bi.yaml_tabs()

    def setUp(self):
        # 获取运行文件的类名
        self.i_label.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.i_label.openingProgram()
        self.i_label._rou_background()

    def tearDown(self):
        self.i_label.driver.quit()
        self.i_label.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_showTitle(self):
        self.i_label.setFunctionName(inspect.stack()[0][3])
        self.i_label.title_execute()
        pass

    def test_showSurface(self):
        self.i_label.setFunctionName(inspect.stack()[0][3])
        self.i_label.surface_execute()
        pass

    def test_buyerTitle(self):
        self.i_label.setFunctionName(inspect.stack()[0][3])
        self.i_label.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        self.i_label.title_execute()
        pass

    def test_buyerSurface(self):
        self.i_label.setFunctionName(inspect.stack()[0][3])
        self.i_label.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        self.i_label.surface_execute()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
