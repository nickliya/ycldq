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


def rescheck(func):
    def wrapper(self, *args, **kwargs):
        proc = func(self)
        errmsg = proc.stderr.read().decode('gbk')
        if errmsg:
            self.adbmsgbrs.setText(errmsg)
        else:
            self.adbmsgbrs.setText(proc.stdout.read())

    return wrapper


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

    def filladbmsg(self, message):
        if 'no devices/emulators found' in message:
            QMessageBox.information(self, 'info', '无法检测到设备', QMessageBox.Yes, QMessageBox.Yes)
        self.adbmsgbrs.append(message)

    def adbroot(self):
        cmd = 'adb root'
        root_thd = AdbThdCommom(cmd, self.rootbtn)
        root_thd.signals.recv_signal.connect(self.filladbmsg)
        self.adbmsgbrs.clear()
        self.threadpool.start(root_thd)

    def adbremount(self):
        cmd = 'adb remount'
        remount_thd = AdbThdCommom(cmd, self.remountbtn)
        remount_thd.signals.recv_signal.connect(self.filladbmsg)
        self.adbmsgbrs.clear()
        self.threadpool.start(remount_thd)

    def screenshoot(self):
        scrennshoot_thd = AdbThdScreenShoot(self.screenshootbtn)
        scrennshoot_thd.signals.recv_signal.connect(self.filladbmsg)
        self.adbmsgbrs.clear()
        self.threadpool.start(scrennshoot_thd)

    def bindfun(self):
        # self.rootbtn.clicked.connect(self.adbroot)
        # self.remountbtn.clicked.connect(self.adbremount)
        # self.devicesbtn.clicked.connect(self.adbdevices)
        #
        # self.get_btnlist["btn_navi"].clicked.connect(lambda: self.getxlog(self.get_btnlist["btn_navi"]))
        #
        pass
