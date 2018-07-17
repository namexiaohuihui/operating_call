# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: wholeActionsJudge.py
@time: 2018/5/25 15:10
"""
# from CenterBackground.InteractionActions import WholeInteraction
from CenterBackground.InteractionActions import InteractionCoexistence
from tools.operationSelector import OperationSelector


class WholeActionsJudge(InteractionCoexistence):
    # excle文档中case所在工作薄的名称
    MODEL_WORKBOOK_LABEL = '标签'
    MODEL_WORKBOOK_DATA = '数据'
    MODEL_WORKBOOK_EVENT = '交互'


    # 当前子目录在菜单下的所属位置
    TREEW_TAGS_LOCATION = "1"

    # 根据key值，读取modei文件下保存用例的存放位置
    MODEI_CASE_POSITION = "whole"

    # MYSQL_DF, LABLE_DF
    def __init__(self) -> '对象实例化时就直接解析yaml中的数据信息,方便之后直接使用':
        self.parseyaml_location()
        self.parseyaml_content()

    # def city_active_confirm(self):
    # loantion = self.select_path['citytab']['value']
    # self._visible_return_selectop(loantion)
    #
    # def screening_to_mysql(self,filters,list_all):
    #     filters_keys = filters.keys()  # 找出filters当中的key
    #     sql_list = []
    #     for row_keys,row_list in filters_keys,list_all:
    #         internal = row_list[row_keys][0]
    #         for int_key in internal.keys():
    #             if internal[int_key] == filters[row_keys][internal]:
    #                 if row_keys == self.names_key.yaml_timeselect():
    #                     if int_key == self.names_key.yaml_choose():
    #                         ti_days = "o.add_time BETWEEN %s AND %s" % (self.ti.today_to_stamp(7))
    #                         sql_list.append(ti_days)