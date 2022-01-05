#!/bin/env python
# coding:utf-8
"""
# Copyright (c) 2019-2020
# All Rights Reserved by Thunder Software Technology Co., Ltd and its affiliates.
# You may not use, copy, distribute, modify, transmit in any form this file
# except in compliance with THUNDERSOFT in writing by applicable law.
#
#
# @file    mainWidget
# @brief   brief function description.
# @details detailed function description.
# @version 1.0
# @author  yangqing
# @date    2019/11/4 15:11
#
# Edit History
# ----------------------------------------------------------------------------
# DATE                     NAME               DESCRIPTION
# 2019/11/4                 yangqing             Create it.
#
"""
import sys

from PyQt5.QtWidgets import QAction, QMainWindow, QDesktopWidget, QGridLayout, QWidget,QApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication
from backend.adbTools import AdbTools

import cgitb
import time
import shutil
import os

cgitb.enable(format='text')  # 解决pyqt5异常只要进入事件循环,程序就崩溃,而没有任何提示

stopsingle = None
waitmsg = None


class MainWidget(QMainWindow):
    """
    主窗口界面
    """

    def __init__(self):
        super(MainWidget, self).__init__()
        self.dataprocessing = AdbTools()

        self.init_ui()
        self.ini_grid()
        self.init_menu()

    def center(self):
        """控件居中"""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def init_menu(self):
        """
        菜单栏
        :return:
        """
        menubar = self.menuBar()

        # file menu
        menuAction5 = QAction(QIcon('exit.png'), '&Exit', self)
        menuAction5.setShortcut(u'Ctrl+Q')
        menuAction5.setStatusTip('Exit application')

        file_menu = menubar.addMenu('File')
        file_menu.addAction(menuAction5)

    def init_ui(self):
        self.setWindowTitle(u'连点器')
        self.statusBar()
        # self.setWindowIcon(QIcon('Resource/icon.ico'))

        self.resize(300, 350)

        # 创建widget窗口实例
        self.center()

    def ini_grid(self):
        self.maingrid = QGridLayout()
        # 创建widget窗口实例
        main_frame = QWidget()
        # 加载布局
        main_frame.setLayout(self.maingrid)
        # 把widget窗口加载到主窗口的中央位置
        self.setCentralWidget(main_frame)
        self.maingrid.setRowStretch(0, 0)
        self.maingrid.addWidget(self.dataprocessing, 0, 0)

    def showEvent(self, event):
        self.dataprocessing.key_monitor()

    def closeEvent(self, event):
        for i in self.dataprocessing.thd_list:
            i.stop()