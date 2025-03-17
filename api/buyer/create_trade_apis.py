# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : create_trade_apis.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2023/7/22 15:25
# @Copyright: 北京码同学
from api.base_api import BaseBuyerApi


class CreateTradeApi(BaseBuyerApi):

    def __init__(self,client='PC',way='BUY_NOW'):
        super().__init__()
        self.url = f'{self.host}/trade/create'
        self.method = 'post'
        self.data = {
            "client":client,
            "way":way
        }