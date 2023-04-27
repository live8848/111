# -*- coding: utf-8 -*-
# @Time    : 2021/11/27 17:54
# @Author  : Hello world!
# @E-mail  : loading....
# @File    : test_event_select.py
import unittest
from project_connect.common_tools.HTML_request import Way_request
from project_connect.common_tools.File_read import Excel_object



class Test_event(unittest.TestCase):
    """事件查询"""
    def setUp(self):
        self.datas = Excel_object().read_excel('添加嘉宾')
        self.b = Excel_object().read_excel('数据')

    def tearDown(self):
        pass

    def test_11_select_event_by_eid(self):
        '''使用eid查询发布会'''
        case = self.datas[10]
        print('开始执行用例：{}'.format(case['测试标题']))
        if case['请求参数'].find('${eid}') != -1:
            case['请求参数'] = case['请求参数'].replace('${eid}', str(self.b[0]['eid']))
        res = Way_request().way_choise(case['请求方法'], case['请求地址'], eval(case['请求参数']))
        if res is not False:
            try:
                comp = res.json()['status']
                self.assertEqual(comp, case['预期结果'])
            except:
                raise
        else:
            pass

    def test_12_select_event_by_name(self):
        '''使用name查询发布会'''
        case = self.datas[11]
        print('开始执行用例：{}'.format(case['测试标题']))
        if case['请求参数'].find('${name}') != -1:
            case['请求参数'] = case['请求参数'].replace('${name}', str(self.b[0]['name']))
        res = Way_request().way_choise(case['请求方法'], case['请求地址'], eval(case['请求参数']))
        if res is not False:
            try:
                comp = res.json()['status']
                self.assertEqual(comp, case['预期结果'])
            except:
                raise
        else:
            pass

    def test_13_select_event_param_wrong(self):
        '''使用错误的参数查询发布会'''
        case = self.datas[12]
        print('开始执行用例：{}'.format(case['测试标题']))
        if case['请求参数'].find('${eid}') != -1:
            case['请求参数'] = case['请求参数'].replace('${eid}', str(self.b[0]['eid']))
        res = Way_request().way_choise(case['请求方法'], case['请求地址'], eval(case['请求参数']))
        if res is not False:
            try:
                comp = res.json()['status']
                self.assertEqual(comp, case['预期结果'])
            except:
                raise
        else:
            pass

    def test_14_select_event_by_wrong_eid(self):
        '''使用未创建的eid查询发布会'''
        case = self.datas[13]
        print('开始执行用例：{}'.format(case['测试标题']))
        if case['请求参数'].find('${eid}') != -1:
            case['请求参数'] = case['请求参数'].replace('${eid}', str(self.b[0]['eid_new']))
        res = Way_request().way_choise(case['请求方法'], case['请求地址'], eval(case['请求参数']))
        if res is not False:
            try:
                comp = res.json()['status']
                self.assertEqual(comp, case['预期结果'])
            except:
                raise
        else:
            pass

    def test_15_select_event_by_wrong_name(self):
        '''使用未创建的name查询发布会'''
        case = self.datas[14]
        print('开始执行用例：{}'.format(case['测试标题']))
        if case['请求参数'].find('${name}') != -1:
            case['请求参数'] = case['请求参数'].replace('${name}', str(self.b[0]['name_new']))
        res = Way_request().way_choise(case['请求方法'], case['请求地址'], eval(case['请求参数']))
        if res is not False:
            try:
                comp = res.json()['status']
                self.assertEqual(comp, case['预期结果'])
            except:
                raise
        else:
            pass