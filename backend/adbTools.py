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
from .ThreadManager import *
import time
import os


def gettime():
    timer = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
    return timer


class AdbTools(AdbToolsView):
    def __init__(self):
        super(AdbTools, self).__init__()
        self.threadpool = QThreadPool.globalInstance()
        self.threadpool.setMaxThreadCount(100)
        self.bindfun()

        self.logcat_thd = None

    def input_key(self, message):
        # print(message)
        if message == "Key.f7":
            self.key_input()
        elif message == "Key.f8":
            self.key_stop()

    def adbroot(self):
        print(self.line_edit1.text())

    def key_input(self):
        wait_time = float(self.line_edit1.text())
        self.input_thd1 = KeyboardInput(wait_time, "1")
        self.input_thd2 = KeyboardInput(wait_time, "2")
        self.input_thd3 = KeyboardInput(wait_time, "3")
        # input_thd.signals.recv_signal.connect(self.filladbmsg)
        self.threadpool.start(self.input_thd1)
        self.threadpool.start(self.input_thd2)
        self.threadpool.start(self.input_thd3)

    def key_stop(self):
        self.input_thd1.stop()
        self.input_thd2.stop()
        self.input_thd3.stop()

    def key_monitor(self):
        monitor_thd = KeyboardMonitor()
        monitor_thd.signals.recv_signal.connect(self.input_key)
        self.threadpool.start(monitor_thd)

    def bindfun(self):
        self.save_btn.clicked.connect(self.adbroot)
        pass
