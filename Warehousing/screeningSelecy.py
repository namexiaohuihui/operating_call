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
@file:      screeningSelecy.py
@time:      2018/12/21 18:08
@desc:
"""
import time
from selenium.common.exceptions import UnexpectedTagNameException
from selenium.webdriver.support.select import Select
from tools.browser_establish import browser_confirm
from tools.operation.selenium_visible import action_visible
from Warehousing.action_interface import ActionVisible


class ScreeningSelecy(ActionVisible):

    def setSelectData(self, labelPath, attr='id'):
        try:
            selectEle = self.is_visible_single_driver(labelPath, attr)
            self.ele_select(selectEle)
            return self
        except UnexpectedTagNameException:
            print("The incoming element path is not a select.")

    def ele_select(self, selectEle):
        """
        通过元素来创建下拉对象
        :return:
        """
        self.select = Select(selectEle)
        # 装options的数据,不创建value的容器是因为很少使用value
        self.optionsList = []
        return self

    # --------------------------------参数类型转换----------------------
    def options_to_str(self):
        self.getAllOptions()
        str_option = ','.join(self.optionsList)
        return str_option

    # ----------------------------------获取参数------------------------

    def __getOptions__(self):
        """
        统计options值，只限内部使用。外部不可调用
        :return:
        """
        for option in self.select.options:
            self.optionsList.append(option.text.strip())

    def get_value(self):
        """
        统计value值，只限内部使用。外部不可调用
        :return:
        """
        self.valueList = []
        for option in self.select.options:
            self.valueList.append(option.get_attribute("value").strip())

    def getSelector(self):
        # 　返回select对象
        return self.select

    def getSelectedOptions(self) -> str:
        '''
        返回当前业已选择的option
        :return:
        '''
        selected = self.select.first_selected_option.text.strip()
        return selected

    def getAllOptions(self):
        """
        获取全部的option数据
        :return: 返回全部的option
        """
        if self.optionsList:
            pass
        else:
            self.__getOptions__()
            pass
        return self.optionsList

    def getAllValue(self):
        """
        获取全部的value数据
        :return:  返回全部value
        """
        try:
            if self.valueList:
                pass
        except Exception as e:
            self.get_value()
            pass
        finally:
            return self.valueList

    def getOptionsSize(self):
        """
        先进options页面判断options数据是否存在
        然后在执行返回
        :return:  返回当前options值的总数
        """
        self.getAllOptions()
        return len(self.optionsList)

    def getValueSize(self):
        """
        先进去values页面判断values数据是否存在
        然后在执行返回
        :return: 返回当前options所对应的value值总数
        """
        self.getAllValue()
        return len(self.valueList)

    # ----------------------------------设置选择的参数------------------------
    def setSelectorValue(self, value):
        """
        通过value值来设置selector中的option
        :param value:  需要设置新的option值所对应的value
        :return: 返回替换前的option
        """
        try:
            selected = self.getSelectedOptions()
            self.select.select_by_value(value)
            return selected
        finally:
            return 'There is no option %s in the select.' % value

    def setSelectorIndex(self, index):
        """
        通过index值来设置selector中的option
        :param index: 需要设置新的option值所对应的index
        :return:  返回替换前的option
        """
        try:
            selected = self.getSelectedOptions()
            self.select.select_by_index(index)
            return selected
        finally:
            return 'There is no option %s in the select.' % index

    def setSelectorText(self, text) -> str:
        """
        通过text值来设置selector中的option
        :param text: 需要设置新的option值所对应的text
        :return: 返回替换前的option
        """
        try:
            selected = self.getSelectedOptions()
            # 判断当前业已的option是否为需要新设置的数据信息
            if selected == text:
                pass
            else:
                self.select.select_by_visible_text(text)
                time.sleep(1)
        except Exception as a:
            print("This parameter is not found in the drop-down box %s --- %s" % (text, a))
        finally:
            return selected

    # ---------------------------------------遍历设置option值-----------------------------
    def traverseYield(self, textList):
        '''
        根据lit/dict创建迭代器
        :param textList:
        :return:
        '''
        for text in textList:
            yield text

    def traverseSetText(self, textList):
        '''
        通过lit/dict来设置select的option
        :param textList:
        :return:
        '''
        tr_yield = self.traverseYield(textList)
        for text in tr_yield:
            self.select.select_by_visible_text(text)

    # ----------------------------------取消已选择的参数------------------------
    def setDeselectAll(self):
        """
        取消select中全部业已选择的option
        :return: 返回取消前的option
        """
        selected = self.getSelectedOptions()
        self.select.deselect_all()
        return selected

    def setDeselectValue(self, value):
        """
        根据value来取消业已选择的option
        :param value: 取消option值所对应的value
        :return:返回取消前的option
        """
        selected = self.getSelectedOptions()
        self.select.deselect_by_value(value)
        return selected

    def setDeselectIndex(self, index):
        """
        根据index来取消业已选择的option
        :param index: 取消option值所对应的index
        :return:返回取消前的option
        """
        selected = self.getSelectedOptions()
        self.select.deselect_by_index(index)
        return selected

    def setDeselectText(self, text):
        """
        根据text来取消业已选择的option
        :param text: 取消option值所对应的text
        :return: 返回取消前的option
        """
        selected = self.getSelectedOptions()
        self.select.deselect_by_visible_text(text)
        return selected

    # -------------------------------根据新的label来设置内容------------------------------
    def lable_set_text(self, label, text):
        '''
        根据label来设置新的text
        :param label: select位置
        :param text:  需要设置的值
        :return:
        '''
        self.setSelectData(label)
        self.setSelectorText(text)
        time.sleep(0.5)
