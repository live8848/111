# -*- coding: utf-8 -*-
# @Time    : 2021/12/10 16:19
# @Author  : Hello world!
# @E-mail  : loading....
# @File    : boser_type.py

from selenium import webdriver
from project_pyt.common.log_test import Testlog


logging = Testlog().getlog()
def Chose_type(type_in):
    if type_in == 1:
        dr = webdriver.Chrome()
        logging.info('')
    elif type_in == 2:
        dr = webdriver.Firefox()
        logging.info()
    else:
        logging.exception('no type')
    return dr



