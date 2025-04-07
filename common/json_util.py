from operator import index

import jsonpath
import jsonpath_ng
from jsonpath_ng import parse, Index, Fields

from common.logger import GetLogger


def update_value_to_json(json_object,json_path,new_value):
    """
    json数据替换或者删除
    :param json_object: 目标对象
    :param json_path: 目标参数对应的jsonpath
    :param new_value: 目标参数的新值，如果是$del代表要删除通过jsonpath匹配到的参数
    :return:
    """
    jsonpath_expr = parse(json_path)
    matches = jsonpath_expr.find(json_object)
    for match in matches:
        path = match.path # 获取当前匹配结果的路径
        if isinstance(path,Index):# 判断他是不是索引对象路径
            if new_value=='$del':# 如果new_value是$del那么我认为你是要删除目标参数
                del match.context.value[match.path.index]
            else:
                match.context.value[match.path.index] = new_value # 完成数据替换
        elif isinstance(path,Fields):# 判断他是不是字段路径
            if new_value=='$del':# 如果new_value是$del那么我认为你是要删除目标参数
                del match.context.value[match.path.fields[0]]
            else:
                match.context.value[match.path.fields[0]] = new_value # 完成数据替换
    return json_object



def extract_json(json_object, json_path, index=0):
    """
    json数据提取
    :param json_object:目标对象
    :param json_path:jsonpath表达式
    :param index:要提取的结果中的第几个, 默认是第一个, 传小于0是要所有
    :return:
    """
    logger = GetLogger.get_logger()
    res = jsonpath.jsonpath(json_object, json_path)
    # res如果提取到了值那么他是一个列表, 如果没匹配到他是False
    if res:
        if index < 0:
            # 如果index<0,则认为是你要所有的匹配结果
            logger.info(f"通过{json_path}匹配到的结果是: {res}")
            return res
        else:
            # 如果不小于0,那么你传几, 就代表你要匹配的某一个
            logger.info(f"通过{json_path}匹配到的结果是: {res[index]}")
            return res[index]

    else:
        logger.info(f"通过{json_path}m没有提取到值")


if __name__ == "__main__":
    json_object = {
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
    print(update_value_to_json(json_object, '$.goods_name','guixuejiang'))
    print(update_value_to_json(json_object, '$.goods_gallery_list[0]','xxxx'))
    print(update_value_to_json(json_object, '$.goods_name','$del'))
    print(update_value_to_json(json_object, '$.goods_gallery_list[0]', '$del'))