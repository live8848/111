# -*- coding: utf-8 -*-
# @Time    : 2021/11/20 18:26
# @Author  : Hello world!
# @E-mail  : loading....
# @File    : report.py

import os, time, datetime
from BeautifulReport import BeautifulReport as br
import unittest


class Report_test:
    def htmlreport(self, suite):
        father_path = os.path.abspath(os.pardir)
        report_name = time.strftime('%Y%m%d-%H%M%S', time.localtime()) + 'rpt.html'
        report_save_path = father_path + '\\output\\pictures' + report_name
        report = br(suite)
        report.report('demo', report_save_path)

