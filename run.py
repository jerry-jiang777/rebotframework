# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : run.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2023/7/20 20:20
# @Copyright: 北京码同学

import os

import pytest

if __name__ == '__main__':
    # pytest.main()自动扫描当前pytest.ini中相关的配置，根据配置执行测试
    pytest.main()

    # 这个是直接打开测试报告，仅仅用于本地自己看
    os.system('allure serve report/data')
