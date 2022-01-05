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
# @date    2019/11/4 17:34
#
# Edit History
# ----------------------------------------------------------------------------
# DATE                     NAME               DESCRIPTION
# 2019/11/4                 yangqing             Create it.
#
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class AdbToolsView(QWidget):
    def __init__(self):
        super(AdbToolsView, self).__init__()

        # label
        self.label_jg1 = QLabel('按键1 间隔')
        self.label_jg2 = QLabel('按键2 间隔')
        self.label_jg3 = QLabel('按键3 间隔')
        self.label_jg4 = QLabel('按键4 间隔')

        self.label_m1 = QLabel('秒')
        self.label_m2 = QLabel('秒')
        self.label_m3 = QLabel('秒')
        self.label_m4 = QLabel('秒')

        self.label_start = QLabel('启动热键')
        self.label_start.setMaximumHeight(15)
        self.label_stop = QLabel('关闭热键')

        # checkbox
        self.checkbox1 = QCheckBox('有效')
        self.checkbox2 = QCheckBox('有效')
        self.checkbox3 = QCheckBox('有效')
        self.checkbox4 = QCheckBox('有效')

        # edit
        self.line_edit1 = QLineEdit('0.1')
        self.line_edit2 = QLineEdit('0.2')
        self.line_edit3 = QLineEdit('0.3')
        self.line_edit4 = QLineEdit('4')
        # self.line_start = QLineEdit('F7')
        self.line_start = QLabel('F7')
        # self.line_stop = QLineEdit('F8')
        self.line_stop = QLabel('F8')

        # btn
        self.save_btn = QPushButton('保存配置')

        # create layout
        self._main_grid = QGridLayout()
        self.__init_grid()

    def __init_grid(self):
        self.setLayout(self._main_grid)

        self._main_grid.addWidget(self.checkbox1, 0, 0)
        self._main_grid.addWidget(self.label_jg1, 0, 1)
        self._main_grid.addWidget(self.line_edit1, 0, 2)
        self._main_grid.addWidget(self.label_m1, 0, 3)

        self._main_grid.addWidget(self.checkbox2, 1, 0)
        self._main_grid.addWidget(self.label_jg2, 1, 1)
        self._main_grid.addWidget(self.line_edit2, 1, 2)
        self._main_grid.addWidget(self.label_m2, 1, 3)

        self._main_grid.addWidget(self.checkbox3, 2, 0)
        self._main_grid.addWidget(self.label_jg3, 2, 1)
        self._main_grid.addWidget(self.line_edit3, 2, 2)
        self._main_grid.addWidget(self.label_m3, 2, 3)

        self._main_grid.addWidget(self.checkbox4, 3, 0)
        self._main_grid.addWidget(self.label_jg4, 3, 1)
        self._main_grid.addWidget(self.line_edit4, 3, 2)
        self._main_grid.addWidget(self.label_m4, 3, 3)

        self._main_grid.addWidget(self.label_start, 4, 0)
        self._main_grid.addWidget(self.line_start, 4, 1)
        self._main_grid.addWidget(self.label_stop, 4, 2)
        self._main_grid.addWidget(self.line_stop, 4, 3)

        self._main_grid.addWidget(self.save_btn, 5, 0)
