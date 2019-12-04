import page
from selenium.webdriver.common.keys import Keys
from time import sleep
from Base.base import Base
from Base.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


class PageCustomerLogin(Base):
    # 打开首页
    def page_open_index(self):
        self.base_index()

    # 点击测评管理标签
    def page_click_measurement_management(self):
        log.info("[page_click_measurement_management]对：{}元素进行点击".format(page.business_measurement_management))
        self.base_click(page.business_measurement_management)

    # 点击测评卡管理标签
    def page_click_card_management(self):
        log.info("[page_click_card_management]对：{}元素进行点击".format(page.business_card_management))
        self.base_click(page.business_card_management)

    # 点击测评卡详细信息
    def page_click_card_info(self):
        log.info("[page_click_card_info]对：{}元素进行点击".format(page.business_card_info))
        self.base_click(page.business_card_info)

    # 获取测评卡账号文本
    def page_card_username(self):
        log.info("[page_card_username]对：{}元素获取文本".format(page.business_card_username_info))
        # username = self.base_get_text(page.business_card_username_info)[5:]
        username = self.base_get_text(page.business_card_username_info)[5:]
        print('username %s ' % username)
        return username

    # 获取测评卡密码文本
    def page_card_pwd(self):
        log.info("[page_card_pwd]对：{}元素获取文本".format(page.business_card_pwd_info))
        pwd = self.base_get_text(page.business_card_pwd_info)[3:]
        print('pwd %s ' % pwd)
        return pwd

    # C端网页输入用户名
    def page_customer_username_input(self, username):
        log.info("[page_customer_username_input]对：{}元素进行输入信息".format(page.customer_username_input))
        self.base_input(page.customer_username_input, username)

    # C端网页输入密码
    def page_customer_pwd_input(self, pwd):
        log.info("[page_customer_pwd_input]对：{}元素输入信息".format(page.customer_pwd_input))
        self.base_input(page.customer_pwd_input, pwd)

    # 输入验证码
    def page_customer_verification_code(self):
        log.info("[page_customer_verification_code]对：{}元素输入信息".format(page.customer_verification_code))
        self.base_input(page.customer_verification_code, 8888)

    # 点击登录按钮
    def page_click_login_button(self):
        log.info("[page_click_login_button]对:{}元素进行点击登录".format(page.customer_login_button))
        self.base_click(page.customer_login_button)

    # 组合获取账号密码方法
    # def page_get_username_pwd(self):
    #     sleep(5)
    #     self.base_click(page.business_card_management)
    #     self.base_click(page.business_card_info)

    # 页面下滑
    def page_down(self):
        self.base_sliding_down()

    # 点击预约时间
    def page_click_time(self):
        log.info("[page_click_time]对:{}元素进行点击".format(page.customer_choice_time))
        self.base_click(page.customer_choice_time)

    # 点击选择具体时间
    def page_click_tru_time(self):
        log.info("[page_click_time]对:{}元素进行点击".format(page.customer_time))
        self.base_click(page.customer_time)

    # 点击预约时间确定按钮
    def page_click_true_time_btn(self):
        log.info("[page_click_true_time_btn]对:{}元素进行点击".format(page.customer_time_btn))
        self.base_send_keys(page.customer_time_btn)

    # B端网页获取账号密码
    def page_business_get_username_pwd(self):
        sleep(5)
        self.base_click(page.business_card_management)
        self.base_click(page.business_card_info)

    # C端网页登陆
    def page_customer_login(self, username, pwd):
        self.base_input(page.customer_username_input, username)
        self.base_input(page.customer_pwd_input, pwd)
        self.base_input(page.customer_verification_code, 8888)
        self.base_click(page.customer_login_button)
        self.base_click(page.customer_choice_package)
        self.base_click(page.customer_package_btn)
        self.base_input(page.customer_input_budget, 5000)
        self.base_click(page.customer_confirm_button)
        sleep(10)
        self.base_sliding_down()
        self.base_click(page.customer_choice_time)
        sleep(1)
        self.base_click(page.customer_time)
        sleep(5)
        self.base_click(page.customer_time_btn)
