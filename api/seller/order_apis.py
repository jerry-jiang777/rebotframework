# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : order_apis.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2023/7/25 20:21
# @Copyright: 北京码同学
from api.base_api import BaseSellerApi


class OrderDeliveryApi(BaseSellerApi):

    def __init__(self,order_sn):
        super().__init__()
        self.url = f'{self.host}/seller/trade/orders/{order_sn}/delivery'
        self.method = 'post'
        self.data = {
            "ship_no":"ashhdhdh",# 快递号
            "logi_id":13,
            "logi_name":"中通01"
        }

class OrderPayApi(BaseSellerApi):

    def __init__(self,order_sn,pay_price):
        super().__init__()
        self.url = f'{self.host}/seller/trade/orders/{order_sn}/pay'
        self.method = 'post'
        self.data = {
            "pay_price":pay_price
        }