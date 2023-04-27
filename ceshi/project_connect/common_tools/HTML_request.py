# -*- coding: utf-8 -*-
# @Time    : 2021/11/23 10:10
# @Author  : Hello world!
# @E-mail  : loading....
# @File    : HTML_request.py
import requests

class Way_request:
    """请求方式选择"""
    def way_choise(self, way, url, datas, header=''):
        if way == 'get':
            res = requests.get(url, datas, headers=header)
        elif way == 'post':
            res = requests.post(url, datas, headers=header)
        else:
            print('没有这种方式！')
            res = False
        return res