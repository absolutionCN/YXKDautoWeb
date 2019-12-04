import page
import time
from time import sleep
from Base.base import Base
from Base.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


class PageCart(Base):
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

    # 点击新增批次按钮
    def page_click_add_batch(self):
        log.info("[page_click_batch]对：{}元素进行点击".format(page.business_add_batch))
        self.base_click(page.business_add_batch)

    # 输入批次名称
    def page_input_batch_name(self, batchname):
        log.info("[page_input_batch_name]对：{}元素输入批次名称：{}操作".format(page.business_batch_name, batchname))
        self.base_input(page.business_batch_name, batchname)

    # 输入测评卡数量
    def page_input_total_card(self, total):
        log.info("[page_input_total_card]对:{}元素输入测评卡数量：{}操作".format(page.business_card_total, total))
        self.base_input(page.business_card_total, total)

    # 点击推荐套餐
    def page_click_package(self):
        log.info("[page_click_package]对:{}元素进行点击".format(page.business_package_toggle))
        self.base_click(page.business_package_toggle)

    # 打折方式//TODO

    # 选择体检区
    def page_select_checkArea(self):
        log.info("[page_select_checkArea]对:{}元素进行查找".format(page.business_check_Area))
        self.base_select_option(page.business_check_Area, 1)

    # 选择套餐类
    def page_select_package_type(self):
        log.info("[page_select_package_type]对：{}元素进行点击".format(page.business_package_fixed))
        self.base_click(page.business_package_fixed)

    # 减免费用//TODO

    # 添加全部套餐按钮
    def page_click_all_package(self):
        log.info("[page_click_all_package]对：{}元素进行点击".format(page.business_add_all_package))
        self.base_click(page.business_add_all_package)

    # 点击保存按钮
    def page_click_save_button(self):
        log.info("[page_click_save_button]对：{}元素进行点击保存".format(page.business_save_setting))
        self.base_click(page.business_save_setting)

    # # 获取添加成功
    # def page_save_batch_success(self):
    #     return self.base_get_text(page.business_info)

    # 获取返回正确信息
    def page_batch_return_right_info(self):
        return self.base_get_text(page.business_right_info)

    # 获取返回的报错信息
    def page_batch_return_err_info(self):
        return self.base_get_text(page.business_err_info)

    # 组合业务调用方法
    def page_add_batch(self, batchname, total):
        try:
            sleep(10)
            self.page_click_batch_management()
            sleep(1)
            self.page_click_add_batch()
            sleep(1)
            self.page_input_batch_name(batchname)
            sleep(1)
            self.page_input_total_card(total)
            sleep(1)
            self.page_click_package()
            sleep(1)
            self.page_select_checkArea()
            sleep(1)
            self.page_select_package_type()
            sleep(1)
            self.page_click_all_package()
            sleep(1)
            self.page_click_save_button()
            sleep(1)
        except Exception as e:
            print("page_add_batch报错原因 % s" % e)
