import unittest
import time
import random
from assertpy import assert_that


# 定义测试类
from Base.get_driver import GetDriver
from page.page_login import PageBusinessLogin





class TestCart(unittest.TestCase):
    # 定义setup
    def setUp(self):
        # 获取driver
        self.driver = GetDriver.get_dirver()
        # 实例化 Page
        self.