# -*- coding: utf-8 -*-
# @Time    : 2021/11/20 14:57
# @Author  : Hello world!
# @E-mail  : loading....
# @File    : page_load.py

from selenium.webdriver.common.by import By


class Load_elemt():
    loadid = (By.XPATH, '//input[@name="loginId"]') # 账号输入框
    passwd = (By.XPATH, '//input[@name="password"]') # 密码输入框
    load_button = (By.XPATH, '//input[@id="button_submit"]') # 登录按钮


class New_object():
    new_button = (By.XPATH, '/html/body/div[2]/div/div[1]/table/tbody/tr[3]/td/a')  # 新建事项按钮
    frame_1 = (By.XPATH, '//iframe[@id="iframe_main"]')             # 标题frame层
    title = (By.XPATH, '//input[@id="subject"]')                    # 标题输入框
    process = d(By.XPATH, '//input[@id="trackInput"]')              # 流程输入框
    frame_2 = (By.XPATH, '//iframe[@id="baidu_editor_0"]')          # 文本内容frame层
    text_input = (By.XPATH, '/html/body/p')                         # 文本输入框

