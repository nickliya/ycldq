#!/bin/env python
# coding:utf-8
"""
# Copyright (c) 2019-2020
# All Rights Reserved by Thunder Software Technology Co., Ltd and its affiliates.
# You may not use, copy, distribute, modify, transmit in any form this file
# except in compliance with THUNDERSOFT in writing by applicable law.
#
#
# @file    ThreadManager
# @brief   brief function description.
# @details detailed function description.
# @version 1.0
# @author  yangqing
# @date    2019/11/14 11:35
#
# Edit History
# ----------------------------------------------------------------------------
# DATE                     NAME               DESCRIPTION
# 2019/11/14                 yangqing             Create it.
#
"""
from PyQt5 import QtCore
from PyQt5.QtCore import *
from pynput import keyboard
from pynput.keyboard import Key, Controller
import time


class WorkerSignals(QObject):
    """工作信号"""
    recv_signal = QtCore.pyqtSignal(str)
    send_signal = QtCore.pyqtSignal(str)
    animate_signal = QtCore.pyqtSignal(str)
    clickable_signal = QtCore.pyqtSignal(bool)
    swibtn_change_signal = QtCore.pyqtSignal(bool)


class AdbThread(QRunnable):
    def __init__(self):
        """
        线程类
        """
        super(AdbThread, self).__init__()
        self.signals = WorkerSignals()


class KeyboardMonitor(AdbThread):
    def __init__(self):
        """
        线程类
        """
        super(KeyboardMonitor, self).__init__()
        self.signals = WorkerSignals()

    def run(self):
        # Collect events until released
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as self.listener:
            self.listener.join()

        # self.listener.start()

    def stop(self):
        self.listener.stop()

    def on_press(self, key):
        try:
            # print('alphanumeric key {0} pressed'.format(key.char))
            self.signals.recv_signal.emit(str(key))
        except AttributeError:
            print('special key {0} pressed'.format(key))

    def on_release(self, key):
        # print('{0} released'.format(key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False


class KeyboardInput(AdbThread):
    def __init__(self, wait_time, input_key):
        """
        线程类
        """
        super(KeyboardInput, self).__init__()
        self.signals = WorkerSignals()
        self.keyboard = Controller()
        self.index = True
        self.time = wait_time
        self.input_key = input_key

    def run(self):
        # Collect events until released
        while self.index:
            self.keyboard.press(self.input_key)
            self.keyboard.release(self.input_key)
            time.sleep(self.time)

    def stop(self):
        # Collect events until released
        self.index = False
