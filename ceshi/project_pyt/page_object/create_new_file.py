# -*- coding: utf-8 -*-
# @Time    : 2021/11/21 12:23
# @Author  : Hello world!
# @E-mail  : loading....
# @File    : create_new_file.py
from ceshi.project_pyt.common.log_test import Testlog
from ceshi.project_pyt.common.elements_object import Element_obj
from ceshi.project_pyt.page_element.page_new import New_object



log = Testlog().getlog()


class Create_file(Element_obj, New_object):
    def __init__(self, dr):
        super().__init__(dr)

    def create(self, name):
        self.click_element(self.new_button)
        log.info('点击新建事项按钮')
        self.switch_into(self.frame_1, type='frame')
        log.info('进入标题所在frame')
        self.input_element(self.title, text=name)
        log.info('输入标题内容')
        self.click_element(self.create_button)
        log.info('点击确定创建事项按钮')
