# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : member_address_apis.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2023/7/27 22:00
# @Copyright: 北京码同学
from api.base_api import BaseBuyerApi


class AddAddressApi(BaseBuyerApi):
    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/members/address'
        self.method = 'post'
        self.data = {
            "def_addr": 0,
            'ship_address_name': '这是地址别名',
            "name": "沙陌20230530",
            "mobile": "18729399607",
            "region": 2799,
            "addr": "这是详细地址"
        }