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
@file:      test_operatemutually.py
@time:      2018/11/9 11:20
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import GeneralizeAssist
from tools.excelname.Center.generalize import Generalize
from CenterBackground.GeneralizeAssist.Invite.inviteoperatejude import InviteOperateJude

basepath = os.path.split(os.path.dirname(__file__))[1]
basename = os.path.splitext(os.path.basename(__file__))[0]
basename = basepath + "-" + basename

# 传入子集的key，以及Excel文档中的sheet名字
config = GeneralizeAssist.add_key(GeneralizeAssist.mutually, GeneralizeAssist.operate)
m_operate = InviteOperateJude(config, basename, Generalize)


class TestOperateMutually(unittest.TestCase):
    """
    invite页面中tbody内容的跳转
    """

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        m_operate.openingProgram()
        m_operate._rou_background()
        m_operate.log.info("%s ---setup: 每个用例开始前后执行" % basename)
        pass

    def tearDown(self):
        m_operate.driver.quit()
        m_operate.log.info("%s ---teardown: 每个用例结束后执行" % basename)
        pass

    def test_goodnameAccess(self):
        m_operate.setFunctionName(inspect.stack()[0][3])
        m_operate.conditions_screening()
        pass

    def test_effectAccess(self):
        m_operate.setFunctionName(inspect.stack()[0][3])
        m_operate.conditions_screening()
        pass




if __name__ == '__main__':
    unittest.main(verbosity=2)
