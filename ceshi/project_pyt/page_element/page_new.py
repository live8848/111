# -*- coding: utf-8 -*-
# @Time    : 2021/11/20 18:36
# @Author  : Hello world!
# @E-mail  : loading....
# @File    : page_new.py
from selenium.webdriver.common.by import By


class New_object():
    new_button = (By.XPATH, '/html/body/div[2]/div/div[1]/table/tbody/tr[3]/td/a')  # 新建事项按钮
    frame_1 = (By.XPATH, '//iframe[@id="iframe_main"]')             # 标题frame层
    title = (By.XPATH, '//input[@id="subject"]')                    # 标题输入框
    process = d(By.XPATH, '//input[@id="trackInput"]')              # 流程输入框
    frame_2 = (By.XPATH, '//iframe[@id="baidu_editor_0"]')          # 文本内容frame层
    text_input = (By.XPATH, '/html/body/p')                         # 文本输入框
    create_button = (By.XPATH, '')              # 确定创建事项按钮
    create_error_text = (By.XPATH, '')      # 标题未输入弹窗
