import requests
import json

def get_token():
    # url = 'https://new.selfhealth.com.cn/api/AssessApi/get_token'
    # url = 'https://dev.selfhealth.cn/api/AssessApi/get_token'
    url = 'https://test.selfhealth.com.cn/api/AssessApi/get_token'
    # url = 'https://pred.selfhealth.com.cn/api/AssessApi/get_token'
    headers = {
        "Content-Type": "application/json",
        "charset": "UTF-8"
    }
    data = {
        "apikey": "8469d381-d6b0-43f9-a0ca-5780ba8a9c73",
        "secret": "fe42735cf4266b67fb61feb9ea009d03455f9d24fea5867784aa2eaed74d98a2" # 燕鑫康达科室key和密钥
        # "apikey": "9f2efdd7-ee6b-49b8-9ef8-e9ab863fc221",
        # "secret": "7f42ad2a7c31fc5e3b78430da6c8815416a3a7d226ed5d8782672c47ed703d2e" # 仁济科室key和密钥
        # "apikey": "03ec39be-bada-49f2-97ea-852aeb8e18b1",
        # "secret": "5b64aed8b4bb8aefa2a199e0e44db8f8dfe6dc0eeb3ae965a12378f49854744a"  # wlt测试科室key和密钥 dev
        # "apikey": "7105e585-d746-4da0-9051-c7252f2a46ae",
        # "secret": "3ad06bf7eacd5a29cbd89f4644a809735994e45f3fbc1e1dbbd57bb61e173929"  # wlt测试科室key和密钥 test new
        # "apikey": "15c27c3f-5d56-42e4-b221-e6009f94bd51",
        # "secret": "fc004b54ac7e3efdd13a8dd7bab6469904a50727be378fe33934c28e56eefa46"  # 浙江省中医院（湖滨院区）健康管理中心
        # "apikey":"d1f6722e-db64-4729-ba57-703ea0eb7da9",
        # "secret":"1a60e8268961b3c37560f494a18af14c145e7346d7acc5b5d41ac7dae3e436e9"  # 杭疗
        # "apikey":"8d345c73-a1b8-4172-88a4-e21939d0e3f9",
        # "secret":"81267adacd411d11fb35ac98be2a8239954b20d09fd868c33312704ee37b0a02"  # 迪安  test
        # "apikey": "68d9875c-9d84-4b7f-89ca-5ef4b8f90b5d",
        # "secret": "33ad070198adc18a58a4a26bcfb693e7d7f17db555304b5e4736112c9522f040"  # 迪安   pred
    }
    response = requests.post(url=url, headers=headers, data=json.dumps(data), verify=False)
    res_data = json.loads(response.text)
    token = res_data['data']['token'] # 获取token值
    # print(token)
    return token # 返回token

# get_token()



