import unittest
import time
import random
from assertpy import assert_that


# 定义测试类
from Base.get_driver import GetDriver
from page.page_bookingSetting import PageBooking
from page.page_login import PageBusinessLogin


class TestCart(unittest.TestCase):
    # 定义setup
    def setUp(self):
        # 获取driver
        self.driver = GetDriver.get_dirver()
        # 实例化 PageCart
        self.bookingManagement = PageBooking(self.driver)
        # 调用成功登陆 依赖
        PageBusinessLogin(self.driver).page_login_success()
        # # 跳转到首页
        # self.upload_excel.page_open_index()

    # 定义teardown
    def tearDown(self):
        # 关闭driver
        GetDriver().quit_driver()

    # 定义测试 预约配置设置修改
    def test_change_booking_setting(self):
        # 调用 组合修改预约配置设置方法
        self.bookingManagement.page_change_booking_settings()
        msg = self.bookingManagement.page_save_success_msg()
        try:
            assert_that(msg).is_equal_to('修改成功')
            print('test06测试通过')
            self.bookingManagement.base_get_info_image()
        except AssertionError as e:
            print('test06报错信息为： %s ' % e)
            self.bookingManagement.base_get_image()
            raise