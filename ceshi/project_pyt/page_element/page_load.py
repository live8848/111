# -*- coding: utf-8 -*-
# @Time    : 2021/11/20 18:35
# @Author  : Hello world!
# @E-mail  : loading....
# @File    : page_load.py
from selenium.webdriver.common.by import By


class Load_elemt():
    loadid = (By.XPATH, '//input[@name="loginId"]') # 账号输入框
    passwd = (By.XPATH, '//input[@name="password"]') # 密码输入框
    load_button = (By.XPATH, '//input[@id="button_submit"]') # 登录按钮
    load_error_text = (By.XPATH, '')      # 密码未输入弹窗