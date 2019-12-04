# encoding:utf-8
import json
import time
import random
import requests
from auto_test.get_token import get_token


def getCardInfo():
    token = get_token()
    checkId = "3433"
    url = 'https://test.selfhealth.cn/cloud/AssessApi/org/updateCardPayStatus?checkId=' + checkId + '&token=' + token
    print(url)
    headers = {
        "Content-Type": "application/json",
        "charset": "UTF-8",
    }  # 响应头

    response = requests.get(url=url, headers=headers, verify=False)
    print(response.text)

# getCardInfo()

def createOrder(cardId):
    token = get_token()
    url = 'https://test.selfhealth.cn/newapi/user/order/createOrder'
    headers = {
        "Content-Type": "application/json",
        "charset": "UTF-8",
    }  # 响应头
    data = {
        "cardId": cardId
    }
    reponse = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    print("createOrder: %s" % reponse)
