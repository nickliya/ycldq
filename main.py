#!/bin/env python
# coding:utf-8
"""
# Copyright (c) 2019-2020
# All Rights Reserved by Thunder Software Technology Co., Ltd and its affiliates.
# You may not use, copy, distribute, modify, transmit in any form this file
# except in compliance with THUNDERSOFT in writing by applicable law.
#
#
# @file    main
# @brief   brief function description.
# @details detailed function description.
# @version 1.0
# @author  yangqing
# @date    2019/11/4 13:59
#
# Edit History
# ----------------------------------------------------------------------------
# DATE                     NAME               DESCRIPTION
# 2019/11/4                 yangqing             Create it.
#
"""
import sys

from PyQt5.QtWidgets import QApplication
from front import mainWindows
from PyQt5 import sip


def main():
    app = QApplication(sys.argv)
    ex = mainWindows.MainWidget()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    # log_info = open('Temp/info.log', 'w')
    # log_err = open('Temp/error.log', 'w')
    # sys.stdout = log_info
    # sys.stderr = log_err
    main()
