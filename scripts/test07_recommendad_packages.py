import unittest
import time
import random
from assertpy import assert_that


# 定义测试类
from Base.get_driver import GetDriver
from page.page_recommendad_pakcages import PageRecommendadPackages
from page.page_login import PageBusinessLogin


class TestCart(unittest.TestCase):
    # 定义setup
    def setUp(self):
        # 获取driver
        self.driver = GetDriver.get_dirver()
        # 实例化 PageCart
        self.recommendad_packages = PageRecommendadPackages(self.driver)
        # 调用成功登陆 依赖
        PageBusinessLogin(self.driver).page_login_success()
        # # 跳转到首页
        # self.upload_excel.page_open_index()

    # 定义teardown
    def tearDown(self):
        # 关闭driver
        GetDriver().quit_driver()

    # 定义测试 项目类别修改
    def test_item_classification(self):
        self.recommendad_packages.page_item_classification_add_edit()
        err_msg = self.recommendad_packages.page_batch_return_err_info()
        try:
            assert_that(err_msg).is_empty()
            print("test07测试通过")
            self.recommendad_packages.base_get_info_image()
        except AssertionError as e:
            print("test07报错信息为 %s" % e )
            self.recommendad_packages.base_get_image()
            raise





