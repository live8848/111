# -*- coding: utf-8 -*-
# @Time    : 2021/11/23 10:03
# @Author  : Hello world!
# @E-mail  : loading....
# @File    : runner.py
import unittest, time
import project_connect.test_case.test_add_guest
from BeautifulReport import BeautifulReport


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('.')         # 使用unittest添加一系列存在的用例
    report = BeautifulReport(suite)
    t = time.strftime('%Y%m%d&%H%M%S', time.localtime())     # 生成时间信息
    report.report('demo', '/report/report{}.html'.format(t))