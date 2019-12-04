from Base.base import Base
import page
from Base.get_logger import GetLogger


# 获取log日志器
log = GetLogger().get_logger()


class PageBusinessLogin(Base):
    # 输入用户名
    def page_input_username(self, username):
        log.info("[page_loging] 对：{} 元素 输入用户名：{} 操作".format(page.login_B_username, username))
        self.base_input(page.login_B_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        log.info("[page_loging] 对：{}元素输入密码：{}操作".format(page.login_B_pwd, pwd))
        self.base_input(page.login_B_pwd, pwd)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.login_B_btn)

    # 获取错误提示信息
    def page_get_err_info(self):
        return self.base_get_text(page.login_err_info)

    # 判断是否登录成功
    def page_if_login_success(self):
        # 注意一定要将找元素的结果返回 True：存在
        return self.base_element_is_exist(page.login_page_info)

    # 点击退出功能
    def page_click_logout_link(self):
        return self.base_click(page.login_logout_link)

    # 判断是否退出成功
    def page_if_logout_success(self):
        return self.base_element_is_exist(page.login_B_username)

    # 组合业务方法 —— 登录业务直接调用
    def page_login(self, username, pwd):
        log.info("[page_login] 正在执行登陆过操作，用户名：{} 密码：{}".format(username, pwd))
        # 调用输入用户名
        self.page_input_username(username)
        # 调用输入密码
        self.page_input_pwd(pwd)
        # 调用点击登录
        self.page_click_login_btn()

    # 组合登陆业务方法(其他模块依赖使用)
    def page_login_success(self, username='0100601admin', pwd='123456'):
        log.info("[page_login] 正在执行登陆过操作，用户名：{} 密码：{}".format(username, pwd))
        # 调用输入用户名
        self.page_input_username(username)
        # 调用输入密码
        self.page_input_pwd(pwd)
        # 调用点击登录
        self.page_click_login_btn()