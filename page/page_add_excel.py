# encoding:utf-8
import page
import os
from selenium.webdriver.common.keys import Keys
from time import sleep
from Base.base import Base
from Base.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


class PageAddExcel(Base):
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

    # 点击导入批次按钮
    def page_click_add_excel(self):
        log.info("[page_click_add_excel]对：{}元素进行点击".format(page.business_add_excel))
        self.base_click(page.business_add_excel)

    # 输入批次名称
    def page_input_batch_name(self, batchname):
        log.info("[page_input_batch_name]对：{}元素输入批次名称：{}操作".format(page.business_batch_name, batchname))
        self.base_input(page.business_batch_name, batchname)

    # 点击导入文件按钮
    def page_click_upload_file(self):
        log.info("[page_click_upload_file]对：{}元素进行点击".format(page.business_choice_file))
        self.base_click(page.business_choice_file)

    # 点击推荐套餐
    def page_click_package(self):
        log.info("[page_click_package]对:{}元素进行点击".format(page.business_package_toggle))
        self.base_click(page.business_package_toggle)

    # 选择体检区
    def page_select_checkArea(self, value):
        log.info("[page_select_checkArea]对:{}元素进行查找".format(page.business_check_Area))
        self.base_select_option(page.business_check_Area, value)

    # 选择套餐类
    def page_select_package_type(self):
        log.info("[page_select_package_type]对：{}元素进行点击".format(page.business_package_fixed))
        self.base_click(page.business_package_fixed)

    # 导入批次模板下的套餐类型1
    def page_select_all_package(self):
        log.info("[page_select_all_package]对:{}元素进行点击".format(page.business_upload_excel_package))
        self.base_click(page.business_upload_excel_package)


    # 添加全部套餐按钮
    def page_click_all_package(self):
        log.info("[page_click_all_package]对：{}元素进行点击".format(page.business_add_all_package))
        self.base_click(page.business_add_all_package)

    # 点击保存按钮
    def page_click_save_button(self):
        log.info("[page_click_save_button]对：{}元素进行点击保存".format(page.business_save_setting))
        self.base_click(page.business_save_setting)

    # 点击导入批次下的提交按钮
    def page_click_save_settings(self):
        log.info("[page_click_save_settings]对：{}元素进行点击保存".format(page.business_upload_save_settings))
        self.base_click(page.business_upload_save_settings)

    # 获取添加成功
    def page_save_batch_success(self):
        return self.base_get_text(page.business_save_success)

    # 获取异常信息
    def page_get_error_msg(self):
        return self.base_get_text(page.business_add_batch_error_msg)

    # 发送短信按钮
    def page_click_send_message(self):
        log.info("[导入批次发送短信]对:{}元素进行点击".format(page.business_send_message))
        self.base_click(page.business_send_message)

    # 不发送短信按钮

    def page_click_not_send_message(self):
        log.info("[导入批次不发送短信]对：{}元素进行点击".format(page.business_not_send_message))
        self.base_click(page.business_not_send_message)


    # 组合业务调用方法
    def page_add_excel(self, batchname):
        try:
            sleep(10)
            self.page_click_measurement_management()
            sleep(1)
            self.page_click_add_excel()
            sleep(1)
            self.page_input_batch_name(batchname)
            sleep(1)
            self.base_send_keys(page.business_choice_file)   # 导入文件
            sleep(1)
            os.system(r'E:\PycharmProject\webAuto\data\uploadFile_v1.1.exe')
            sleep(1)
            self.page_click_package()  # 点击推荐套餐按钮
            sleep(1)
            self.page_select_checkArea(1)  # 选择体检区
            sleep(1)
            self.page_select_all_package()  # 导入批次模板下的套餐类型1
            sleep(1)
            self.page_click_all_package()  # 添加全部按钮
            sleep(1)
            self.page_click_save_settings()  # 导入批次模板下的提交按钮
            sleep(1)
            self.page_click_send_message() # 点击发送短信按钮
            sleep(1)
        except Exception as e:
            print("page_add_excel报错原因 % s" % e)
            self.base_get_image()
