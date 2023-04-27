# -*- coding: utf-8 -*-
# @Time    : 2021/11/20 19:04
# @Author  : Hello world!
# @E-mail  : loading....
# @File    : test_01_log.py

from ceshi.project_pyt.common.log_test import Testlog
from ceshi.project_pyt.page_object.load_object import Login
from ceshi.project_pyt.text_datas.test_datas import *
from ceshi.project_pyt.page_object.create_new_file import Create_file
from project_pyt.common.elements_object import Element_obj
import unittest
from selenium import webdriver

log = Testlog().getlog()

class Test_load(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global dr
        dr = webdriver.Chrome()
        dr.get(r'http://192.168.50.89:8080/oa/')

    @classmethod
    def tearDownClass(cls):
        dr.quit()

    def test_01(self):
        '''验证登陆密码不能为空'''
        log.info('执行用例:{}'.format(self.error_load[0]['test_name']))
        self.login(self.error_load[0]['name'], self.error_load[0]['code'])
        wd_l = self.get_element_text(self.load_error_text)
        try:
            self.assertEqual(wd_l, self.error_load[0]['check'])
            log.info('用例{}执行成功！'.format(self.error_load[0]['test_name']))
        except:
            log.exception('用例{}执行失败'.format(self.error_load[0]['test_name']))
            self.save_pucture()
            raise

    def test_02(self):
        '''验证创建事项标不能为空'''
        log.info('执行用例:{}'.format(self.error_title[0]['test_name']))
        self.create(self.error_text[0]['code'])
        wd_c = self.get_element_text(self.create_error_text)
        try:
            self.assertEqual(wd_c, self.error_title[0]['check'])
            log.info('用例{}执行成功'.format(self.error_title[0]['test_name']))
        except:
            log.exception('用例{}执行失败'.format(self.error_title[0]['test_name']))
            self.save_pucture()
            raise


