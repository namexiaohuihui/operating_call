# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: AccountPrivacy.py
@time: 2018/1/4 22:13
@项目名称:operating
"""
from practical.constant.browser_establish import browser_confirm
from selenium.webdriver.common.touch_actions import TouchActions
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui

from practical.config import readModel
import time


def start_program(driver): # 暂时不用
    """
           开启线程用于执行打开浏览器和读取表格的数据。
           当数据执行完毕之后，开始执行动作
    """
    browser = Thread(args=accountPrivacy_user_login(driver))

    browser.start()

    sleep_Rest()  # 确保线程thread1已经启动
    browser.join()  # 将一直堵塞，直到thread1运行结束。



"""
#------------------获取浏览器部分------------------------------------
"""
def accountPrivacy_browser():
    # 1.创建浏览器所在函数的对象
    bc = browser_confirm.__new__(browser_confirm)
    options = bc.mobile_phone_mode()

    conf = readModel.establish_con()
    url = conf.get("wap", "url")

    # 2.调用已经规划好的浏览器函数
    driver = bc.url_opens(url, options)
    return driver

"""
#------------------- 用户登录-------------------
"""

def accountPrivacy_Route(driver):
    # 点击信息页面
    accountPrivacy_visible_css_selectop(driver,".nav-user")
    sleep_Rest()
    # 点击页面中的登录按钮
    accountPrivacy_visible_css_selectop(driver,".user-head")


def accountPrivacy_user_login(driver):
    try:
        conf = readModel.establish_con()
        account = conf.get("username", "account")
        password = conf.get("username", "password")
        accountPrivacy_Route(driver)

        accountPrivacy_visible_css_selectop(driver,'.login-type>a:nth-child(1)')  # 切换登陆方式

        # 账号密码的输入
        driver.find_element_by_css_selector("#J_tel").send_keys(account)
        driver.find_element_by_css_selector("#J_pwd").send_keys(password)

        # 登陆按钮
        accountPrivacy_visible_css_selectop(driver,".u-btn.u-btn-morange")


    except Exception:
        import inspect
        function = inspect.stack()[0][3]  # 执行函数的函数名
        error_log(driver,function)
        raise

"""
#--------------------读取excel表格数据部分-----------------------------------------
"""

def accountPrivacy_excel_Data(file_path=None):

    """
    从excel表格中获取数据并进行转换
    :param file_path:
    :return:
    """
    # 获取excel路径
    if file_path == None: file_path = readModel.establish_con().get("excel", "exclusiveServiceFile")

    # 读取相应路径中的数据
    from practical.utils.OpenpyxlExcel import READEXCEL, PANDASDATA
    read = READEXCEL(file_path)

    # 获取case
    whole = read.position_sheet_row_value()
    # 获取内容
    row_col_data = whole[0]
    # 获取标题
    title_data = whole[1]

    # 数据转换
    pan = PANDASDATA(row_col_data)
    df = pan.definition_DataFrame(index="2017-12-24", periods=len(tuple(row_col_data)), columns=title_data)
    print("wanbisgsdg %s" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    return df, row_col_data

"""
#--------------------元素判断部分-----------------------------------------
"""

def accountPrivacy_visible_css_selectop(driver, locator, timeout=3):
    # 判断元素是否存在，如果存在就进行点击并返回对象
    try:

        import datetime
        # ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        element = ui.WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        sleep_Rest()
        touchActions_tap(driver,element)
        return element

    except TimeoutException:

        print("元素未出现：   %s" % locator)
        import inspect
        function = inspect.stack()[0][3]  # 执行函数的函数名
        error_log(driver, function)
        return False


def accountPrivacy_visible_css_selectop_text(driver, locator, timeout=3):
    # 判断元素是否存在，如果存在就进行获取元素的text属性
    try:

        import datetime
        _ele = ui.WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        return _ele.text


    except TimeoutException:

        print("元素未出现：   %s" % locator)
        import inspect
        function = inspect.stack()[0][3]  # 执行函数的函数名
        error_log(driver, function)

        return False

def accountPrivacy_visible_css_selectop_attribute(driver, locator, timeout=3):
    # 判断元素是否存在，如果存在就获取元素的value属性内容
    try:
        import datetime
        _ele = ui.WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        text = _ele.get_attribute("value")  # 创建元素对象
        return text
    except TimeoutException:
        print("元素未出现：   %s" % locator)
        import inspect
        function = inspect.stack()[0][3]  # 执行函数的函数名
        error_log(driver, function)
        return False

def accountPrivacy_sendKeys_css_selectop(driver, locator,content, timeout=3):
    # 判断元素是否存在，如果存在就进行输入
    try:

        import datetime
        # ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        element = ui.WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        sleep_Rest()
        accountPrivacy_sendKeys_content(element,content)
        return element

    except TimeoutException:

        print("元素未出现：   %s" % locator)
        import inspect
        function = inspect.stack()[0][3]  # 执行函数的函数名
        error_log(driver, function)
        return False

"""
#--------------------浏览器操作部分-----------------------------------------
"""

def touchActions_tap(driver, element):
    # 点击元素
    TouchActions(driver).tap(element).perform()
    sleep_Rest()

def accountPrivacy_sendKeys_content(element,content):
    element.clear()
    element.send_keys(content)


"""
#--------------------其他一些配置部分-----------------------------------------
"""

def sleep_Rest( ti=1):  # 延迟
    time.sleep(ti)

def error_log(browser,function):
    import os
    # 执行文件的文件名
    basename = os.path.splitext(os.path.basename(__file__))[0]

    # 拼接名字
    name_tion = basename + ":" + function

    # 调用错误类
    from practical.utils import DefinitionError
    DefinitionError.error_output(name_tion, browser)


