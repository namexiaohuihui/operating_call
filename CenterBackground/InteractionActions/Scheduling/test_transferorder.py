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
@file:      test_transferorder.py
@time:      2018/10/17 16:36
@desc:
"""
import os
import inspect
import unittest
from CenterBackground.InteractionActions.operationViewJude import OperationViewJude
from CenterBackground import InteractionActions
from tools.excelname.Center.Interaction import InteractionController

basepath = os.path.split(os.path.dirname(__file__))[1]
basename = os.path.splitext(os.path.basename(__file__))[0]
basename = basepath + "-" + basename
# 传入子集的key，以及Excel文档中的sheet名字
config = InteractionActions.add_key(InteractionActions.dispatch, InteractionActions.transfer)

trans_o = OperationViewJude(config, basename, InteractionController)


class TestTransferOrder(unittest.TestCase):
    """
    转预约功能的订单
    """
    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        trans_o.openingProgram()
        trans_o._rou_background()
        trans_o.log.info("%s : The use case begins execution" % basename)
        pass

    def tearDown(self):
        trans_o.driver.quit()
        trans_o.log.info("%s : The use case is done" % basename)
        pass

    def test_dayTransfer(self):
        """
        查看下单时间为当天的订单
        :return:
        """
        trans_o.setFunctionName(inspect.stack()[0][3])
        trans_o.release_success()
        # 找到td通过子元素的text来找到信息
        trans_o.transfer_order_types()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)