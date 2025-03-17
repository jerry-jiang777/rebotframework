# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : cart_apis.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2023/7/20 21:23
# @Copyright: 北京码同学
from api.base_api import BaseBuyerApi


class AddCartApi(BaseBuyerApi):

    def __init__(self,sku_id):
        super().__init__()
        self.url = f'{self.host}/trade/carts'
        self.method = 'post'
        self.data = {
            "sku_id":sku_id,
            "num":1,
            "activity_id":''
        }
class BuyNowApi(BaseBuyerApi):

    def __init__(self,sku_id):
        super().__init__()
        self.url = f'{self.host}/trade/carts/buy'
        self.method = 'post'
        self.data = {
            "sku_id":sku_id,
            "num":1,
            "activity_id":''
        }

class DeleteCartApi(BaseBuyerApi):

    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/trade/carts'
        self.method = 'delete'