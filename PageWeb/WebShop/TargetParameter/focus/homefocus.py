# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: homefocus.py
@time: 2017/12/19 17:22
"""
from PageWeb.WebShop.TargetParameter.FocusVerification import verification_focus

from practical.utils.PymysqlMain import pymysqls


class focus_home(verification_focus):
    print("")

if __name__ == '__main__':
    print("11")
    pm = pymysqls.__new__(pymysqls)
    # pm.connects_cureors('localhost', 3306, 'root', 'xiaodingdong', 'ph_exclusive', 'utf8')
    pm.connects_cureors('load', 3306, 'root', 'xiaodingdong', 'table', 'utf8')
    sql = ""

    result = pm.selects(sql)

    for res in result:
        print("******************************************")
        book = verification_focus(res);
        print('\n'.join(['%s:%s' % item for item in book.__dict__.items()]))