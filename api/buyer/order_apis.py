# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : order_apis.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2023/7/25 20:31
# @Copyright: 北京码同学
from api.base_api import BaseBuyerApi


class OrderRogApi(BaseBuyerApi):

    def __init__(self,order_sn):
        super().__init__()
        self.url = f'{self.host}/trade/orders/{order_sn}/rog'
        self.method = 'post'