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
@file:      test_emptyDetail.py
@time:      2019/2/20 11:56
@desc:
"""
import os
import inspect
import unittest
import ddt
from CenterBackground import GoodsManagement
from tools.excelname.Center.googsMana import CityGoodsPage
from CenterBackground.surfacejude import SurfaceJude
from CenterBackground.judeVerification import JudgmentVerification
from Warehousing.TestStore import StoreDefault
from CenterBackground.GoodsManagement.EnterSales.handle_action_ddt import HandleActionDdt


def read_excle_data():
    GoodsManagement.add_key(GoodsManagement.emptybarrel, GoodsManagement.emdetail)
    excle_data = GoodsManagement._excel_Data('序号')
    return excle_data


@ddt.ddt
class TestEmptyDetail(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        #
        cls.empty_detail = HandleActionDdt(cls.basename, GoodsManagement.INVENTORY['yaml'])

        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]

        # 执行打开页面以及登录用户操作
        cls.empty_detail.screen_set_up('admin_url', 'admin_account', 'admin_password')

        # 进入空桶变更步骤
        cls.empty_detail.a_click.css_click(cls.empty_detail.driver,
                                           cls.empty_detail.financial['barrel_logs'])

        # 设置日志名称
        cls.empty_detail.log.fun_name = "test_modify_operation"
        pass

    @classmethod
    def tearDownClass(cls):
        cls.empty_detail.screen_tear_down(cls)
        pass

    @ddt.data(*read_excle_data())
    def test_modify_operation(self, case):
        """用例场景=:="""
        self.empty_detail.log.info("注释开头%s注释结尾" % case['场景'])

        if 'y' in case['执行'] or 'Y' in case['执行']:

            method_way = case.loc['执行方法']
            locator = case.loc['元素']
            way = case.loc['信息']

            method_way = self.function_getattr(method_way)
            method_way(locator, way)

            pass
        else:
            self.empty_detail.log.info("该场景不执行:%s" % case["场景"])

        pass

    def function_getattr(self, fun_attr):
        fun_attr = getattr(self.empty_detail, fun_attr, False)
        return fun_attr
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
