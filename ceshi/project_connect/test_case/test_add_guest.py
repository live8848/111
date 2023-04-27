# -*- coding: utf-8 -*-
# @Time    : 2021/11/23 14:25
# @Author  : Hello world!
# @E-mail  : loading....
# @File    : test_add_guest.py
import unittest
from project_connect.common_tools.HTML_request import Way_request
from project_connect.common_tools.File_read import Excel_object

class Test_people(unittest.TestCase):
    """添加嘉宾"""
    def setUp(self):
        self.datas = Excel_object().read_excel('添加嘉宾')
        self.b = Excel_object().read_excel('数据')

    def tearDown(self):
        pass

    def test_01_add_success(self):
        '''成功添加嘉宾'''
        case = self.datas[0]
        print('开始执行用例：{}'.format(case['测试标题']))
        if case['请求参数'].find('${phone}') != -1:
            case['请求参数'] = case['请求参数'].replace('${phone}', str(self.b[0]['phone_new']))
        res = Way_request().way_choise(case['请求方法'], case['请求地址'], eval(case['请求参数']))
        if res is not False:
            try:
                comp = res.json()['status']
                phone = eval(case['请求参数'])['phone']
                Excel_object().write_excel(phone, 1)
                self.assertEqual(comp, case['预期结果'])
            except:
                raise
        else:
            pass

    def test_02_add_repet_phone(self):
        '''使用已存在的手机号添加嘉宾'''
        case = self.datas[1]
        print('开始执行用例：{}'.format(case['测试标题']))
        if case['请求参数'].find('${phone}') != -1:
            case['请求参数'] = case['请求参数'].replace('${phone}', str(self.b[0]['phone']))
        res = Way_request().way_choise(case['请求方法'], case['请求地址'], eval(case['请求参数']))
        if res is not False:
            try:
                comp = res.json()['status']
                self.assertEqual(comp, case['预期结果'])
            except:
                raise
        else:
            pass

    def test_03_add_eid_not_exist(self):
        '''给未创建的eid添加用户'''
        case = self.datas[2]
        print('开始执行用例：{}'.format(case['测试标题']))
        if case['请求参数'].find('${phone}') != -1:
            case['请求参数'] = case['请求参数'].replace('${phone}', str(self.b[0]['phone_new']))
        res = Way_request().way_choise(case['请求方法'], case['请求地址'], eval(case['请求参数']))
        if res is not False:
            try:
                comp = res.json()['status']
                phone = eval(case['请求参数'])['phone']
                Excel_object().write_excel(phone, 1)
                self.assertEqual(comp, case['预期结果'])
            except:
                raise
        else:
            pass

    def test_04_add_param_wrong(self):
        '''添加用户使用错误的参数'''
        case = self.datas[3]
        print('开始执行用例：{}'.format(case['测试标题']))
        if case['请求参数'].find('${phone}') != -1:
            case['请求参数'] = case['请求参数'].replace('${phone}', str(self.b[0]['phone_new']))
        res = Way_request().way_choise(case['请求方法'], case['请求地址'], eval(case['请求参数']))
        if res is not False:
            try:
                comp = res.json()['status']
                phone = eval(case['请求参数'])['phone']
                Excel_object().write_excel(phone, 1)
                self.assertEqual(comp, case['预期结果'])
            except:
                raise
        else:
            pass

