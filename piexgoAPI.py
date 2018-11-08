#!/usr/bin/python
# -*- coding: utf-8 -*-


from HttpUtil import getSign, httpGet, httpPost

class PIEXGO:
    def __init__(self, url, apiKey, secretKey):
        self.__url = url
        self.__apiKey = apiKey
        self.__secretKey = secretKey

    ## General methods that query the exchange

    #所有交易对
    def pairs(self):
        URL = "/v1/symbols"
        params=''
        return httpGet(self.__url, URL, params)


    #所有交易行情
    def tickers(self):
        URL = "/v1/tickers"
        params=''
        return httpGet(self.__url, URL, params)

    #单品种交易行情
    def ticker(self, param):
        URL = "/v1/ticker"
        return httpGet(self.__url, URL, param)

    # 交易对市场深度
    def orderBook(self, param):
        URL = "/v1/orderBook"
        return httpGet(self.__url, URL, param)

    # 历史成交记录
    def tradeHistory(self, param):
        URL = "/v1/trades"
        return httpGet(self.__url, URL, param)

    ## Methods that make use of the users keys

    #获取帐号资金余额
    def account(self):
        URL = "/v1/account"
        param = {}
        return httpPost(self.__url, URL, param, self.__apiKey, self.__secretKey)

    # 下单
    def order(self, price,quantity,symbol,side,orderType):
        URL = "/v1/order"
        params = {'price': price,'quantity':quantity, 'symbol':symbol,'side':side,'type':orderType}
        return httpPost(self.__url, URL, params, self.__apiKey, self.__secretKey)


    # 取消订单
    def cancelOrder(self, symbol,orderId):
        URL = "/v1/cancelOrder"
        params = {'symbol': symbol, 'order_id': orderId}
        return httpPost(self.__url, URL, params, self.__apiKey, self.__secretKey)


    # 获取我的当前挂单列表
    def openOrders(self,page):
        URL = "/v1/openOrders"
        params = {'page': page}
        return httpPost(self.__url, URL, params, self.__apiKey, self.__secretKey)

    # 获取我的历史订单
    def orderHistory(self, symbol,page):
        URL = "/v1/orderHistory"
        params = {'symbol':symbol,'page': page}
        return httpPost(self.__url, URL, params, self.__apiKey, self.__secretKey)

