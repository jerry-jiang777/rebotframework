# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : run.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2023/7/20 20:20
# @Copyright: 北京码同学

import os
import sys

import pytest

from common.file_load import load_yaml_file, write_yaml
from paths_manager import common_yaml_path, http_yaml_path, db_yaml_path, redis_yaml_path

if __name__ == '__main__':
    # pytest.main()自动扫描当前pytest.ini中相关的配置，根据配置执行测试
    # pytest.main()
    args = sys.argv
    env_file = f'config/env_uat.yml'
    if len(args) > 1:
        env_name = args[1] # 获取环境名称
        env_file = f'config/env_{env_name}.yml'
        del args[1]
    # 读取要执行的环境配置文件，获取所有配置信息
    env_info = load_yaml_file(env_file)
    # print(env_info['common'])
    # 依次写入各个配置的文件中
    write_yaml(common_yaml_path, env_info['common'])
    write_yaml(http_yaml_path, env_info['http'])
    write_yaml(db_yaml_path, env_info['db'])
    write_yaml(redis_yaml_path, env_info['redis'])
    # pytest.main()自动扫描当前pytest.ini中相关的配置，根据配置执行测试
    pytest.main()
    # 这个是直接打开测试报告，仅仅用于本地自己看
    os.system('allure serve report/data')
