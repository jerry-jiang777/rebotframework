# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : login_apis.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2023/7/20 21:08
# @Copyright: 北京码同学
from api.base_api import BaseBuyerApi


class BuyerLoginApi(BaseBuyerApi):

    # 接口的基本信息，统一封装在init函数中
    def __init__(self,username,password):
        super().__init__()
        self.url = f'{self.host}/passport/login'
        self.method = 'post'
        self.data = {
            "username":username,
            "password":password,
            "captcha":'1512',
            "uuid":"asdasdasdasdasdd"
        }