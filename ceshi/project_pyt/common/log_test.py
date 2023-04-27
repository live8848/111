# -*- coding: utf-8 -*-
# @Time    : 2021/11/20 11:36
# @Author  : Hello world!
# @E-mail  : loading....
# @File    : log_test.py

import logging, os, time


class Testlog:
    def __init__(self, logger=None):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        self.long_path = os.path.abspath(os.path.abspath(os.pardir)) + '\\output\\logs\\'
        self.create_time = time.strftime('%Y%m%d&%H%M%S', time.localtime())
        self.fh = logging.FileHandler('{}{}.log'.format(self.long_path, self.create_time), encoding='utf-8')
        self.fh.setLevel(logging.INFO)

        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.INFO)

        fh_format = logging.Formatter('%(asctime)s-%(name)s[Line:%(lineno)d]-%(levelname)s:%(message)s')
        self.fh.setFormatter(fh_format)
        self.ch.setFormatter(fh_format)

        # self.logger.removeHandler(self.fh)
        # self.logger.removeHandler(self.ch)

        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)

        self.fh.close()
        self.ch.close()

    def getlog(self):
        return self.logger


# os.path.abspath(os.pardir)