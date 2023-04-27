# -*- coding: utf-8 -*-
# @Time    : 2021/11/20 13:23
# @Author  : Hello world!
# @E-mail  : loading....
# @File    : elements_object.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
import os, time, datetime
from pywin32 import win32gui,win32con
from ceshi.project_pyt.common.log_test import Testlog

log = Testlog().getlog()

class Element_obj:
    def __init__(self, dr):
        self.dr = dr

    # 等待时间
    def wait_time(self, local, times = 30, frequency = 0.5):
        try:
            time_now = datetime.datetime.now()
            log.info('等待元素{}加载完成'.format(local))
            WebDriverWait(self.dr, times, frequency).until(ec.visibility_of_element_located(local))
            time_now_new = datetime.datetime.now()
            wait_time = time_now_new - time_now
            log.info('等待元素时长：{}'.format(wait_time))
        except:
            log.exception('元素{}加载失败'.format(local))
            self.save_pucture()
            raise

    # 截图
    def save_pucture(self):
        father_path = os.path.abspath(os.pardir)
        img_name = time.strftime('%Y%m%d-%H%M%S', time.localtime()) + '.png'
        screen_save_path = father_path + '\\output\\pictures' + img_name
        log.error('截取图片，名为{}'.format(img_name))
        self.dr.save_screenshot(screen_save_path)

    # 页面跳转
    def switch_into(self, local, type):
        log.info('进入{}页面内部'.format(local))
        now_windows = windows.handles
        while True:
            if type == 'frame':
                try:
                    frame = self.dr.find_element(local)
                    self.dr.switch_to.frame(frame)
                    log.info('成功进入{}页面内'.format(local))
                    break
                except:
                    log.exception('进入页面{}失败'.format(local))
                    self.save_pucture()
                    raise
            elif type == 'window[1]':
                try:
                    self.switch_to.window(now_windows[1])
                    log.info('成功进入窗口{}'.format(now_windows[1]))
                    break
                except:
                    log.exception('进入窗口{}失败'.format(now_windows[1]))
                    self.save_pucture()
                    raise
            elif type == 'window[0]':
                try:
                    self.switch_to.window(now_windows[0])
                    log.info('成功进入窗口{}'.format(now_windows[0]))
                    break
                except:
                    log.exception('进入窗口{}失败'.format(now_windows[0]))
                    self.save_pucture()
                    raise
            else:
                print('参数传递错误')
                log.exception('输入了错误的参数{}'.format(type))


    # 获取元素
    def get_element(self, local):
        log.info('查找元素{}'.format(local))
        try:
            return self.dr.find_element(*local)
        except:
            log.exception('元素{}未找到'.format(local))
            self.save_pucture()
            raise

    # 获取元素组
    def get_elements(self, local):
        log.info('查找元素组：{}'.format(local))
        try:
            elements = self.dr.find_elements(*local)
            log.info('获取到{}个元素'.format(len(elements)))
        except:
            log.exception('元素组{}查找失败'.format(local))
            self.save_pucture()
            raise

    # 元素点击操作
    def click_element(self, local):
        log.info('点击元素{}'.format(local))
        ele = self.get_element(local)
        try:
            ele.click()
            log.info('成功点击元素{}'.format(local))
        except:
            log.error('{}元素点击操作失败'.format(local))
            self.save_picture()

    # 元素输入操作
    def input_element(self, local, text = ''):
        log.info('对元素{}进行输入操作'.format(local))
        ele = self.get_element(local)
        try:
            ele.clear()
            ele.send_keys('{}'.format(text))   #输入的值
            log.info('成功向元素{}输入内容'.format(ipt[1]))
        except:
            log.error('未能成功向元素{}中输入信息'.format(ipt[1]))
            self.save_pucture()

    # 获取元素文本内容
    def get_element_text(self, local):
        log.info('获取元素{}文本内容'.format(local))
        self.wait_time(local)
        ele = self.get_element(local)
        try:
            return ele.text
        except:
            log.exception('获取元素{}文本失败'.format(local))
            self.save_pucture()

    # 获取元素属性名
    def get_element_attribute(self, local, attribute):
        """
        :local 元素定位表达式
        :attribute  元素属性名
        """
        log.info('获取元素{}属性值'.format(local))
        self.wait_time(local)
        ele = self.get_element(local)
        try:
            return ele.get_attribute(attribute)
        except:
            log.exception('元素{}属性获取失败'.format(local))
            self.save_pucture()

    # 上传文件
    def updata_file(self, file_path):
        a = win32gui.FindWindow(None, '打开')
        log.info('查找文件上传窗口：{}'.format(a))
        b = win32gui.FindWindowEx(a, 0, "ComboBoxEx32", None)
        log.info('查找文件路径输入窗口:{}'.format(b))
        c = win32gui.FindWindowEx(b, 0, "Button", '打开(&O)')
        log.info('查找文件上传确定按钮：{}'.format(c))
        win32gui.SendMessage(b, win32con.WM_SETTEXT, None, file_path)
        log.info('在文件上传路径栏输入上传文件路径：{}'.format(file_path))
        win32gui.SendMessage(a, win32con.WM_COMMAND, 1, c)
        log.info('点击确认上传文件按键！')