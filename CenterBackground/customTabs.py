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
@file: customTabs.py
@time: 2018/8/21 10:15
@desc:
'''
import operator
from tools.operation.selenium_click import action_click
from tools import StringCutting

_att = 'a'
_href = 'href'
_class = 'class'
_active = 'active'
_on = 'on'


class CustomTypeError(Exception):
    pass


class CustomTabs(object):
    '''
    Use the tabs path to get the value of the element and the corresponding active.
    Parse the label attributes in the element to get the qualified code.
    '''

    def __init__(self, driver, parth):
        """
        初始化对象
        :param driver:
        :param parth:  元素路径
        """
        self.driver = driver
        self.parth = parth
        self.ac = action_click()
        pass

    def is_visibles(self):
        """
        判断城市tab是否出现
        :return:
        """
        self.ul_li = self.ac.is_visibles_css_selectop(self.driver, self.parth)
        if type(self.ul_li) is bool:
            raise CustomTypeError("You can't find the tabs element.")

    def visibles_tabs(self, reduce=0):
        '''
        将后面不需要的button给排除
        :param reduce:
        :return:
        '''
        self.is_visibles()
        reduce = int(reduce)
        for l in range(reduce):
            length = len(self.ul_li) - 1
            self.ul_li.pop(length)

    def active_tab(self, _class, reduce=0):
        '''
        比较li标签的class值.
        找到li中默认展示的值
        :return:
        '''
        self.visibles_tabs(reduce)
        for li in self.ul_li:
            ac_at = li.get_attribute(_class)
            if operator.eq(_active, ac_at) or operator.eq(_on, ac_at):
                return li
        raise CustomTypeError("active_tab: no li! No li found! You didn't write LI")

    def city_code(self, li):
        """
        切割城市的code值
        :param li:
        :return:
        """
        li_a = li.find_element_by_tag_name(_att)
        li_a = li_a.get_attribute(_href)
        li_a = StringCutting.re_zip_code(li_a)
        return li_a

    def diva_city_code(self, li):
        """
        专门对div>a进行处理操作
        :param li:
        :return:
        """
        li_a = li.get_attribute(_href)
        li_a = StringCutting.specified_cut_ber(li_a, "=", -1)
        return li_a

    def custom_keys(self, reduce=0):
        '''
        全部城市和编码
        :return:  城市为key，编码为value
        '''
        self.visibles_tabs(reduce)
        custom_d = {}
        for li in self.ul_li:
            li_a = li.find_element_by_tag_name(_att)
            li_a = li_a.get_attribute(_href)
            custom_d[li_a.text.strip()] = StringCutting.re_zip_code(li_a)
        return custom_d

    def active_keys(self, tag):
        '''
        默认城市和编码
        :return: 城市为key，编码为value
        '''
        li = self.active_tab(tag)
        li_a = li.find_element_by_tag_name(_att)
        li_a = li_a.get_attribute(_href)
        active_d = {li_a.text.strip(): StringCutting.re_zip_code(li_a)}
        return active_d

    def instance_citys(self, reduce=0):
        '''
        :param parth:
        :return:  全部城市
        '''
        self.visibles_tabs(reduce)
        list_text = [li.text.strip() for li in self.ul_li]
        return list_text

    def active_city(self, tag):
        '''
        默认城市
        :return:
        '''
        li = self.active_tab(tag)
        li_text = li.text.strip()
        return li_text

    def instance_codes(self, reduce=0):
        '''
        :return: 全部元素的编码
        '''
        self.visibles_tabs(reduce)
        list_code = [self.city_code(li) for li in self.ul_li]
        return list_code

    def active_code(self, tag):
        '''
        默认城市编码
        :return:
        '''
        li = self.active_tab(tag)
        li_code = self.city_code(li)
        return li_code

    def judge_source(self, reduce=0):
        '''
        遍历点击
        :param reduce:
        :return:
        '''
        self.visibles_tabs(reduce)
        length = len(self.ul_li)
        for l in range(length):
            self.ac.element_click(self.ul_li[l])
            self.visibles_tabs(reduce)
        pass

    def judge_source_url(self, tag, reduce):
        '''
        遍历点击标签元素
        :param tag: 元素标签默认值属性
        :param reduce:  需要扣除的个数
        :return:
        '''
        list_text = self.judge_citys(reduce)  # 读取全部的城市
        length = len(self.ul_li)  # 读取数据长度
        self.visibles_tabs(reduce)  # 剔除不符合的数据
        for l in range(length):
            # 读取默认值对象的href属性
            li_a = self.ul_li[l]
            # 如果元素标签为a，那么就直接获取参数值，否则元素标签就是为li那么就要获取旗下的a标签然后在获取参数值
            if li_a.tag_name == _att:
                pass
            else:
                li_a = li_a.find_element_by_tag_name(_att)
                # li_a = self.ul_li[l].find_element_by_tag_name(_att)
            li_a = li_a.get_attribute(_href)
            # 输入网址
            self.driver.get(li_a)
            # 数据比较
            self.judge_city(tag, list_text[l])
            self.visibles_tabs(reduce)
        pass

    def judge_citys(self, reduce=0, ov_default=True):
        list_text = self.instance_citys(reduce)
        self.debugging_log(True, ov_default, 'All labels in the title are misjudged.')
        return list_text

    def judge_city(self, tag, ov_default):
        ct_default = self.active_city(tag)
        self.debugging_log(ct_default, ov_default, 'The caption tabs element text is judged incorrectly.')
        pass

    def judge_codes(self, reduce=0, ov_default=True):
        list_code = self.instance_codes(reduce)
        self.debugging_log(True, ov_default, 'All labels in the title are misjudged.')
        return list_code

    def judge_diva_codes(self, reduce=0, ov_default=True):
        self.visibles_tabs(reduce)
        list_code = [self.diva_city_code(li) for li in self.ul_li]
        self.debugging_log(True, ov_default, 'All labels in the title are misjudged.')
        return list_code

    def judge_code(self, tag, ov_default):
        ct_default = self.active_code(tag)
        ov_default = self.data_to_determine(ov_default)
        self.debugging_log(ct_default, ov_default, 'The header label attribute is incorrect.')
        pass

    def judge_diva_code(self, tag, ov_default):
        """
        单独did>A的写法
        找到默认显示的对象,读取该对象中的url。
        切分数据信息
        :param tag:
        :param ov_default:
        :return:
        """
        # 默认对象
        li = self.active_tab(tag)
        # 读取对象的指定值
        ct_default = self.diva_city_code(li)
        # 专门处理
        ov_default = StringCutting.specified_cut_ber(ov_default, ".")

        self.debugging_log(ct_default, ov_default, 'The header label attribute is incorrect.')

        pass

    def box_code(self, li_a):
        li_a = li_a.get_attribute(_href)
        li_a = StringCutting.re_zip_code(li_a)
        return li_a

    def judge_box_code(self, tag, ov_default):
        ct_default = self.active_tab(tag)
        ct_default = self.box_code(ct_default)
        ov_default = self.data_to_determine(ov_default)
        self.debugging_log(ct_default, ov_default, 'The header label attribute is incorrect.')
        pass

    def judge_box_codes(self, reduce, ov_default=True):
        self.visibles_tabs(reduce)
        list_code = [self.box_code(li) for li in self.ul_li]
        self.debugging_log(True, ov_default, 'The header label attribute is incorrect.')
        return list_code

    def debugging_log(self, ct_default, ov_default, mesg):
        print("--------------------------------")
        # print('moren', ct_default, type(ct_default))
        # print('duqu', ov_default, type(ov_default))
        print("--------------------------------")
        # 暂时先这样,因为把统计数也加到里面去了
        assert operator.eq(ct_default, ov_default), mesg
        pass

    def data_to_determine(self, strData):
        '''
        之所以需要对数据转换成int在转str：
        从excle读取的int是float，需要转成整数然后再转成str进行判断
        :param strData:
        :return:
        '''
        # print('Data read from the excel table : %s' % strData)
        return str(int(strData)) if strData else None

    def into_the_city(self, vac, case_city):
        """
        指定城市进行点击
        :param vac:  点击操作对象
        :param case_city:  需要点击的城市名
        :return:
        """
        self.is_visibles()
        # 2.1读取全部的城市text
        ul_text = [ul.text for ul in self.ul_li]

        # 2.2将元素和城市text通过dict形式存储
        city_text = dict(zip(self.ul_li, ul_text))

        # 2.3找到城市
        for city_k, city_v in city_text.items():
            if case_city == city_v:
                vac.element_click(city_k)
                break
        pass

    def into_the_city2(self, vac, case_city):
        """
        指定城市进行点击
        :param vac:  点击操作对象
        :param case_city:  需要点击的城市名
        :return:
        """
        self.is_visibles()

        # 2.1读取全部的城市text
        ul_text = [ul.text for ul in self.ul_li]

        # 2.2将元素和城市text通过dict形式存储
        city_text = dict(zip(ul_text, self.ul_li))

        # 2.3找到城市
        if case_city in city_text:
            vac.element_click(city_text[case_city])
        else:
            print("进入的城市不存在: %s %s" % ("into_the_city2", case_city))
