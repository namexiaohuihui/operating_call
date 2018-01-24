# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: name_bean.py
@time: 2017/11/2 23:36
@项目名称:operating
"""


# 该类主要设置一些常用的属性值以及参数

class letter_parameter_names(object):

    """
    整体路径
    """
    sidebar = ".sidebar-menu li:nth-child(2)" # 顶级目录
    treew = ".treeview-menu.menu-open li:nth-child(1)" #上级目录
    tabs_withdrawals = ".nav.nav-tabs li:nth-child(4)" # 提现入口

    """--------------------------------参数的获取路径------------------------------"""

    # 提取页面的----------------------
    # 提取值的设置
    amount_load = "amount"
    # 　手续的设置
    fee_load = "fee"
    # 提交按钮
    extractSave = '.btn.btn-primary.feeSave'

    # 优惠页面的-------------
    # 对象折扣
    goods_discount = 'goods_discount'

    # 对象限购
    goods_id = 'goods_id'

    # 绑定折扣
    watiki_discount = 'watiki_discount'

    # 绑定限购
    watikis_id = 'watikis_id'

    # 绑定峰值
    watikis_max = 'watikis_max'

    # 页面提交按钮
    settingSave = '.btn.btn-primary.settingSave'

    # 邀请页面-----------------------------------
    hourTime = ".form-control.hour"
    timeTime = ".form-control.time"
    real_payTime = ".form-control.real_pay"
    moneyTime = ".form-control.money"
    saveTime = ".btn.btn-primary.save"

    # 弹窗的设置-------------------
    # 提示框的标题
    visible_h2 = '.sweet-alert.showSweetAlert.visible h2:nth-of-type(1)'

    # 提示框的内容
    visible_p = '.sweet-alert.showSweetAlert.visible p:nth-of-type(1)'

    # 提示框中的确认
    confirm = '.confirm'

    # 二次确认中的重点文字
    modal_body_h4 = '.modal-body>h4'

    # 二次确认中的侧面文字
    modal_body_p = '.modal-body>p'

    # 二次确认中的取消按钮:分类class名为modal-footer，去找到子类中button的元素并且位置为第一个
    btn_default = '.modal-footer button:nth-child(1)'

    # 二次确认中的确认按钮,通过id进行执行
    discountsave = '#discountsave'

    """--------------------------------提示参数------------------------------"""

    # 提取页面----------------
    ex_less = '提现手续费应小于提现金额'
    ex_format = '请输入整数最多7位,小数后两位的价格格式'

    # 优惠设置---------------
    # 商品折扣数的提示
    gb_between = "请输入0.1~9.9之间的数"  # 折扣数输入的数字符合格式范围内
    gb_format = "请输入正确格式例如 0.1/0.5"  # 折扣数输入的格式完全不符合

    # 不参与折扣商品的提示
    gp_non_existent = "没有该商品ID:"  # 没有找到输入的数字
    gp_separate = "请输入正整数多个用逗号分隔"  # 输入的不为数字
    gp_proper = "该商品为店铺商品"  # 输入的数字不是共有的
    gp_incorrect = "输入的不参与优惠商品不正确"  # 输入完全不正确的提示

    #  上限数量的提示:
    number_max = "请输入金额格式"


    # 邀请页面设置---------------

    # 系统固定提示框的提示
    system_preservation = "你确定要保存吗？"  # 再次确认的标题
    system_content = "保存后新产生的订单立即生效已产生的订单不受影响"  # 再次确认的提示内容
    system_successful = "操作成功"  # 再次确认的提示内容