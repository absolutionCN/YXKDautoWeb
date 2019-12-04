# import unittest
# from time import sleep
# import random
#
# # 定义测试类
# from Base.get_driver import GetDriver
# from Base.get_driver import GetSecondDriver
# from page.page_customer_login import PageCustomerLogin
# from page.page_login import PageBusinessLogin
# # from auto_test.auto_answer import answer_question
#
#
# class TestCustomerLogin(unittest.TestCase):
#     # 定义setup
#     def setUp(self):
#         # 获取driver
#         self.driver = GetDriver.get_dirver()
#         self.customer_driver = GetSecondDriver.get_Custonmer_dirver()
#         # 调用成功登陆 依赖
#         PageBusinessLogin(self.driver).page_login_success()
#         # 实例化 PageCart
#         self.get_customer_info = PageCustomerLogin(self.driver)
#         self.get_customer_login = PageCustomerLogin(self.customer_driver)
#         # 跳转到首页
#         # self.get_customer_info.page_open_index()
#
#     # 定义teardown
#     def tearDown(self):
#         # 关闭driver
#         GetDriver().quit_driver()
#         GetSecondDriver.quit_driver()
#
#     # 定义测试 获取C端账号密码登陆
#     def test_customer_login(self):
#         # answer_question.main()
#         # 调用方法
#         # self.get_customer_info.page_get_username_pwd()
#         # self.get_customer_info.page_business_get_username_pwd()
#         # username = self.get_customer_info.page_card_username()
#         # pwd = self.get_customer_info.page_card_pwd()
#         # print(username, pwd)
#         # self.get_customer_login.page_customer_login(username=username, pwd=pwd)
#         self.get_customer_info.page_business_get_username_pwd()
#         username = self.get_customer_info.page_card_username()
#         pwd = self.get_customer_info.page_card_pwd()
#         self.get_customer_login.page_customer_login(username=username, pwd=pwd)
#
#
#         # print(self.get_customer_info.page_business_get_username_pwd())
