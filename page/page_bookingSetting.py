# encoding:utf-8
import page
import os, random
from selenium.webdriver.common.keys import Keys
from time import sleep
from Base.base import Base
from Base.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


class PageBooking(Base):
    # 点击预约管理标签
    def page_click_business_booking_label(self):
        log.info("[page_click_business_booking_label]对：{}元素进行点击".format(page.business_booking_label))
        self.base_click(page.business_booking_label)

    # 点击预约配置子标签
    def page_click_business_booking_setting(self):
        log.info("[page_click_business_booking_setting]对：{}元素进行点击".format(page.business_booking_setting))
        self.base_click(page.business_booking_setting)

    # 点击预约配置页面编辑按钮
    def page_click_business_booking_button(self):
        log.info("[点击预约配置页面编辑按钮]对：{}元素进行点击".format(page.business_booking_button))
        self.base_click(page.business_booking_button)

    # # 配置预约界面其他设置填写信息
    # def page_input_booking_settings(self):
    #     log.info("[可预约时间段进行编辑]对：{}元素进行input".format(page.businsee_booking_timePeriod))
    #     self.base.base_input()

    # 点击添加体检区
    def page_click_business_booking_addCheckAreas(self):
        log.info("[点击添加体检区按钮]对：{}元素进行点击".format(page.business_booking_addCheckAreas))
        self.base_click(page.business_booking_addCheckAreas)

    # 输入可预约时间段
    def page_input_businsee_booking_timePeriod(self, value):
        log.info("[点击可预约时间段按钮输入框，输入数值]对：{}元素进行点击".format(page.businsee_booking_timePeriod))
        self.base_input(page.businsee_booking_timePeriod, value)

    # 输入特殊时间设置
    def page_input_business_booking_intervalLastTime(self, intervalLastTime):
        log.info("[点击特殊时间设置输入框，输入数值]对:{}元素进行点击".format(page.business_booking_intervalLastTime))
        self.base_input(page.business_booking_intervalLastTime, intervalLastTime)

    # 输入工作日设置
    def page_input_businsee_booking_intervalTime(self, intervalTime):
        log.info("[点击工作日输入框，输入数值]对：{}元素进行点击".format(page.businsee_booking_intervalTime))
        self.base_input(page.businsee_booking_intervalTime, intervalTime)

    # 保存预约配置修改
    def page_save_bookging_settings(self):
        log.info("[点击保存按钮，保存预约配置修改]对：{}进行点击".format(page.business_save_booking_button))
        self.base_click(page.business_save_booking_button)

    # 获取保存成功信息
    def page_save_success_msg(self):
        return self.base_get_text(page.bussiness_save_success_msg)


    # 组合调用方法
    def page_change_booking_settings(self):
        try:
            sleep(10)
            self.page_click_business_booking_label()
            sleep(1)
            self.page_click_business_booking_setting()
            sleep(1)
            self.page_click_business_booking_button()
            sleep(1)
            self.page_input_businsee_booking_timePeriod(str(random.randint(5, 730)))
            sleep(1)
            self.page_input_business_booking_intervalLastTime(
                str(random.randint(10, 24))+ ":" +str(random.randint(1, 59)))
            sleep(1)
            self.page_input_businsee_booking_intervalTime(str(random.randint(1, 5)))
            sleep(1)
            self.page_save_bookging_settings()
        except Exception as e:
            print("page_change_booking_settings报错原因 % s" % e)
            self.base_get_image()
