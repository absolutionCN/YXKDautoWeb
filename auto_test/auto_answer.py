# encoding:utf-8
import json
import time
import random
import requests
# from auto_test.create_card import create_card
from auto_test.createcard_adduser import uacadduser
from auto_test.get_token import get_token
from auto_test.getCardInfo import getCardInfo


class answer_question(object):
    def __init__(self):
        self.headers = {
            "Content-Type": "application/json",
            "charset": "UTF-8"
        }  # 响应头
        # self.cls = 'new'
        self.cls = 'test'
        # self.cls = 'dev'
        # self.cls = 'pred'

    def get_first_question(self, cardId, token):
        data = {
            "cardId": cardId
        }  # 传递参数
        # print('获取第一次问题数据%s' % data)
        url = 'https://' + self.cls + '.selfhealth.com.cn/newapi/AssessApi/questionnaire/getFirstQuestion?token=' + token
        response = requests.post(url, headers=self.headers, data=json.dumps(data), verify=False)  # 返回响应
        res_dict = json.loads(response.text)
        print('get_first%s' % res_dict)
        self.resultId = res_dict['data']['resultId']  # 获取resultId
        questionSer = res_dict['data']['questionsDomain']['questionSer']  # 获取数据
        sectionIndex = res_dict['data']['sectionIndex']  # 获取维度
        questionType = res_dict['data']['questionsDomain']['questionType']  # 获取题目类型
        questionsDomain = res_dict['data']['questionsDomain']  # 获取返回的信息
        options = res_dict['data']['questionsDomain']['options']
        print("获取第一题：%s" % options)
        # option = options[random.randint(1, len(options))]['optionTag'] # 获取选项
        self.answer_dict = {'questionSer': questionSer, 'sectionIndex': sectionIndex,
                            'questionType': questionType, 'questionsDomain': questionsDomain, 'answerDomainList': None,
                            'options': options}  # 将参数添加到字典中。全局变量

    def answer(self, cardId, token):
        option = self.answer_dict['options'][random.randint(0, len(self.answer_dict['options']) - 1)]["optionTag"]
        data = {
            "answerDTO": {
                "optionDTOList": [
                    {
                        "tag": option
                        # 随机获取选项
                    }
                ]
            },
            "cardId": cardId,
            "questionSer": self.answer_dict['questionSer'],
            "resultId": self.resultId,
            "sectionIndex": self.answer_dict['sectionIndex']
        }  # 传递参数
        url = 'https://' + self.cls + '.selfhealth.com.cn/newapi/AssessApi/questionnaire/answer?token=' + token
        questionsDomain = None
        questionType = None
        questionSer = None
        sectionIndex = None
        answerDomainList = None
        options = None
        # 定义参数
        if self.answer_dict['questionType'] == "SINGLE_CHOICE":
            print('回答单选问题%s' % data)
            print(url)
            response = requests.post(url, headers=self.headers, data=json.dumps(data), verify=False)
            res_dict = json.loads(response.text)
            print('single_choice%s ' % res_dict)

            if res_dict['data']['questionsDomain'] is not None:
                questionSer = res_dict['data']['questionsDomain']['questionSer']
                sectionIndex = res_dict['data']['sectionIndex']
                questionType = res_dict['data']['questionsDomain']['questionType']
                questionsDomain = res_dict['data']['questionsDomain']
                answerDomainList = res_dict['data']['answerDomainList']
                options = res_dict['data']['questionsDomain']['options']
                print('单选选项：%s' % options)
            self.answer_dict = {'questionSer': questionSer, 'sectionIndex': sectionIndex,
                                'questionType': questionType, 'questionsDomain': questionsDomain,
                                'answerDomainList': answerDomainList, 'options': options}


        elif self.answer_dict['questionType'] == "MULTI_CHOICE":
            print('回答多选问题%s' % data)
            response = requests.post(url, headers=self.headers, data=json.dumps(data), verify=False)
            res_dict = json.loads(response.text)
            print(res_dict)
            print('multi_choice%s' % res_dict)
            questionSer = res_dict['data']['questionsDomain']['questionSer']
            sectionIndex = res_dict['data']['sectionIndex']
            questionType = res_dict['data']['questionsDomain']['questionType']
            questionsDomain = res_dict['data']['questionsDomain']
            answerDomainList = res_dict['data']['answerDomainList']
            options = res_dict['data']['questionsDomain']['options']
            print('多选选项：%s' % options)
            self.answer_dict = {'questionSer': questionSer, 'sectionIndex': sectionIndex,
                                'questionType': questionType, 'questionsDomain': questionsDomain,
                                'answerDomainList': answerDomainList, "options": options}

        else:
            data = {
                "answerDTO": {
                    "optionDTOList": [
                        {
                            "option": random.randint(1, 250),
                        }
                    ]
                },
                "cardId": uacadduser(),
                "questionSer": self.answer_dict['questionSer'],
                "resultId": self.resultId,
                "sectionIndex": self.answer_dict['sectionIndex']
            }
            print('填空选项%s' % data)
            response = requests.post(url, headers=self.headers, data=json.dumps(data), verify=False)
            res_dict = json.loads(response.text)
            print('填空%s' % res_dict)
            questionSer = res_dict['data']['questionsDomain']['questionSer']
            sectionIndex = res_dict['data']['sectionIndex']
            questionType = res_dict['data']['questionsDomain']['questionType']
            questionsDomain = res_dict['data']['questionsDomain']
            answerDomainList = res_dict['data']['answerDomainList']
            options = res_dict['data']['questionsDomain']['options']
            self.answer_dict = {'questionSer': questionSer, 'sectionIndex': sectionIndex,
                                'questionType': questionType, 'questionsDomain': questionsDomain,
                                'answerDomainList': answerDomainList, 'options': options}

    def move_to_next(self, cardId, token):
        url = 'https://' + self.cls + '.selfhealth.com.cn/newapi/AssessApi/questionnaire/moveToNext?token=' + token
        data = {
            "answerDTO": {
                "optionDTOList": [
                    {
                        "tag": "A"
                        # 随机获取选项
                    }
                ]
            },
            "cardId": cardId,
            "questionSer": self.answer_dict['questionSer'],
            "resultId": self.resultId,
            "sectionIndex": self.answer_dict['sectionIndex']
        }
        # print('跳转下一题数据%s' % data)
        response = requests.post(url, headers=self.headers, data=json.dumps(data), verify=False)
        res_dict = json.loads(response.text)
        # print('movetonext %s' % res_dict)
        questionSer = res_dict['data']['questionsDomain']['questionSer']
        sectionIndex = res_dict['data']['sectionIndex']
        questionType = res_dict['data']['questionsDomain']['questionType']
        questionsDomain = res_dict['data']['questionsDomain']
        answerDomainList = res_dict['data']['answerDomainList']
        options = res_dict['data']['questionsDomain']['options']
        # print('跳转到下一题：%s' % options)
        self.answer_dict = {'questionSer': questionSer, 'sectionIndex': sectionIndex,
                            'questionType': questionType, 'questionsDomain': questionsDomain,
                            'answerDomainList': answerDomainList, 'options': options}

    def get_report(self, cardId):
        url = 'https://' + self.cls + '.selfhealth.com.cn/newapi/user/report/getReport'
        data = {
            "cardId": cardId
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(data), verify=False)
        res_dict = json.loads(response.text)

    def createOrder(self, cardId):
        url = 'https://' + self.cls + '.selfhealth.com.cn/newapi/user/order/createOrder'

        data = {
            "cardId": cardId
        }
        reponse = requests.post(url, headers=self.headers, data=json.dumps(data), verify=False)
        print("createOrder: %s" % reponse)

    def upload_data(self, name, phone, idcard, checkId, token):
        url = "https://" + self.cls + ".selfhealth.com.cn/api/v3.0/physical_examination_datas?token=" + token
        self.headers = {
            "Content-Type": "application/json",
            "charset": "UTF-8"
        }
        data = {
            "physicalData": [
                {
                    "name": name,
                    "mobile": phone,
                    "physicalNumber": checkId,
                    "IDNumber": idcard,
                    # "batchName": time.strftime('%Y.%m.%d%H:%M:%S ', time.localtime(time.time())) + 'WLT上传批次',
                    "batchName": time.strftime('%Y-%m-%d') + "wlt测试批次",
                    "physicalExaminationTime": time.strftime('%Y-%m-%d %H:%M:%S ', time.localtime(time.time())),
                    "doctor": "wlt",
                    "advice": "1. 血压正常高值\r\n建议：复查血压，在平静的情况下，非同日二次血压≥140/90mmhg为高血压。必要时行动态血压检查，心血管内科随访。\r\n生活中应戒烟，限盐（6g/日），控制体重，严格控制饮酒量，并积极参加体育锻炼，保持心理健康等。\r\n2. 卡式幽门螺旋菌检查:阳性(++)\r\n建议进行治疗并定期观察，一般采用药物三联药物治疗，配合螺旋藻类产品修复。\r\n3. 彩超:双侧乳腺增生 红外乳腺检查:双侧乳腺小叶增生(轻度)\r\n是乳腺实质的良性增生，多为生理性，建议：\r\n(1)定期６－１２个月复查乳腺影像及每个月自检乳腺。\r\n(2)必要时到乳腺科进一步诊治。\r\n(3)低脂饮食，避免服用含激素的保健品。\r\n(4)保持愉快心情。\r\n4. 慢性宫颈炎(宫颈脱落细胞学II级良性)\r\n建议：定期复查，必要时妇科诊治。\r\n",
                    "sectionConclusion": [
                        {
                            "conclusion": "(1)血常规五分类：平均血红蛋白浓度(MCHC)：317【g/L】↓；红细胞分布宽度(RDW-SD)：49.4【%CV】↑；平均血小板体积(MPV)：13【fL】↑；大血小板比率(P-LCR)：45.7【%】↑；血小板压积(PCT)：0.14【%】↓；平均红细胞体积(MCV)：101【FL】↑\r\n(2)血脂四项：低密度脂蛋白胆固醇(LDL-C)：1.52【mmol/L】↓\r\n(3)尿常规11项+镜检：镜检管型：0【个/HP】\r\n(4)阴道分泌物涂片：清洁度：II\r\n",
                            "sectionName": "实验室检查"
                        },
                        {
                            "conclusion": "十二导联心电图:①窦性心律②正常心电图",
                            "sectionName": "心电图检查"
                        },
                        {
                            "conclusion": "(1)检查未见异常\r\n(2)剖腹产术后12年（自愿）",
                            "sectionName": "妇科"
                        },
                        {
                            "conclusion": "肝脏、胆囊、胰腺、脾脏、双肾:未见异常\r\n",
                            "sectionName": "上腹B超"
                        },
                        {
                            "conclusion": "甲状腺:未见异常\r\n",
                            "sectionName": "甲状腺彩超"
                        },
                        {
                            "conclusion": "(1)身高:165cm\r\n(2)体重:54Kg\r\n(3)收缩压:113mmHg\r\n(4)舒张压:81mmHg\r\n(5)血压结论:血压正常高值\r\n(6)体重指数:19.83,体重正常\r\n",
                            "sectionName": "一般检查"
                        },
                        {
                            "conclusion": "双侧乳腺小叶增生(轻度)，建议进一步检查。",
                            "sectionName": "红外乳腺检查"
                        },
                        {
                            "conclusion": "胸透:两肺心膈未见异常",
                            "sectionName": "胸透检查"
                        },
                        {
                            "conclusion": "(1)子宫、附件、膀胱:未见异常\r\n(2)输尿管:双侧输尿管无扩张\r\n",
                            "sectionName": "下腹B超"
                        },
                        {
                            "conclusion": "乳腺彩超:双侧乳腺增生\r\n",
                            "sectionName": "乳腺彩超"
                        },
                        {
                            "conclusion": "卡式幽门螺旋菌检查:阳性(++)605",
                            "sectionName": "卡式幽门螺杆菌"
                        },
                        {
                            "conclusion": "宫颈脱落细胞学检查:II级,慢性宫颈炎,细胞良性反应性改变",
                            "sectionName": "病理科"
                        }]
                    ,
                    "physicalItem": [{
                        "sectionName": "一般检查",
                        "itemID": "202",
                        "itemName": "一般检查",
                        "indicatorID": "5528",
                        "unit": "cm",
                        "indicatorName": "身高",
                        "indicatorValue": "165"
                    }, {
                        "sectionName": "一般检查",
                        "itemID": "202",
                        "itemName": "一般检查",
                        "indicatorID": "102",
                        "unit": "Kg",
                        "indicatorName": "体重",
                        "indicatorValue": "63"
                    }, {
                        "sectionName": "一般检查",
                        "itemID": "202",
                        "itemName": "一般检查",
                        "indicatorID": "104",
                        "unit": "mmHg",
                        "indicatorName": "舒张压",
                        "indicatorValue": "96"
                    }, {
                        "sectionName": "一般检查",
                        "itemID": "202",
                        "itemName": "一般检查",
                        "indicatorID": "103",
                        "unit": "mmHg",
                        "indicatorName": "收缩压",
                        "indicatorValue": "169"
                    }, {
                        "sectionName": "一般检查",
                        "itemID": "202",
                        "itemName": "一般检查",
                        "indicatorID": "1",
                        "indicatorName": "体重指数",
                        "indicatorValue": "23.1"
                    }, {
                        "sectionName": "甲状腺彩超",
                        "itemID": "2577",
                        "itemName": "甲状腺彩超",
                        "indicatorID": "5395",
                        "indicatorName": "甲状腺",
                        "indicatorValue": "甲状腺双叶及峡部大小正常，包膜光滑，于左叶探及一囊实性结节，"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4125",
                        "itemName": "阴道分泌物涂片",
                        "indicatorID": "6654",
                        "ref": "阴性",
                        "indicatorName": "滴虫",
                        "indicatorValue": "-"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4125",
                        "itemName": "阴道分泌物涂片",
                        "indicatorID": "6101",
                        "ref": "0-0",
                        "unit": "个/LP",
                        "indicatorName": "红细胞",
                        "indicatorValue": "0"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4125",
                        "itemName": "阴道分泌物涂片",
                        "indicatorID": "7222",
                        "ref": "阴性",
                        "indicatorName": "霉菌",
                        "indicatorValue": "-"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4125",
                        "itemName": "阴道分泌物涂片",
                        "indicatorID": "6656",
                        "ref": "Ⅰ-Ⅱ",
                        "unit": "°",
                        "indicatorName": "清洁度",
                        "indicatorValue": "II"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4125",
                        "itemName": "阴道分泌物涂片",
                        "indicatorID": "5182",
                        "ref": "0-0",
                        "unit": "个/LP",
                        "indicatorName": "白细胞",
                        "indicatorValue": "+"
                    }, {
                        "sectionName": "乳腺彩超",
                        "itemID": "2576",
                        "itemName": "乳腺彩超(双侧)",
                        "indicatorID": "207",
                        "indicatorName": "乳腺彩超",
                        "indicatorValue": "双侧乳房探查：双侧乳腺腺体不厚，回声稍增强，分布欠均匀，乳腺"
                    }, {
                        "sectionName": "放射检查",
                        "itemID": "4326",
                        "itemName": "DR胸部正位片",
                        "indicatorID": "238",
                        "indicatorName": "胸部正位片",
                        "indicatorValue": "两肺纹理清晰，肺内未见明显实质性病变；两肺门影未见明显增大，"
                    }, {
                        "sectionName": "心电图检查",
                        "itemID": "4642",
                        "itemName": "心电图新",
                        "indicatorID": "6814",
                        "indicatorName": "十二导联心电图",
                        "indicatorValue": "①窦性心律②T波:V5.V6低平"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "1790",
                        "itemName": "尿常规11项+镜检",
                        "indicatorID": "5174",
                        "ref": "阴性",
                        "unit": "cell/μl",
                        "indicatorName": "白细胞(LEU)",
                        "indicatorValue": "-"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "1790",
                        "itemName": "尿常规11项+镜检",
                        "indicatorID": "5175",
                        "ref": "阴性",
                        "unit": "mmol/L",
                        "indicatorName": "酮体(KET)",
                        "indicatorValue": "-"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "1790",
                        "itemName": "尿常规11项+镜检",
                        "indicatorID": "5295",
                        "ref": "0-5",
                        "unit": "个/HP",
                        "indicatorName": "镜检白细胞",
                        "indicatorValue": "0"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "1790",
                        "itemName": "尿常规11项+镜检",
                        "indicatorID": "6848",
                        "ref": "清",
                        "indicatorName": "清晰度",
                        "indicatorValue": "清晰"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "1790",
                        "itemName": "尿常规11项+镜检",
                        "indicatorID": "5176",
                        "ref": "阴性",
                        "unit": "μmol/L",
                        "indicatorName": "胆红素(BIL)",
                        "indicatorValue": "-"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "1790",
                        "itemName": "尿常规11项+镜检",
                        "indicatorID": "5178",
                        "ref": "阴性",
                        "unit": "μmol/L",
                        "indicatorName": "亚硝酸盐(NIT)",
                        "indicatorValue": "-"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "1790",
                        "itemName": "尿常规11项+镜检",
                        "indicatorID": "7050",
                        "ref": "阴性",
                        "unit": "mmol/L",
                        "indicatorName": "维生素C",
                        "indicatorValue": "-"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "1790",
                        "itemName": "尿常规11项+镜检",
                        "indicatorID": "5296",
                        "ref": "0-2",
                        "unit": "个/HP",
                        "indicatorName": "镜检红细胞",
                        "indicatorValue": "0"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "1790",
                        "itemName": "尿常规11项+镜检",
                        "indicatorID": "7057",
                        "ref": "5.5-7",
                        "indicatorName": "PH(干化学)",
                        "indicatorValue": "6.5"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "1790",
                        "itemName": "尿常规11项+镜检",
                        "indicatorID": "5292",
                        "ref": "阴性",
                        "unit": "mmol/L",
                        "indicatorName": "尿糖(GLU)",
                        "indicatorValue": "-"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "1790",
                        "itemName": "尿常规11项+镜检",
                        "indicatorID": "7049",
                        "ref": "阴性",
                        "unit": "Cell/μL",
                        "indicatorName": "尿隐血(BLD)",
                        "indicatorValue": "-"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "1790",
                        "itemName": "尿常规11项+镜检",
                        "indicatorID": "5177",
                        "ref": "阴性",
                        "unit": "μmol/L",
                        "indicatorName": "尿胆原(UBG)",
                        "indicatorValue": "- 3.2"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "1790",
                        "itemName": "尿常规11项+镜检",
                        "indicatorID": "5594",
                        "ref": "0-0",
                        "indicatorName": "颜色",
                        "indicatorValue": "淡黄色"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "1790",
                        "itemName": "尿常规11项+镜检",
                        "indicatorID": "5169",
                        "ref": "阴性",
                        "indicatorName": "尿蛋白(PRO)",
                        "indicatorValue": "-"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "1790",
                        "itemName": "尿常规11项+镜检",
                        "indicatorID": "5299",
                        "ref": "0-0",
                        "unit": "个/HP",
                        "indicatorName": "镜检管型",
                        "indicatorValue": "0"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "1790",
                        "itemName": "尿常规11项+镜检",
                        "indicatorID": "5172",
                        "ref": "1.01-1.025",
                        "indicatorName": "比重(SG)",
                        "indicatorValue": "1.015"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "3030",
                        "itemName": "心肌酶五项",
                        "indicatorID": "7007",
                        "ref": "0-24",
                        "unit": "ng/ml",
                        "indicatorName": "肌酸激酶同工酶MB",
                        "indicatorValue": "16.6"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "3030",
                        "itemName": "心肌酶五项",
                        "indicatorID": "6683",
                        "ref": "100-285",
                        "unit": "U/L",
                        "indicatorName": "乳酸脱氢酶(LDH)",
                        "indicatorValue": "153"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "3030",
                        "itemName": "心肌酶五项",
                        "indicatorID": "6695",
                        "ref": "40-167",
                        "unit": "U/L",
                        "indicatorName": "肌酸激酶(CK)",
                        "indicatorValue": "64"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "3030",
                        "itemName": "心肌酶五项",
                        "indicatorID": "7078",
                        "ref": "0-40",
                        "unit": "U/L",
                        "indicatorName": "谷草转氨酶(AST)",
                        "indicatorValue": "18"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "3030",
                        "itemName": "心肌酶五项",
                        "indicatorID": "6249",
                        "ref": "70-230",
                        "unit": "U/L",
                        "indicatorName": "α-羟丁酸脱氢酶(HBDH)",
                        "indicatorValue": "126"
                    }, {
                        "sectionName": "一般检查",
                        "itemID": "202",
                        "itemName": "一般检查",
                        "indicatorID": "2",
                        "unit": " ",
                        "indicatorName": "血压结论",
                        "indicatorValue": "高血压"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4512",
                        "itemName": "血脂六项",
                        "indicatorID": "5118",
                        "ref": "0.4-1.86",
                        "unit": "mmol/L",
                        "indicatorName": "甘油三酯(TG)",
                        "indicatorValue": "1.85"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4512",
                        "itemName": "血脂六项",
                        "indicatorID": "5117",
                        "ref": "3.1-6.19",
                        "unit": "mmol/L",
                        "indicatorName": "总胆固醇(CHO)",
                        "indicatorValue": "6.21"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4512",
                        "itemName": "血脂六项",
                        "indicatorID": "5539",
                        "ref": "0.6-1.14",
                        "unit": "g/L",
                        "indicatorName": "载脂蛋白B(ApoB)",
                        "indicatorValue": "1.40"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4512",
                        "itemName": "血脂六项",
                        "indicatorID": "5538",
                        "ref": "1-1.6",
                        "unit": "g/L",
                        "indicatorName": "载脂蛋白A1(ApoA1)",
                        "indicatorValue": "1.37"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4512",
                        "itemName": "血脂六项",
                        "indicatorID": "5119",
                        "ref": "1.2-1.68",
                        "unit": "mmol/L",
                        "indicatorName": "高密度脂蛋白胆固醇(HDL-C)",
                        "indicatorValue": "1.43"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4512",
                        "itemName": "血脂六项",
                        "indicatorID": "5120",
                        "ref": "2.07-3.1",
                        "unit": "mmol/L",
                        "indicatorName": "低密度脂蛋白胆固醇(LDL-C)",
                        "indicatorValue": "4.17"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4686",
                        "itemName": "胃功能四项",
                        "indicatorID": "7526",
                        "ref": "3-11",
                        "indicatorName": "胃蛋白酶原II",
                        "indicatorValue": "5.01"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4686",
                        "itemName": "胃功能四项",
                        "indicatorID": "7569",
                        "ref": "1-7",
                        "indicatorName": "胃泌素",
                        "indicatorValue": "1.17"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4686",
                        "itemName": "胃功能四项",
                        "indicatorID": "7525",
                        "ref": "70-165",
                        "indicatorName": "胃蛋白酶原I",
                        "indicatorValue": "150.76"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4686",
                        "itemName": "胃功能四项",
                        "indicatorID": "7527",
                        "ref": "≥7",
                        "indicatorName": "胃蛋白酶原比值",
                        "indicatorValue": "30.09"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4286",
                        "itemName": "肾功三项",
                        "indicatorID": "5114",
                        "ref": "155-357",
                        "unit": "μmol/L",
                        "indicatorName": "尿酸(UA)",
                        "indicatorValue": "261"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4286",
                        "itemName": "肾功三项",
                        "indicatorID": "5113",
                        "ref": "40-100",
                        "unit": "μmol/L",
                        "indicatorName": "肌酐(Cr)",
                        "indicatorValue": "50"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4286",
                        "itemName": "肾功三项",
                        "indicatorID": "5112",
                        "ref": "2.86-8.2",
                        "unit": "mmol/L",
                        "indicatorName": "尿素氮(BUN)",
                        "indicatorValue": "5.7"
                    }, {
                        "sectionName": "眼科",
                        "itemID": "3272",
                        "itemName": "眼科检查",
                        "indicatorID": "6772",
                        "indicatorName": "巩膜",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "眼科",
                        "itemID": "3272",
                        "itemName": "眼科检查",
                        "indicatorID": "6759",
                        "indicatorName": "泪器",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "眼科",
                        "itemID": "3272",
                        "itemName": "眼科检查",
                        "indicatorID": "6732",
                        "indicatorName": "眼球运动",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "眼科",
                        "itemID": "3272",
                        "itemName": "眼科检查",
                        "indicatorID": "5513",
                        "indicatorName": "视力检查",
                        "indicatorValue": "视力:右1.0;左0.6。"
                    }, {
                        "sectionName": "眼科",
                        "itemID": "3272",
                        "itemName": "眼科检查",
                        "indicatorID": "145",
                        "indicatorName": "辨色力",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "眼科",
                        "itemID": "3272",
                        "itemName": "眼科检查",
                        "indicatorID": "6733",
                        "indicatorName": "结膜",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "眼科",
                        "itemID": "3272",
                        "itemName": "眼科检查",
                        "indicatorID": "147",
                        "indicatorName": "眼睑",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "骨密度检查",
                        "itemID": "1980",
                        "itemName": "骨密度测定",
                        "indicatorID": "422",
                        "indicatorName": "综合评估",
                        "indicatorValue": "骨量正常"
                    }, {
                        "sectionName": "骨密度检查",
                        "itemID": "1980",
                        "itemName": "骨密度测定",
                        "indicatorID": "6996",
                        "unit": "dB/Mhz",
                        "indicatorName": "BUA",
                        "indicatorValue": "29.1"
                    }, {
                        "sectionName": "骨密度检查",
                        "itemID": "1980",
                        "itemName": "骨密度测定",
                        "indicatorID": "6995",
                        "indicatorName": "Z值",
                        "indicatorValue": "2.27"
                    }, {
                        "sectionName": "骨密度检查",
                        "itemID": "1980",
                        "itemName": "骨密度测定",
                        "indicatorID": "6994",
                        "indicatorName": "T值",
                        "indicatorValue": "-0.74"
                    }, {
                        "sectionName": "骨密度检查",
                        "itemID": "1980",
                        "itemName": "骨密度测定",
                        "indicatorID": "6992",
                        "indicatorName": "检查部位",
                        "indicatorValue": "右脚"
                    }, {
                        "sectionName": "病理科",
                        "itemID": "4291",
                        "itemName": "液基细胞学检查(女)",
                        "indicatorID": "7368",
                        "indicatorName": "宫颈TCT炎症程度",
                        "indicatorValue": "轻度"
                    }, {
                        "sectionName": "妇科",
                        "itemID": "207",
                        "itemName": "妇科检查",
                        "indicatorID": "3980",
                        "indicatorName": "月经史",
                        "indicatorValue": "自诉不详"
                    }, {
                        "sectionName": "妇科",
                        "itemID": "207",
                        "itemName": "妇科检查",
                        "indicatorID": "177",
                        "indicatorName": "附件",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "妇科",
                        "itemID": "207",
                        "itemName": "妇科检查",
                        "indicatorID": "173",
                        "indicatorName": "分泌物",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "妇科",
                        "itemID": "207",
                        "itemName": "妇科检查",
                        "indicatorID": "5535",
                        "indicatorName": "手术史",
                        "indicatorValue": "无"
                    }, {
                        "sectionName": "妇科",
                        "itemID": "207",
                        "itemName": "妇科检查",
                        "indicatorID": "172",
                        "indicatorName": "阴道",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "颈部血管彩超",
                        "itemID": "4327",
                        "itemName": "颈部血管彩超",
                        "indicatorID": "7183",
                        "indicatorName": "颈部血管彩超",
                        "indicatorValue": "双侧颈动脉走行自然，双侧颈总、颈内及颈外动脉未见狭窄及扩张，"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4359",
                        "itemName": "风湿三项",
                        "indicatorID": "6636",
                        "ref": "<20",
                        "unit": "IU/mL",
                        "indicatorName": "类风湿因子(RF)",
                        "indicatorValue": "<20"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4359",
                        "itemName": "风湿三项",
                        "indicatorID": "6637",
                        "ref": "阴性",
                        "unit": "mg/L",
                        "indicatorName": "C反应蛋白(CRP)",
                        "indicatorValue": "阴性"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4359",
                        "itemName": "风湿三项",
                        "indicatorID": "7095",
                        "ref": "0-200",
                        "indicatorName": "抗链球菌溶血素“O”",
                        "indicatorValue": "<200"
                    }, {
                        "sectionName": "妇科",
                        "itemID": "207",
                        "itemName": "妇科检查",
                        "indicatorID": "176",
                        "indicatorName": "宫体",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "妇科",
                        "itemID": "207",
                        "itemName": "妇科检查",
                        "indicatorID": "174",
                        "indicatorName": "宫颈",
                        "indicatorValue": "宫颈组织充血、水肿"
                    }, {
                        "sectionName": "妇科",
                        "itemID": "207",
                        "itemName": "妇科检查",
                        "indicatorID": "5435",
                        "indicatorName": "婚姻史",
                        "indicatorValue": "已婚"
                    }, {
                        "sectionName": "妇科",
                        "itemID": "207",
                        "itemName": "妇科检查",
                        "indicatorID": "171",
                        "indicatorName": "外阴",
                        "indicatorValue": "未见明显异常"
                    }, {
                        "sectionName": "耳鼻喉科",
                        "itemID": "1911",
                        "itemName": "耳鼻喉科检查",
                        "indicatorID": "5427",
                        "indicatorName": "中内耳/乳突",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "耳鼻喉科",
                        "itemID": "1911",
                        "itemName": "耳鼻喉科检查",
                        "indicatorID": "5430",
                        "indicatorName": "咽",
                        "indicatorValue": "咽部粘膜慢性充血　侧索肥厚　后壁淋巴滤泡增生。"
                    }, {
                        "sectionName": "耳鼻喉科",
                        "itemID": "1911",
                        "itemName": "耳鼻喉科检查",
                        "indicatorID": "5734",
                        "indicatorName": "其它",
                        "indicatorValue": "无"
                    }, {
                        "sectionName": "耳鼻喉科",
                        "itemID": "1911",
                        "itemName": "耳鼻喉科检查",
                        "indicatorID": "6874",
                        "indicatorName": "鼻中隔",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "耳鼻喉科",
                        "itemID": "1911",
                        "itemName": "耳鼻喉科检查",
                        "indicatorID": "6875",
                        "indicatorName": "鼻前庭",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "耳鼻喉科",
                        "itemID": "1911",
                        "itemName": "耳鼻喉科检查",
                        "indicatorID": "6876",
                        "indicatorName": "外鼻",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "耳鼻喉科",
                        "itemID": "1911",
                        "itemName": "耳鼻喉科检查",
                        "indicatorID": "6871",
                        "indicatorName": "耳廓",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "耳鼻喉科",
                        "itemID": "1911",
                        "itemName": "耳鼻喉科检查",
                        "indicatorID": "6872",
                        "indicatorName": "耳道",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "耳鼻喉科",
                        "itemID": "1911",
                        "itemName": "耳鼻喉科检查",
                        "indicatorID": "5431",
                        "indicatorName": "喉",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "耳鼻喉科",
                        "itemID": "1911",
                        "itemName": "耳鼻喉科检查",
                        "indicatorID": "5429",
                        "indicatorName": "鼻腔、鼻窦",
                        "indicatorValue": "鼻粘膜、下鼻甲、中鼻甲、灰白色　苍白　暗红色　水肿　黏液涕　"
                    }, {
                        "sectionName": "CT检查",
                        "itemID": "2835",
                        "itemName": "颅脑CT(平扫)",
                        "indicatorID": "6518",
                        "indicatorName": "颅脑CT",
                        "indicatorValue": "　颅内脑实质未见异常密度影，诸脑室、脑池未见明显扩张、加深，"
                    }, {
                        "sectionName": "内科",
                        "itemID": "3228",
                        "itemName": "内科检查",
                        "indicatorID": "6720",
                        "indicatorName": "呼吸音",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "内科",
                        "itemID": "3228",
                        "itemName": "内科检查",
                        "indicatorID": "114",
                        "indicatorName": "胸廓",
                        "indicatorValue": "无畸形"
                    }, {
                        "sectionName": "内科",
                        "itemID": "3228",
                        "itemName": "内科检查",
                        "indicatorID": "110",
                        "indicatorName": "杂音",
                        "indicatorValue": "无杂音"
                    }, {
                        "sectionName": "内科",
                        "itemID": "3228",
                        "itemName": "内科检查",
                        "indicatorID": "5549",
                        "indicatorName": "过敏史",
                        "indicatorValue": "无特殊"
                    }, {
                        "sectionName": "内科",
                        "itemID": "3228",
                        "itemName": "内科检查",
                        "indicatorID": "5446",
                        "indicatorName": "腹部",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "内科",
                        "itemID": "3228",
                        "itemName": "内科检查",
                        "indicatorID": "124",
                        "indicatorName": "脾脏",
                        "indicatorValue": "肋下未触及"
                    }, {
                        "sectionName": "内科",
                        "itemID": "3228",
                        "itemName": "内科检查",
                        "indicatorID": "6675",
                        "indicatorName": "神经系统",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "内科",
                        "itemID": "3228",
                        "itemName": "内科检查",
                        "indicatorID": "5447",
                        "indicatorName": "既往史",
                        "indicatorValue": "高血压病史1年　(间断服药)"
                    }, {
                        "sectionName": "内科",
                        "itemID": "3228",
                        "itemName": "内科检查",
                        "indicatorID": "5550",
                        "unit": "年",
                        "indicatorName": "饮酒史",
                        "indicatorValue": "偶尔饮酒"
                    }, {
                        "sectionName": "内科",
                        "itemID": "3228",
                        "itemName": "内科检查",
                        "indicatorID": "5526",
                        "indicatorName": "心音",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "内科",
                        "itemID": "3228",
                        "itemName": "内科检查",
                        "indicatorID": "6677",
                        "indicatorName": "肾",
                        "indicatorValue": "未触及"
                    }, {
                        "sectionName": "内科",
                        "itemID": "3228",
                        "itemName": "内科检查",
                        "indicatorID": "6713",
                        "indicatorName": "胆囊",
                        "indicatorValue": "无压痛"
                    }, {
                        "sectionName": "内科",
                        "itemID": "3228",
                        "itemName": "内科检查",
                        "indicatorID": "5445",
                        "indicatorName": "肝脏",
                        "indicatorValue": "肋下未触及"
                    }, {
                        "sectionName": "内科",
                        "itemID": "3228",
                        "itemName": "内科检查",
                        "indicatorID": "5542",
                        "indicatorName": "家族史",
                        "indicatorValue": "无家族遗传病史"
                    }, {
                        "sectionName": "内科",
                        "itemID": "3228",
                        "itemName": "内科检查",
                        "indicatorID": "5548",
                        "indicatorName": "吸烟史",
                        "indicatorValue": "无嗜烟"
                    }, {
                        "sectionName": "内科",
                        "itemID": "3228",
                        "itemName": "内科检查",
                        "indicatorID": "5529",
                        "unit": "次／分",
                        "indicatorName": "心率",
                        "indicatorValue": "62　次/分"
                    }, {
                        "sectionName": "内科",
                        "itemID": "3228",
                        "itemName": "内科检查",
                        "indicatorID": "109",
                        "indicatorName": "心律",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "3671",
                        "itemName": "血糖测定",
                        "indicatorID": "7221",
                        "ref": "3.9-6.1",
                        "unit": "mmol/L",
                        "indicatorName": "葡萄糖(GLU)",
                        "indicatorValue": "6.7"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "5210",
                        "ref": "0.38--0.47",
                        "indicatorName": "红细胞压积（L/L）",
                        "indicatorValue": "0.44"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "5209",
                        "ref": "1.18-1.74",
                        "indicatorName": "血浆粘度值(mpas):200",
                        "indicatorValue": "1.88"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "7696",
                        "ref": "3.59-11.44",
                        "indicatorName": "全血中切还原粘度(50/s)",
                        "indicatorValue": "5.01"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "7709",
                        "ref": "0.05-0.09",
                        "indicatorName": "卡森应力",
                        "indicatorValue": "0.07"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "7702",
                        "ref": "6.23-21.33",
                        "indicatorName": "全血低切还原粘度(3/s)",
                        "indicatorValue": "10.41"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "7704",
                        "ref": "3.64-4.65",
                        "indicatorName": "红细胞计数",
                        "indicatorValue": "4.47"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "5216",
                        "ref": "1.38-2.74",
                        "indicatorName": "红细胞聚集指数",
                        "indicatorValue": "1.93"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "5217",
                        "ref": "2.51-9.47",
                        "indicatorName": "红细胞刚性指数",
                        "indicatorValue": "4.32"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "7697",
                        "ref": "9.35-32.06",
                        "indicatorName": "全血低切还原粘度(1/s)",
                        "indicatorValue": "14.49"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "7707",
                        "ref": "39.9-63.84",
                        "indicatorName": "低切流阻",
                        "indicatorValue": "58.51"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "7706",
                        "ref": "29.34-39.82",
                        "indicatorName": "高切流阻",
                        "indicatorValue": "38.21"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "6697",
                        "ref": "2.23-4.6",
                        "indicatorName": "全血高切相对粘度",
                        "indicatorValue": "2.91"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "6296",
                        "ref": "4.61-6.04",
                        "unit": "mpa.s",
                        "indicatorName": "全血粘度:中切|50(1/S)",
                        "indicatorValue": "6.05"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "7047",
                        "ref": "14.7-19.95",
                        "indicatorName": "红细胞电泳时间",
                        "indicatorValue": "19.15"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "5218",
                        "ref": "0.38-1.11",
                        "indicatorName": "红细胞变形指数(TK)",
                        "indicatorValue": "0.79"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "7708",
                        "ref": "35.63-47.5",
                        "indicatorName": "中切流阻",
                        "indicatorValue": "45.48"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "7703",
                        "ref": "0.34-1.69",
                        "indicatorName": "红细胞聚集系数",
                        "indicatorValue": "0.93"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "7046",
                        "ref": "2.68-3.66",
                        "indicatorName": "卡森粘度",
                        "indicatorValue": "3.64"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "5214",
                        "ref": "2.85-10.17",
                        "indicatorName": "全血高切还原粘度(200/s)",
                        "indicatorValue": "4.32"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "7698",
                        "ref": "3.11-10.26",
                        "indicatorName": "全血高切还原粘度(150/s)",
                        "indicatorValue": "4.36"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "7700",
                        "ref": "5.3-16.57",
                        "indicatorName": "全血低切还原粘度(10/s)",
                        "indicatorValue": "7.35"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "7699",
                        "ref": "4.01-12.81",
                        "indicatorName": "全血中切还原粘度(30/s)",
                        "indicatorValue": "5.57"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "7705",
                        "ref": "0.23-4.45",
                        "indicatorName": "红细胞内粘度",
                        "indicatorValue": "3.4"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "6297",
                        "ref": "9.5-15.2",
                        "unit": "mpa.s",
                        "indicatorName": "全血粘度:低切|1(1/S)",
                        "indicatorValue": "13.93"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "7701",
                        "ref": "6.25-20.13",
                        "indicatorName": "全血低切还原粘度(5/s)",
                        "indicatorValue": "8.95"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "6698",
                        "ref": "5.05-12.26",
                        "indicatorName": "全血低切相对粘度",
                        "indicatorValue": "7.41"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4299",
                        "itemName": "血流变",
                        "indicatorID": "5461",
                        "ref": "4.2-5.7",
                        "unit": "mPa.s",
                        "indicatorName": "全血粘度:高切|200(1/S)",
                        "indicatorValue": "5.47"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4323",
                        "itemName": "糖化血红蛋白",
                        "indicatorID": "6648",
                        "ref": "4.3-6",
                        "unit": "g/L",
                        "indicatorName": "糖化血红蛋白",
                        "indicatorValue": "5.8"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "3957",
                        "itemName": "血沉",
                        "indicatorID": "5211",
                        "ref": "0-20",
                        "unit": "mm/h",
                        "indicatorName": "血沉(ESR)",
                        "indicatorValue": "7"
                    }, {
                        "sectionName": "眼科",
                        "itemID": "4136",
                        "itemName": "眼底、裂隙灯等检查",
                        "indicatorID": "5530",
                        "indicatorName": "角膜",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "眼科",
                        "itemID": "4136",
                        "itemName": "眼底、裂隙灯等检查",
                        "indicatorID": "5531",
                        "indicatorName": "虹膜睫状体",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "眼科",
                        "itemID": "4136",
                        "itemName": "眼底、裂隙灯等检查",
                        "indicatorID": "6736",
                        "indicatorName": "瞳孔",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "眼科",
                        "itemID": "4136",
                        "itemName": "眼底、裂隙灯等检查",
                        "indicatorID": "6734",
                        "indicatorName": "眼底",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "眼科",
                        "itemID": "4136",
                        "itemName": "眼底、裂隙灯等检查",
                        "indicatorID": "5532",
                        "indicatorName": "晶状体",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "眼科",
                        "itemID": "4136",
                        "itemName": "眼底、裂隙灯等检查",
                        "indicatorID": "6735",
                        "indicatorName": "前房",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "眼科",
                        "itemID": "4136",
                        "itemName": "眼底、裂隙灯等检查",
                        "indicatorID": "5533",
                        "indicatorName": "玻璃体",
                        "indicatorValue": "未见异常"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4203",
                        "itemName": "肝功十一项",
                        "indicatorID": "5490",
                        "ref": "1.7-17",
                        "unit": "μmol/L",
                        "indicatorName": "间接胆红素(IBIL)",
                        "indicatorValue": "6.60"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4203",
                        "itemName": "肝功十一项",
                        "indicatorID": "5101",
                        "ref": "0-40",
                        "unit": "U/L",
                        "indicatorName": "谷丙转氨酶(ALT)",
                        "indicatorValue": "18"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4203",
                        "itemName": "肝功十一项",
                        "indicatorID": "5110",
                        "ref": "40-150",
                        "unit": "U/L",
                        "indicatorName": "碱性磷酸酶(ALP)",
                        "indicatorValue": "76"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4203",
                        "itemName": "肝功十一项",
                        "indicatorID": "5107",
                        "ref": "35-54",
                        "unit": "g/L",
                        "indicatorName": "白蛋白(ALB)",
                        "indicatorValue": "49.3"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4203",
                        "itemName": "肝功十一项",
                        "indicatorID": "5383",
                        "ref": "0-50",
                        "unit": "U/L",
                        "indicatorName": "γ-谷氨酰转肽酶(GGT)",
                        "indicatorValue": "15"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4203",
                        "itemName": "肝功十一项",
                        "indicatorID": "5104",
                        "ref": "3.4-25.4",
                        "unit": "μmol/L",
                        "indicatorName": "总胆红素(TBIL)",
                        "indicatorValue": "8.4"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4203",
                        "itemName": "肝功十一项",
                        "indicatorID": "5106",
                        "ref": "62-85",
                        "unit": "g/L",
                        "indicatorName": "总蛋白(TP)",
                        "indicatorValue": "75.3"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4203",
                        "itemName": "肝功十一项",
                        "indicatorID": "5108",
                        "ref": "20-40",
                        "unit": "g/L",
                        "indicatorName": "球蛋白(GLO)",
                        "indicatorValue": "26.00"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4203",
                        "itemName": "肝功十一项",
                        "indicatorID": "5105",
                        "ref": "0-8",
                        "unit": "μmol/L",
                        "indicatorName": "直接胆红素(DBIL)",
                        "indicatorValue": "1.8"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4203",
                        "itemName": "肝功十一项",
                        "indicatorID": "5109",
                        "ref": "1.4-2.6",
                        "indicatorName": "白球比(A/G)",
                        "indicatorValue": "1.8"
                    }, {
                        "sectionName": "电子阴道镜",
                        "itemID": "4437",
                        "itemName": "阴道镜检查",
                        "indicatorID": "7356",
                        "indicatorName": "宫颈",
                        "indicatorValue": "宫颈肥大"
                    }, {
                        "sectionName": "电子阴道镜",
                        "itemID": "4437",
                        "itemName": "阴道镜检查",
                        "indicatorID": "7355",
                        "indicatorName": "阴道",
                        "indicatorValue": "未见明显异常。"
                    }, {
                        "sectionName": "电子阴道镜",
                        "itemID": "4437",
                        "itemName": "阴道镜检查",
                        "indicatorID": "7354",
                        "indicatorName": "外阴",
                        "indicatorValue": "未见明显异常。"
                    }, {
                        "sectionName": "电子阴道镜",
                        "itemID": "4437",
                        "itemName": "阴道镜检查",
                        "indicatorID": "7357",
                        "indicatorName": "其它",
                        "indicatorValue": "未见明显异常。"
                    }, {
                        "sectionName": "上腹彩超",
                        "itemID": "4238",
                        "itemName": "上腹彩超",
                        "indicatorID": "6022",
                        "indicatorName": "双肾",
                        "indicatorValue": "双肾：大小形态正常，肾实质部回声均匀，集合系统清晰，未见明显"
                    }, {
                        "sectionName": "上腹彩超",
                        "itemID": "4238",
                        "itemName": "上腹彩超",
                        "indicatorID": "6020",
                        "indicatorName": "胰腺",
                        "indicatorValue": "胰腺：大小正常，腺体回声均质，主胰管不扩张，未见明显异常。"
                    }, {
                        "sectionName": "上腹彩超",
                        "itemID": "4238",
                        "itemName": "上腹彩超",
                        "indicatorID": "6019",
                        "indicatorName": "胆囊",
                        "indicatorValue": "胆囊：大小正常，壁光滑，腔内透声好；胆总管无扩张。"
                    }, {
                        "sectionName": "上腹彩超",
                        "itemID": "4238",
                        "itemName": "上腹彩超",
                        "indicatorID": "6021",
                        "indicatorName": "脾脏",
                        "indicatorValue": "脾脏：大小正常，包膜光滑完整，脾内回声均质，脾静脉不宽。"
                    }, {
                        "sectionName": "上腹彩超",
                        "itemID": "4238",
                        "itemName": "上腹彩超",
                        "indicatorID": "6018",
                        "indicatorName": "肝脏",
                        "indicatorValue": "肝脏：大小正常，包膜光滑，静脉清晰，肝左实质内可见囊性暗区，"
                    }, {
                        "sectionName": "动脉硬化检查",
                        "itemID": "1934",
                        "itemName": "动脉硬化检测",
                        "indicatorID": "6816",
                        "indicatorName": "ABI",
                        "indicatorValue": "右1.21　左1.20"
                    }, {
                        "sectionName": "动脉硬化检查",
                        "itemID": "1934",
                        "itemName": "动脉硬化检测",
                        "indicatorID": "6817",
                        "indicatorName": "baPWV",
                        "indicatorValue": "右1573　左1606"
                    }, {
                        "sectionName": "动脉硬化检查",
                        "itemID": "1934",
                        "itemName": "动脉硬化检测",
                        "indicatorID": "6776",
                        "indicatorName": "动脉硬化检测",
                        "indicatorValue": "动脉僵硬度轻度升高"
                    }, {
                        "sectionName": "卡式幽门螺杆菌",
                        "itemID": "4294",
                        "itemName": "卡式幽门螺杆菌检测",
                        "indicatorID": "7156",
                        "indicatorName": "卡式幽门螺旋菌检查",
                        "indicatorValue": "阴性(—)"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4803",
                        "itemName": "血常规五分类",
                        "indicatorID": "5078",
                        "ref": "3.5-5",
                        "unit": "10^12/L",
                        "indicatorName": "红细胞(RBC)",
                        "indicatorValue": "4.75"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4803",
                        "itemName": "血常规五分类",
                        "indicatorID": "5080",
                        "ref": "35.3-51.2",
                        "unit": "%",
                        "indicatorName": "红细胞压积(HCT)",
                        "indicatorValue": "36.70"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4803",
                        "itemName": "血常规五分类",
                        "indicatorID": "6692",
                        "ref": "27.1-32.4",
                        "unit": "pg",
                        "indicatorName": "平均血红蛋白含量(MCH)",
                        "indicatorValue": "23.8"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4803",
                        "itemName": "血常规五分类",
                        "indicatorID": "5086",
                        "ref": "9.2-12",
                        "unit": "fL",
                        "indicatorName": "平均血小板体积(MPV)",
                        "indicatorValue": "10.1"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4803",
                        "itemName": "血常规五分类",
                        "indicatorID": "6039",
                        "ref": "0.2-5.3",
                        "unit": "%",
                        "indicatorName": "嗜酸性粒细胞比率(EOS%)",
                        "indicatorValue": "1.8"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4803",
                        "itemName": "血常规五分类",
                        "indicatorID": "6389",
                        "ref": "113-151",
                        "unit": "g/L",
                        "indicatorName": "血红蛋白(HGB)",
                        "indicatorValue": "113"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4803",
                        "itemName": "血常规五分类",
                        "indicatorID": "6261",
                        "ref": "12.2-14.8",
                        "unit": "%CV",
                        "indicatorName": "红细胞分布宽度%(RDW-CV)",
                        "indicatorValue": "16.70"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4803",
                        "itemName": "血常规五分类",
                        "indicatorID": "7056",
                        "ref": "0.18-0.39",
                        "unit": "%",
                        "indicatorName": "血小板压积(PCT)",
                        "indicatorValue": "0.44"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4803",
                        "itemName": "血常规五分类",
                        "indicatorID": "7220",
                        "ref": "86.7-102.3",
                        "unit": "FL",
                        "flag": "↓",
                        "indicatorName": "平均红细胞体积(MCV)",
                        "indicatorValue": "77.3"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4803",
                        "itemName": "血常规五分类",
                        "indicatorID": "6260",
                        "ref": "42.9-74.3",
                        "unit": "%",
                        "flag": "↓",
                        "indicatorName": "中性粒细胞比率(NEU%)",
                        "indicatorValue": "59.70"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4803",
                        "itemName": "血常规五分类",
                        "indicatorID": "5083",
                        "ref": "318-347",
                        "unit": "g/L",
                        "flag": "↓",
                        "indicatorName": "平均血红蛋白浓度(MCHC)",
                        "indicatorValue": "308"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4803",
                        "itemName": "血常规五分类",
                        "indicatorID": "5090",
                        "ref": "1.26-3.35",
                        "unit": "10^9/L",
                        "flag": "↓",
                        "indicatorName": "淋巴细胞绝对值(LYM#)",
                        "indicatorValue": "2.12"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4803",
                        "itemName": "血常规五分类",
                        "indicatorID": "5737",
                        "ref": "0.01-0.4",
                        "unit": "10^9/L",
                        "flag": "↓",
                        "indicatorName": "嗜酸性粒细胞绝对值(EOS#)",
                        "indicatorValue": "0.12"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4803",
                        "itemName": "血常规五分类",
                        "indicatorID": "5089",
                        "ref": "18.3-45.7",
                        "unit": "%",
                        "flag": "↓",
                        "indicatorName": "淋巴细胞比率(LYM%)",
                        "indicatorValue": "31.80"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4803",
                        "itemName": "血常规五分类",
                        "indicatorID": "6040",
                        "ref": "0.1-1",
                        "unit": "%",
                        "flag": "↑",
                        "indicatorName": "嗜碱性粒细胞比率(BAS%)",
                        "indicatorValue": "0.60"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4803",
                        "itemName": "血常规五分类",
                        "indicatorID": "5085",
                        "ref": "100-300",
                        "unit": "10^9/L",
                        "flag": "↑",
                        "indicatorName": "血小板(PLT)",
                        "indicatorValue": "431"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4803",
                        "itemName": "血常规五分类",
                        "indicatorID": "5088",
                        "ref": "9.9-15.4",
                        "unit": "%",
                        "flag": "↑",
                        "indicatorName": "血小板分布宽度(PDW)",
                        "indicatorValue": "10.6"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4803",
                        "itemName": "血常规五分类",
                        "indicatorID": "6038",
                        "ref": "0.01-0.07",
                        "unit": "10^9/L",
                        "flag": "↑",
                        "indicatorName": "嗜碱性粒细胞绝对值(BAS#)",
                        "indicatorValue": "0.04"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4803",
                        "itemName": "血常规五分类",
                        "indicatorID": "5094",
                        "ref": "2.1-8.89",
                        "unit": "10^9/L",
                        "flag": "↑",
                        "indicatorName": "中性粒细胞绝对值(NEU#)",
                        "indicatorValue": "3.98"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4803",
                        "itemName": "血常规五分类",
                        "indicatorID": "5084",
                        "ref": "38.2-49.2",
                        "unit": "%CV",
                        "flag": "↑",
                        "indicatorName": "红细胞分布宽度(RDW-SD)",
                        "indicatorValue": "45.30"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4803",
                        "itemName": "血常规五分类",
                        "indicatorID": "5077",
                        "ref": "4-10",
                        "unit": "10^9/L",
                        "flag": "↑",
                        "indicatorName": "白细胞(WBC)",
                        "indicatorValue": "6.67"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4803",
                        "itemName": "血常规五分类",
                        "indicatorID": "6041",
                        "ref": "17.5-42.3",
                        "unit": "%",
                        "flag": "↑",
                        "indicatorName": "大血小板比率(P-LCR)",
                        "indicatorValue": "24.50"
                    }, {
                        "sectionName": "实验室检查",
                        "itemID": "4803",
                        "itemName": "血常规五分类",
                        "indicatorID": "6259",
                        "ref": "0.25-0.84",
                        "unit": "10^9/L",
                        "flag": "↑",
                        "indicatorName": "单核细胞绝对值(MON#)",
                        "indicatorValue": "0.41"
                    }],
                    "fatalAbnormal": [
                        {
                            "conclustion": "血压正常高值"
                        },
                        {
                            "conclustion": "双侧乳腺小叶增生"
                        },
                        {
                            "conclustion": "乳腺增生"
                        },
                        {
                            "conclustion": "卡式幽门螺杆菌阳性(++)"
                        },
                        {
                            "conclustion": "清洁度异常"
                        },
                        {
                            "conclustion": "慢性宫颈炎"
                        },
                    ],
                },
            ]
        }
        response = requests.post(url, data=json.dumps(data), headers=self.headers, verify=False)
        print(response.text)

    def main():
        start = time.time()
        token = get_token()
        a = answer_question()
        data_dict = uacadduser()
        cardId = data_dict['cardId']
        # list.append(cardId)
        print('cardId:%s' % cardId)
        name = data_dict['name']
        phone = data_dict['phone']
        idcard = data_dict['IDNumber']
        checkId = data_dict['checkId']
        print(checkId)
        a.get_first_question(cardId, token)
        while True:
            if a.answer_dict['questionsDomain'] is not None:
                if a.answer_dict['answerDomainList'] == []:
                    a.answer(cardId, token)
                elif a.answer_dict['answerDomainList'] is None:
                    a.answer(cardId, token)
                else:
                    a.move_to_next(cardId, token)
            else:
                # a.get_report(cardId)
                a.createOrder(cardId)
                # getCardInfo(token, checkId)  # 没有选择套餐时候传递getCardInfo会返回套餐不存在
                print('答题完成')
                end = time.time()
                print("耗费时间%s ", end - start)
                # while True:
                a.upload_data(name, phone, idcard, checkId, token)
                break


#
# n = 0
# while n < 10 :
#     try:
#         answer_question.main()
#         n += 1
#     except Exception as e:
#         print("e:%s" % e)
#         answer_question.main()
#         n += 1
answer_question.main()
