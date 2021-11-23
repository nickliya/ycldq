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


def rescheck(func):
    def wrapper(self, *args, **kwargs):
        proc = func(self)
        errmsg = proc.stderr.read().decode('gbk')
        if errmsg:
            self.adbmsgbrs.setText(errmsg)
        else:
            self.adbmsgbrs.setText(proc.stdout.read())
        self.btn.setEnabled(True)

    return wrapper


def resemit(proc, signals):
    # 规避adb pull 卡死,先用out接收
    outmsg = proc.stdout.read().decode('gbk')
    errmsg = proc.stderr.read().decode('gbk')
    if errmsg:
        signals.recv_signal.emit(errmsg)
        return False, errmsg
    else:
        signals.recv_signal.emit(outmsg)
        return True, outmsg


def res_emit_keepon(proc, signals):
    outmsg = None
    while proc.poll() is None:
        outmsg = proc.stdout.readline().decode('gbk')
        outmsg = outmsg.strip()
        if outmsg:
            signals.recv_signal.emit(outmsg)

    errmsg = proc.stderr.read().decode('gbk')
    if errmsg:
        signals.recv_signal.emit(errmsg)
        return False, errmsg
    else:
        return True, outmsg


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


class AdbThdCommom(AdbThread):
    def __init__(self, cmd, btn=None):
        """
        公共adb命令线程
        :param cmd: 命令行
        :param btn: 按钮，默认为空
        :param collection: 数据采集的接收路径，默认为空
        """
        super(AdbThdCommom, self).__init__()
        self.command = cmd
        self.btn = btn

    def run(self):
        """
        命令行执行
        :return:
        """
        self.btn.setEnabled(False)

        if type(self.command) == list:
            for cmd in self.command:
                proc = self.adb.popen(cmd)
                stopindex, res = resemit(proc, self.signals)
                if stopindex is False:
                    break
        else:
            proc = self.adb.popen(self.command)
            resemit(proc, self.signals)

        self.btn.setEnabled(True)

