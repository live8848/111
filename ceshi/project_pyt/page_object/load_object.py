# -*- coding: utf-8 -*-
# @Time    : 2021/11/20 18:37
# @Author  : Hello world!
# @E-mail  : loading....
# @File    : load_object.py

from ceshi.project_pyt.common.log_test import Testlog
from ceshi.project_pyt.common.elements_object import Element_obj
from ceshi.project_pyt.page_element.page_load import Load_elemt
from ceshi.project_pyt.page_element.page_new import New_object



log = Testlog().getlog()


class Login(Element_obj, Load_elemt):
    def __init__(self, dr):
        # self.dr = dr
        super().__init__(dr)

    def login(self, name, password):
        self.iuput_element(self.loadid, text=name)  # 输入用户名
        log.info('输入用户名{}'.format(name))
        self.iuput_element(self.passwd, text=password)    # 输入密码
        log.info('输入用户名{}'.format(passwd))
        self.click_element(self.load_button)   # 点击登录按钮
        log.info('点击登录按钮')
        self.wait_time(New_object.new_button)
        log.info('等待进入系统')