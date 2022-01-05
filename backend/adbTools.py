#!/bin/env python
# coding:utf-8
"""
# Copyright (c) 2019-2020
# All Rights Reserved by Thunder Software Technology Co., Ltd and its affiliates.
# You may not use, copy, distribute, modify, transmit in any form this file
# except in compliance with THUNDERSOFT in writing by applicable law.
#
#
# @file    dataProcessing
# @brief   brief function description.
# @details detailed function description.
# @version 1.0
# @author  yangqing
# @date    2019/11/13 15:42
#
# Edit History
# ----------------------------------------------------------------------------
# DATE                     NAME               DESCRIPTION
# 2019/11/13                 yangqing             Create it.
#
"""
from front.adbToolsView import AdbToolsView
from front.adbToolsView import QMessageBox
from PyQt5.QtCore import QThreadPool
from backend.ThreadManager import *
import time


def gettime():
    timer = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
    return timer


class AdbTools(AdbToolsView):
    def __init__(self):
        super(AdbTools, self).__init__()
        self.threadpool = QThreadPool.globalInstance()
        self.threadpool.setMaxThreadCount(100)
        self.bindfun()
        self.thd_list = []

        self.logcat_thd = None
        self.disable = True

    def input_key(self, message):
        print(message)
        if message == "Key.f7":
            if self.disable:
                self.key_input()
                self.disable = False
            else:
                # QMessageBox
                self.msgBox = QMessageBox.warning(self, '提示', "当前已经是启动状态!\n请先按F8停止，再按F7启动")

        elif message == "Key.f8":
            if not self.disable:
                self.key_stop()
                self.disable = True
            else:
                pass

    def adbroot(self):
        print(self.line_edit1.text())

    def key_input(self):
        self.stop_list = []
        if self.checkbox1.checkState():
            wait_time1 = float(self.line_edit1.text())
            self.input_thd1 = KeyboardInput(wait_time1, "1")
            self.threadpool.start(self.input_thd1)
            self.stop_list.append(self.input_thd1)
            self.thd_list.append(self.input_thd1)

        if self.checkbox2.checkState():
            wait_time2 = float(self.line_edit2.text())
            self.input_thd2 = KeyboardInput(wait_time2, "2")
            self.threadpool.start(self.input_thd2)
            self.stop_list.append(self.input_thd2)
            self.thd_list.append(self.input_thd2)

        if self.checkbox3.checkState():
            wait_time3 = float(self.line_edit3.text())
            self.input_thd3 = KeyboardInput(wait_time3, "3")
            self.threadpool.start(self.input_thd3)
            self.stop_list.append(self.input_thd3)
            self.thd_list.append(self.input_thd3)

        if self.checkbox4.checkState():
            wait_time4 = float(self.line_edit4.text())
            self.input_thd4 = KeyboardInput(wait_time4, "4")
            self.threadpool.start(self.input_thd4)
            self.stop_list.append(self.input_thd4)
            self.thd_list.append(self.input_thd4)

    def key_stop(self):
        for i in self.stop_list:
            i.stop()

    def key_monitor(self):
        monitor_thd = KeyboardMonitor()
        monitor_thd.signals.recv_signal.connect(self.input_key)
        self.threadpool.start(monitor_thd)
        self.thd_list.append(monitor_thd)

    def bindfun(self):
        self.save_btn.clicked.connect(self.adbroot)
        pass
