# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : client.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2023/7/20 20:34
# @Copyright: 北京码同学
import requests

from common.logger import GetLogger


class RequestsClient:

    session = requests.session()

    # 要发起一个接口的调用需要用到哪些信息
    def __init__(self):
        self.url = None
        self.method = None
        self.headers = None
        self.params = None
        self.data = None
        self.json = None
        self.files = None
        self.resp = None

    def send(self):
        # 发起之前记录请求信息
        GetLogger.get_logger().debug(f'=================================================')
        GetLogger.get_logger().debug(f'接口url:{self.url}')
        GetLogger.get_logger().debug(f'接口method:{self.method}')
        GetLogger.get_logger().debug(f'接口headers:{self.headers}')
        GetLogger.get_logger().debug(f'接口params:{self.params}')
        GetLogger.get_logger().debug(f'接口data:{self.data}')
        GetLogger.get_logger().debug(f'接口json:{self.json}')
        GetLogger.get_logger().debug(f'接口files:{self.files}')
        # verify=False 该参数表示忽略https的证书校验
        try:
            self.resp = RequestsClient.session.request(method=self.method,
                                                       url=self.url,
                                                       headers=self.headers,
                                                       params=self.params,
                                                       data=self.data,
                                                       json=self.json,
                                                       files=self.files,
                                                       verify=False)
            GetLogger.get_logger().debug(f'接口响应状态码:{self.resp.status_code}')
            GetLogger.get_logger().debug(f'接口响应body:{self.resp.text}')
        except BaseException as e:
            GetLogger.get_logger().exception(f'接口发起失败')
            raise BaseException(f'接口发起失败:{e}')
        return self.resp