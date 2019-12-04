import page
import os, random
from selenium.webdriver.common.keys import Keys
from time import sleep
from Base.base import Base
from Base.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()



class PageAdditionalBatch(Base):
    # 打开首页
    def page_open_index(self):
        sleep(1)
        self.base_index()

    # 点击测评管理标签
    def page_click_measurement_management(self):
        log.info("[page_click_measurement_management]对：{}元素进行点击".format(page.business_measurement_management))
        self.base_click(page.business_measurement_management)

    # 点击批次管理标签
    def page_click_batch_management(self):
        log.info("[page_click_batch_management]对：{}元素进行点击".format(page.business_batch_management))
        self.base_click(page.business_batch_management)

    # 点击批次管理勾选按钮
    def page_click_check_button(self):
        log.info("[page_click_check_button]对:{}元素进行点击".format(page.business_check_button))
        self.base_click(page.business_check_button)

    # 点击追加批次按钮
    def page_click_additional_button(self):
        log.info("[page_click_additional_button]对：{}元素进行点击".format(page.business_additional_button))
        self.base_click(page.business_additional_button)

    # 按数量追加测评卡
    def page_click_add_card_by_number(self):
        log.info("[按照数量增加测评卡]对：{}元素进行点击".format(page.bussiness_add_card_by_number))
        self.base_click(page.bussiness_add_card_by_number)

    # 输入测评卡数量
    def page_input_card_number(self, value):
        log.info("[输入测评卡数量]对:{}元素进行点击".format(page.bussiness_add_card_number))
        self.base_input(page.bussiness_add_card_number, value)

    # 点击选择文件按钮
    def page_click_upload_file(self):
        log.info("[page_click_upload_file]对：{}元素进行点击".format(page.business_choice_file))
        self.base_click(page.business_choice_file)

    # 点击保存按钮
    def page_click_save_button(self):
        log.info("[page_click_save_button]对：{}元素进行点击保存".format(page.business_additional_put_button))
        self.base_click(page.business_additional_put_button)


    # 获取返回正确信息
    def page_batch_return_right_info(self):
        return self.base_get_text(page.business_right_info)

    # 获取返回的报错信息
    def page_batch_return_err_info(self):
        return self.base_get_text(page.business_err_info)

    # 组合业务调用方法
    def page_additional_batch(self):
        try:
            sleep(10)
            self.page_click_batch_management()
            sleep(1)
            self.page_click_check_button()
            sleep(1)
            self.page_click_additional_button()
            sleep(1)
            self.page_click_add_card_by_number()
            self.page_input_card_number(random.randint(1,10))
            sleep(1)
            self.base_sliding_down()
            sleep(1)
            self.page_click_save_button()
        except Exception as e:
            print("page_additional_batch报错原因 % s" % e)
            self.base_get_image()
