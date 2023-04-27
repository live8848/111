# -*- coding: utf-8 -*-
# @Time    : 2021/11/23 16:46
# @Author  : Hello world!
# @E-mail  : loading....
# @File    : test_add_event.py
import unittest
from project_connect.common_tools.HTML_request import Way_request
from project_connect.common_tools.File_read import Excel_object
from project_connect.common_tools.log_test import Testlog

logging = Testlog().getlog()


class Test_event(unittest.TestCase):
    """创建事件"""
    def setUp(self):
        self.datas = Excel_object().read_excel('添加嘉宾')
        self.b = Excel_object().read_excel('数据')

    def tearDown(self):
        pass

    def test_05_add_event_success(self):
        '''成功创建新的发布会'''
        case = self.datas[4]
        print('开始执行用例：{}'.format(case['测试标题']))
        logging.info('开始执行用例：{}'.format(case['测试标题']))
        if case['请求参数'].find('${eid}') != -1:
            case['请求参数'] = case['请求参数'].replace('${eid}', str(self.b[0]['eid_new']))
            logging.info('eid参数已找到')
        else:
            logging.exception('eid参数未找到')
        if case['请求参数'].find('${name}') != -1:
            case['请求参数'] = case['请求参数'].replace('${name}', str(self.b[0]['name_new']))
            logging.info('name参数已找到')
        else:
            logging.exception('name参数未找到')
        res = Way_request().way_choise(case['请求方法'], case['请求地址'], eval(case['请求参数']))
        if res is not False:
            try:
                comp = res.json()['status']
                eid = eval(case['请求参数'])['eid']
                name = eval(case['请求参数'])['name']
                Excel_object().write_excel(eid, 3)
                Excel_object().write_excel(name, 5)
                self.assertEqual(comp, case['预期结果'])
            except:
                logging.exception('断言报错')
                raise
        else:
            logging.exception('请求方式有误')
            pass

    def test_06_add_event_param_wrong(self):
        '''使用错误的参数添加发布会'''
        case = self.datas[5]
        print('开始执行用例：{}'.format(case['测试标题']))
        if case['请求参数'].find('${eid}') != -1:
            case['请求参数'] = case['请求参数'].replace('${eid}', str(self.b[0]['eid_new']))
        if case['请求参数'].find('${name}') != -1:
            case['请求参数'] = case['请求参数'].replace('${name}', str(self.b[0]['name_new']))
        res = Way_request().way_choise(case['请求方法'], case['请求地址'], eval(case['请求参数']))
        if res is not False:
            try:
                comp = res.json()['status']
                eid = eval(case['请求参数'])['eid']
                name = eval(case['请求参数'])['name']
                Excel_object().write_excel(eid, 3)
                Excel_object().write_excel(name, 5)
                self.assertEqual(comp, case['预期结果'])
            except:
                raise
        else:
            pass

    def test_07_add_event_eid_exist(self):
        '''使用已经存在的eid新建发布会'''
        case = self.datas[6]
        print('开始执行用例：{}'.format(case['测试标题']))
        if case['请求参数'].find('${eid}') != -1:
            case['请求参数'] = case['请求参数'].replace('${eid}', str(self.b[0]['eid']))
        if case['请求参数'].find('${name}') != -1:
            case['请求参数'] = case['请求参数'].replace('${name}', str(self.b[0]['name_new']))
        res = Way_request().way_choise(case['请求方法'], case['请求地址'], eval(case['请求参数']))
        if res is not False:
            try:
                comp = res.json()['status']
                name = eval(case['请求参数'])['name']
                Excel_object().write_excel(name, 5)
                self.assertEqual(comp, case['预期结果'])
            except:
                raise
        else:
            pass

    def test_08_add_event_name_exist(self):
        '''使用已经存在的name新建发布会'''
        case = self.datas[7]
        print('开始执行用例：{}'.format(case['测试标题']))
        if case['请求参数'].find('${eid}') != -1:
            case['请求参数'] = case['请求参数'].replace('${eid}', str(self.b[0]['eid_new']))
        if case['请求参数'].find('${name}') != -1:
            case['请求参数'] = case['请求参数'].replace('${name}', str(self.b[0]['name']))
        res = Way_request().way_choise(case['请求方法'], case['请求地址'], eval(case['请求参数']))
        if res is not False:
            try:
                comp = res.json()['status']
                eid = eval(case['请求参数'])['eid']
                Excel_object().write_excel(eid, 3)
                self.assertEqual(comp, case['预期结果'])
            except:
                raise
        else:
            pass

    def test_09_add_event_time_wrong(self):
        '''使用错误的时间格式创建发布会'''
        case = self.datas[8]
        print('开始执行用例：{}'.format(case['测试标题']))
        if case['请求参数'].find('${eid}') != -1:
            case['请求参数'] = case['请求参数'].replace('${eid}', str(self.b[0]['eid_new']))
        if case['请求参数'].find('${name}') != -1:
            case['请求参数'] = case['请求参数'].replace('${name}', str(self.b[0]['name_new']))
        res = Way_request().way_choise(case['请求方法'], case['请求地址'], eval(case['请求参数']))
        if res is not False:
            try:
                comp = res.json()['status']
                eid = eval(case['请求参数'])['eid']
                name = eval(case['请求参数'])['name']
                Excel_object().write_excel(eid, 3)
                Excel_object().write_excel(name, 5)
                self.assertEqual(comp, case['预期结果'])
            except:
                raise
        else:
            pass

    def test_10_add_event_time_gone(self):
        '''使用过去的时间创建发布会'''
        case = self.datas[9]
        print('开始执行用例：{}'.format(case['测试标题']))
        if case['请求参数'].find('${eid}') != -1:
            case['请求参数'] = case['请求参数'].replace('${eid}', str(self.b[0]['eid_new']))
        if case['请求参数'].find('${name}') != -1:
            case['请求参数'] = case['请求参数'].replace('${name}', str(self.b[0]['name_new']))
        res = Way_request().way_choise(case['请求方法'], case['请求地址'], eval(case['请求参数']))
        if res is not False:
            try:
                comp = res.json()['status']
                eid = eval(case['请求参数'])['eid']
                name = eval(case['请求参数'])['name']
                Excel_object().write_excel(eid, 3)
                Excel_object().write_excel(name, 5)
                self.assertEqual(comp, case['预期结果'])
            except:
                raise
        else:
            pass