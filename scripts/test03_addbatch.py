import unittest
import time
import random
from assertpy import assert_that

# 定义测试类
from Base.get_driver import GetDriver
from page.page_cart import PageCart
from page.page_login import PageBusinessLogin
from Base.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()

class TestCart(unittest.TestCase):
    # 定义setup
    def setUp(self):
        # 获取driver
        self.driver = GetDriver.get_dirver()
        # 实例化 PageCart
        self.cart = PageCart(self.driver)
        # 调用成功登陆 依赖
        PageBusinessLogin(self.driver).page_login_success()
        # 跳转到首页
        # self.cart.page_open_index()

    # 定义teardown
    def tearDown(self):
        # 关闭driver
        GetDriver().quit_driver()

    # 定义测试添加批次
    def test_add_batch(self):
        batchName = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time())) + 'WLT自动测试批次'
        total = random.randint(1, 5)
        # 调用 组合添加批次业务方法
        self.cart.page_add_batch(batchName, total)
        time.sleep(1)
        msg = self.cart.page_batch_return_right_info()
        print(msg)
        try:
            assert_that(msg).is_equal_to('添加成功')
            print('test03测试通过')
            self.cart.base_get_info_image()
        except AssertionError as e:
            print('test03的报错信息为 %s' % e)
            self.cart.base_get_image()
            raise
