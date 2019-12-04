import unittest
import time
import random
from assertpy import assert_that

# 定义测试类
from Base.get_driver import GetDriver
from page.page_additional_batch import PageAdditionalBatch
from page.page_login import PageBusinessLogin


class TestAdditionalBatch(unittest.TestCase):
    # 定义setup
    def setUp(self):
        # 获取driver
        self.driver = GetDriver.get_dirver()
        # 实例化 PageCart
        self.additional_batch = PageAdditionalBatch(self.driver)
        # 调用成功登陆 依赖
        PageBusinessLogin(self.driver).page_login_success()
        # # 跳转到首页
        # self.additional_batch.page_open_index()

    # 定义teardown
    def tearDown(self):
        # 关闭driver
        GetDriver().quit_driver()

    # 定义测试 追加批次
    def test_additional_batch(self):
        # 调用 组合追加批次业务方法
        self.additional_batch.page_additional_batch()
        msg = self.additional_batch.page_batch_return_right_info()
        try:
            assert_that(msg).is_equal_to('追加成功')
            print('test04测试通过')
            self.additional_batch.base_get_info_image()
        except AssertionError as e:
            print('test04的报错信息为 %s' % e)
            self.additional_batch.base_get_image()
            raise
