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
@file: tabsJude.py
@time: 2018/8/14 17:41
@desc:
'''
from CenterBackground.judeVerification import JudgmentVerification



class TabsJude(JudgmentVerification):
    def __init__(self, config, basename, centerName):
        '''
        :param config: 头文件所在位置
        :param basename: 执行用例的文件名
        :param centerName: 参数定义的类对象
        '''
        JudgmentVerification.__init__(self, config, basename)
        self.bi = centerName()
        pass

    # --------------------------------------------------------
    # ---------------------用例直接调用进行使用-------------------
    # ---------------------tabs用例位置-------------------------
    # --------------------------------------------------------
    def get_tabs_active(self):
        # 根据界面元素，获取相应的text
        # locator = self.financial[self.bi.page_evaluation()][self.bi.page_tabs()]
        locator = self.financial[self.bi.yaml_tabs()]
        locator = '%s.active' % locator
        label_tabs = self.vac.is_visible_css_selectop(self.driver, locator)
        # 获取用例设置的数据信息
        excle_tabs = self.overall[self.bi.whole_default()]
        information = 'The tabs element defaults to jump.'

        self.verify_operator(label_tabs.text, excle_tabs, information)
        pass

    def get_tabs_text(self):
        # 获取界面元素，并将list存储的text转成str
        # locator = self.financial[self.bi.page_evaluation()][self.bi.page_tabs()]
        locator = self.financial[self.bi.yaml_tabs()]
        label_tabs = self.vac.is_visibles_css_selectop(self.driver, locator)
        label_tabs = [str.strip(tabs.text) for tabs in label_tabs]
        # 获取用例设置的数据信息
        excle_tabs = self.overall[self.bi.whole_including()]
        information = 'The caption tabs element text is judged incorrectly.'

        self.verify_operator(','.join(label_tabs), excle_tabs, information)
        pass

    def get_tabs_switch(self):
        # locator = self.financial[self.bi.page_evaluation()][self.bi.page_tabs()]
        locator = self.financial[self.bi.yaml_tabs()]
        label_tabs = self.vac.is_visibles_css_selectop(self.driver, locator)
        for tabs in range(len(label_tabs)):
            self.vac.element_click(label_tabs[tabs])
            label_tabs = self.vac.is_visibles_css_selectop(self.driver, locator)

    # --------------------------------------------------------
    # ---------------------用例直接调用进行使用-------------------
    # ---------------------box用例位置--------------------------
    # --------------------------------------------------------
    def get_box_active(self):
        # 根据界面元素，获取相应的text
        locator = self.financial[self.bi.yaml_box()]
        locator = '%s.on' % locator
        label_tabs = self.vac.is_visible_css_selectop(self.driver, locator)
        # 获取用例设置的数据信息
        excle_tabs = self.overall[self.bi.whole_default()]
        information = 'The box element defaults to jump.'

        self.verify_operator(label_tabs.text, excle_tabs, information)
        pass

    def get_box_text(self):
        # 获取界面元素，并将list存储的text转成str
        locator = self.financial[self.bi.yaml_box()]
        label_tabs = self.vac.is_visibles_css_selectop(self.driver, locator)
        label_tabs = [str.strip(tabs.text) for tabs in label_tabs]
        # 获取用例设置的数据信息
        excle_tabs = self.overall[self.bi.whole_including()]
        information = 'The caption box element text is judged incorrectly.'

        self.verify_operator(','.join(label_tabs), excle_tabs, information)
        pass

    def get_box_switch(self):
        locator = self.financial[self.bi.yaml_box()]
        label_tabs = self.vac.is_visibles_css_selectop(self.driver, locator)
        for tabs in range(len(label_tabs)):
            self.vac.element_click(label_tabs[tabs])
            label_tabs = self.vac.is_visibles_css_selectop(self.driver, locator)
