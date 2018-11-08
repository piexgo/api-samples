#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8


from piexgoAPI import PIEXGO
import time

## 填写 apiKey APISECRET
apiKey = '23db31c6-6fd7-4041-9388-81dea6a05087'
secretKey = '7bea08b911022f8eece9dbd0b86facb86011c662'


API_BASE_URL = 'api.piexgo.co'

## Create a instance

client = PIEXGO(API_BASE_URL, apiKey, secretKey)


#print(client.pairs())

#print(client.tickers())

#print(client.ticker('symbol=BTC_USDT'))

#print(client.orderBook('symbol=BTC_USDT'))

#print(client.tradeHistory('symbol=BTC_USDT'))

print(client.account())

#print(client.orderHistory("BTC_USDT",0))

#print(client.openOrders('0'))

#print(client.order('7000','0.1','BTC_USDT','BUY','limit'))

#print(client.cancelOrder('BTC_USDT','1060499209679016091"'))

