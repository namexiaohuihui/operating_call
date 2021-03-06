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
@file: commoditiesJude.py
@time: 2018/8/20 16:27
@desc:
'''
from CenterBackground import Commodities
from CenterBackground.customTabs import CustomTabs
from CenterBackground.judeVerification import JudgmentVerification


class CommoditiesJude(JudgmentVerification):
    '''
    二次封装tabs进行判断
    '''

    def __init__(self, config, basename, centerName):
        '''
        :param config: 头文件所在位置,即__init__.py文件中定义的INVENTORY
        :param basename: 当前执行用例的文件名,在用例文件中自动获取
        :param centerName: 元素路径对应的关键字的函数
        '''
        JudgmentVerification.__init__(self, config, basename)
        self.bi = centerName()
        pass

    def custom_tabs(self):
        """
        统一实例化city操作对象
        :return:
        """
        # 读取元素的类型
        keys = self.overall[self.bi.whole_keys()]
        # 根据类型读取相应的数据信息
        self.ct = CustomTabs(self.driver, self.financial[keys])
        return self.ct

    def active_city(self, tag):
        """
        比较默认显示的城市
        :param tag: 元素标签默认值的读取元素
        :return:
        """
        try:
            ov_default = self.overall[self.bi.whole_city()]
            self.custom_tabs().judge_city(tag, ov_default)
            del ov_default
        except KeyError as a:
            raise KeyError("用例上的类型参数没有设置内容 %s" % ov_default)
        pass

    def active_code(self, tag):
        """
        比较默认显示的区域
        :param tag: 元素标签默认值的读取元素
        :return:
        """
        ov_default = self.overall[self.bi.whole_code()]
        self.custom_tabs().judge_code(tag, ov_default)
        pass

    def div_a_city_code(self, tag):
        """
        城市标签位置处于div>a下面时的读取方式
        :return:
        """
        ov_default = self.overall[self.bi.whole_code()]
        self.custom_tabs().judge_diva_code(tag, ov_default)
        pass

    def already_citys(self, reduce=0):
        """
        读取全部city的数据信息
        :param reduce:
        :return:
        """
        self.custom_tabs().judge_citys(reduce=reduce)
        pass

    def already_codes(self, reduce=0):
        self.custom_tabs().judge_codes(reduce=reduce)
        pass

    def div_a_city_codes(self, reduce=0):
        """
        城市标签位置处于div>a下面时的读取方式
        :return:
        """
        self.custom_tabs().judge_diva_codes(reduce=reduce)
        pass

    def switch_city(self, reduce=0):
        """
        循环点击city/box出现的项
        :param reduce:
        :return:
        """
        self.custom_tabs().judge_source(reduce=reduce)
        pass

    def switch_url(self, tag, reduce=0):
        """
        解析city/box绑定连接,利用url原理循环进入
        :param tag:
        :param reduce:
        :return:
        """
        self.custom_tabs().judge_source_url(tag, reduce=reduce)
        pass
