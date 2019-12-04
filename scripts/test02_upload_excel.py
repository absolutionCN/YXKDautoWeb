import unittest
import time
import random
from assertpy import assert_that


# 定义测试类
from Base.get_driver import GetDriver
from page.page_add_excel import PageAddExcel
from page.page_login import PageBusinessLogin


class TestCart(unittest.TestCase):
    # 定义setup
    def setUp(self):
        # 获取driver
        self.driver = GetDriver.get_dirver()
        # 实例化 PageCart
        self.upload_excel = PageAddExcel(self.driver)
        # 调用成功登陆 依赖
        PageBusinessLogin(self.driver).page_login_success()
        # # 跳转到首页
        # self.upload_excel.page_open_index()

    # 定义teardown
    def tearDown(self):
        # 关闭driver
        GetDriver().quit_driver()

    # 定义测试 导入excel批次
    def test_upload_excel(self):
        batchName = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time())) + 'WLT自动测试导入批次'
        # 调用 组合添加批次业务方法
        self.upload_excel.page_add_excel(batchName)
        # error_msg = self.upload_excel.page_get_error_msg()
        msg = self.upload_excel.page_save_batch_success()
        try:
            if assert_that(msg).is_equal_to('导入成功'):
                print('test02测试通过')
                self.upload_excel.base_get_info_image()
        except AssertionError as e:
            print('test02的报错信息为 %s' % e)
            self.upload_excel.base_get_image()
            raise

