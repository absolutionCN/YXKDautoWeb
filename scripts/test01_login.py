import unittest

from Base.get_driver import GetDriver
from page.page_login import PageBusinessLogin
from parameterized import parameterized
from tool.read_txt import read_txt
from Base.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


def get_login_data() -> object:
    arrs = []
    for data in read_txt("login.txt"):
        arrs.append(tuple(data.strip().split(",")))
    return arrs[1:]


# 新建 登录测试类 并继承unittest.TestCase
class TestLogin(unittest.TestCase):
    # 新建setupClass
    @classmethod
    def setUpClass(cls):
        try:
            # 实例化，并获取driver
            cls.driver = GetDriver().get_dirver()
            # 实例化 PageBusinessLogin()
            cls.login = PageBusinessLogin(cls.driver)
        except Exception as e:
            log.error("错误:{}".format(e))
            # 截图
            cls.login.base_get_image()

    # 新建 登录测试方法
    @parameterized.expand(get_login_data())
    def test_login(self, username, pwd, expect_result, status):
        try:
            # 调用登录业务
            self.login.page_login(username, pwd)
            # 判断是否为正向
            if status == "true":
                # 断言是否登录成功
                try:
                    self.assertTrue(self.login.page_if_login_success())
                except Exception as e:
                    # 截图
                    self.login.base_get_image()
                    log.error("错误:{}".format(e))
            else:
                # 获取错误信息
                msg = self.login.page_get_err_info()
                print("msg:", msg)
                try:
                    self.assertEqual(msg, expect_result)
                except Exception as e:
                    # 截图
                    self.login.base_get_image()
                    log.error("错误:{}".format(e))
                # 点击错误提示框 确定按钮
        except Exception as e:
            log.error("错误：{}".format(e))
            # 截图
            self.login.base_get_image()





    # 新建 tearDownClass
    @classmethod
    def tearDownClass(cls):
        # 关闭driver驱动
        GetDriver().quit_driver()
