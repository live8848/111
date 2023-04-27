# -*- coding: utf-8 -*-
# @Time    : 2021/11/20 15:10
# @Author  : Hello world!
# @E-mail  : loading....
# @File    : test_load.py

from selenium import webdriver
import unittest
from ceshi.project_unit.text_datas import load_datas
from ceshi.project_unit.page_element import page_load

class Test_load(unittest.TestCase):
    driver = webdriver.Chrome()
    @classmethod
    def setUpClass(cls):
        driver.get(r'http://192.168.50.89:8080/oa/')
        driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        driver.quit()

    def test_01(self):
        '''验证登陆密码不能为空'''
        data = load_datas.sign_in()[0]
        ele_local = page_load.load_elemt()
        ele_local[0].send_keys('abc')
        ele_local[1].send_keys(data['abc123456'])
        ele_local[2].click()

if __name__=='__main__':
    unittest.main()