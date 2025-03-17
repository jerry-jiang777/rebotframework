# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : goods_apis.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2023/7/25 20:07
# @Copyright: 北京码同学
from api.base_api import BaseSellerApi


class AddGoodsApi(BaseSellerApi):
    """卖家添加商品"""
    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/seller/goods'
        self.method = 'post'
        self.json = {
            "brand_id": "",
            "category_id": 83,
            "category_name": "",
            "goods_name": "沙陌0530班商品",
            "sn": "sn05300",
            "price": "179",
            "mktprice": "180",
            "cost": "7",
            "weight": "1",
            "goods_gallery_list": [{
                "img_id": -1,
                "original": "http://82.156.74.26:7000/statics/attachment/goods/2023/7/25/20/12499927.png",
                "sort": 0
            }],
            "quantity": 99999999,
            "goods_transfee_charge": 1,
            "has_changed": 0,
            "market_enable": 1,
            "template_id": 0,
            "exchange": {
                "category_id": "",
                "enable_exchange": 0,
                "exchange_money": 0,
                "exchange_point": 0
            },
            "shop_cat_id": 0,
            "meta_description": "",
            "meta_keywords": "",
            "page_title": "",
            "goods_params_list": [],
            "sku_list": [],
            "intro": "<p>这是说明</p>"
        }


class ChangeGoodsApi(BaseSellerApi):
    """卖家修改商品信息"""
    def __init__(self, goods_id):
        super().__init__()
        self.url = f'{self.url}/seller/goods/{goods_id}'
        self.method = 'put'
        self.json = {
            "goods_id": goods_id,
            "category_id": 83,
            "category_name": "厨房用品&gt;锅具水壶 &gt;炒锅",
            "shop_cat_id": 0,
            "brand_id": None,
            "goods_name": "沙陌0530班商品",
            "sn": "sn05300",
            "price": 179,
            "cost": 7,
            "mktprice": "181",
            "weight": 1,
            "goods_transfee_charge": 1,
            "intro": "<p>这是说明</p>",
            "have_spec": 0,
            "quantity": 99999999,
            "market_enable": 1,
            "goods_gallery_list": [{
                "img_id": 39588,
                "original": "http://82.156.74.26:7000/statics/attachment/goods/2023/7/25/20/12499927.png",
                "sort": None
            }],
            "page_title": "沙陌0530班商品",
            "meta_keywords": "沙陌0530班商品",
            "meta_description": "沙陌0530班商品",
            "template_id": 0,
            "is_auth": 0,
            "enable_quantity": 99999999,
            "auth_message": None,
            "goods_type": "NORMAL",
            "exchange": {
                "category_id": "",
                "enable_exchange": 0,
                "exchange_money": 0,
                "exchange_point": 0
            },
            "category_ids": [79, 80, 83],
            "promotion_tip": "此商品参与的[满优惠]促销活动,修改上架后将会被取消",
            "sku_list": [],
            "has_changed": 0
        }


class GoodsUnderApi(BaseSellerApi):
    """卖家下架商品"""

    def __init__(self, goods_ids:list):
        super().__init__()
        goods_ids = ",".join([str(i) for i in goods_ids])
        self.url = f"{self.host}/seller/goods/{goods_ids}/under"
        self.method = 'put'
        self.data = {
            "reason": "没啥理由，卖不动"
        }



class GoodsRecycleApi(BaseSellerApi):
    """卖家把商品放入回收站"""
    def __init__(self, goods_ids:list):
        super().__init__()
        goods_ids = ",".join([str(i) for i in goods_ids])
        self.url = f"{self.host}/seller/goods/{goods_ids}/recycle"
        self.method = "put"

class GoodsDeleteApi(BaseSellerApi):
    """卖家彻底删除商品"""
    def __init__(self, goods_ids:list):
        super().__init__()
        goods_ids = ",".join([str(i) for i in goods_ids])
        self.url = f'{self.host}/seller/goods/{goods_ids}'
        self.method = "delete"
