# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: dailyLabelNames.py
@time: 2018/4/15 17:54
"""
from utils.excelname.shopSystemsetup import ShopNoticeController
class DailyLabelNames(ShopNoticeController):

    def getDailyBulletin(self):
        """
            定义文件名以及工作薄，方便统一进行修改
        """
        disList = ["dailybulletin", 1];
        return disList

    """
        整体路径
    """
    sidebar = ".sidebar-menu>li:nth-child(9)"  # 菜单目录


    treew = ".treeview-menu.menu-open li:nth-child(2)"  # 标签目录

    tabs_maintenance = ".nav.nav-tabs li:nth-child(1)"  # 维护页面
    tabs_dail = ".nav.nav-tabs li:nth-child(2)"  # 日常页面
    tabs_help = ".nav.nav-tabs>li:nth-child(3)"  # 帮助页面


    # -----------------------参数获取路径---------------------

    # 界面上：添加按钮
    operation = ".btn.btn-default.btn-sm modal-btn"
    turn_page = ".pagination"
    # 界面上：公告标题
    lable_thead = "#datatatle > thead"
    # 界面上：公告内容
    lable_tbody = "#datatatle > tbody"
    # 界面上：公告第一个操作按钮
    button_one = "%s > tr:nth-child(1) > td:nth-child(7) >button:nth-child(1)" % lable_tbody
    # 界面上：公告第二个操作按钮
    button_two = "%s > tr:nth-child(1) > td:nth-child(7) >button:nth-child(2)" % lable_tbody

    # 弹窗的位置
    operation_location = ".modal-content"
    # 弹窗的类型:
    operation_noticesort = "#noticesort1" #日常
    operation_noticesort2 = "#noticesort2" # 维护
    # 弹窗上：标题
    operation_title = ".modal-header>h4:nth-of-type(1)"
    # 弹窗上：公告类型
    operation_choose = ".form-group>div>span"
    # 弹窗上：提示文字
    operation_text = ".#noticeForm > div:nth-child(3) > div > p"
    # 弹窗上：下拉
    operation_select = "#noticeForm > div:nth-child(4) > div > select"
    operation_select_text = "#noticeForm > div:nth-child(4) > label"
    # 弹窗上：标题输入
    operation_dail_text = "#noticeForm > div:nth-child(5) > label"
    operation_dail_input = ".form-control.noticename"
    # 弹窗上：内容输入
    operation_content_text = "#noticeForm > div:nth-child(6) > label"
    operation_content_input = ".form-control.noticeinfo"
    # 弹窗上：日期输入
    operation_deadline_text = "#noticeForm > div:nth-child(7) > label"
    operation_deadline_input = ".form-control.pull-right"
    operation_deadline_id = "reservationtime"  # 这个时间放的是id路径不是cssSelector
    # 弹窗上：取消/确定按钮
    operation_default = ".btn.btn-default"
    operation_primary = ".btn.btn-primary"

    # 日常上：城市
    dail_city = ".box-city > div:nth-child(1) > select"
    # 日常上：状态
    dail_status = ".box-city > div:nth-child(2) > select"
    # 日常上：按钮
    dail_button = ".btn.btn-default.btn-flat.btn-action.J_ipt"
    # 日常上：弹窗标题
    dail_title ='.sweet-alert.showSweetAlert.visible h2:nth-of-type(1)'
    # 日常上：弹窗内容
    dail_content ='.sweet-alert.showSweetAlert.visible p:nth-of-type(1)'
    # 日常上：弹窗确定按钮
    dail_determine = '.sa-confirm-button-container'
    # 日常上：弹窗取消按钮
    dail_cancel = ".cancel"


    # 帮助上：页面入口
    hele_iframe = ".ke-edit-iframe"
    # 帮助上：输入框
    hele_body = ".ke-content"

    # -----------------------提示标语信息---------------------
    bulletin_primary = "确定"
    stop_title = "你确认要停止?"
    stop_content = "确定要停止该平台公告吗?"
    stop_determine = "是的, 停止!"
    stop_cancel = "取消"






