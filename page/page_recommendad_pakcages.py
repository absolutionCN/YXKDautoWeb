import page,random,time
from selenium.webdriver.common.keys import Keys
from time import sleep
from Base.base import Base
from Base.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


class PageRecommendadPackages(Base):
    # 点击套餐推荐标签
    def page_click_recommendad_packages(self):
        log.info("[点击套餐推荐按钮]:对{}元素进行点击".format(page.business_recommendad_packages))
        self.base_click(page.business_recommendad_packages)

    # 点击项目类别管理标签
    def page_click_item_classification(self):
        log.info("[点击项目类别管理标签]：对{}元素进行点击".format(page.business_recommendad_item_classification))
        self.base_click(page.business_recommendad_item_classification)

    # 点击项目类别管理新增按钮
    def page_click_item_classification_add(self):
        log.info("[点击项目类别管理新增按钮]:对{}元素进行点击".format(page.bussiness_item_classification_add))
        self.base_click(page.bussiness_item_classification_add)

    # 点击类别序号输入数据
    def page_input_category_number(self, value):
        log.info("[点击类别序号，输入数据]:对{}元素进行点击".format(page.bussiness_category_number))
        self.base_input(page.bussiness_category_number, value)

    # 点击编码输入框输入数据
    def page_input_encoding_number(self, value):
        log.info("[点击编码，输入数据]:对{}元素进行点击".format(page.business_encoding_number))
        self.base_input(page.business_encoding_number, value)

    # 点击类别名称输入框输入数据
    def page_input_category_name(self, value):
        log.info("[点击类别名称输入框，输入数据]:对{}元素进行点击".format(page.business_category_name))
        self.base_input(page.business_category_name, value)

    # 点击新增类别弹窗下的保存按钮
    def page_click_item_classification_add_button(self):
        log.info("[点击新增类别弹窗下的保存按钮]对：{}元素进行点击".format(page.business_item_classification_add_button))
        self.base_click(page.business_item_classification_add_button)

    # 点击类别管理下新增的的checkbox
    def page_click_item_classification_checkbox(self):
        log.info("[点击类别弹窗下新增的的checkbox]对:{}元素进行点击".format(page.business_item_classification_checkbox))
        self.base_click(page.business_item_classification_checkbox)

    # 点击类别管理下的编辑按钮
    def page_click_item_classification_edit_button(self):
        log.info("[点击类别管理下的编辑按钮]对：{}元素进行点击".format(page.bussiness_item_classification_edit_button))
        self.base_click(page.bussiness_item_classification_edit_button)

    # 获取返回的报错信息
    def page_batch_return_err_info(self):
        return self.base_get_text(page.business_err_info)

    # 组合调用方法
    def page_item_classification_add_edit(self):
        try:
            sleep(10)
            self.page_click_recommendad_packages()
            sleep(1)
            self.page_click_item_classification()
            sleep(1)
            self.page_click_item_classification_add()
            sleep(1)
            self.page_input_category_number(time.strftime("%m%d%H%M%S",time.localtime(time.time())))
            sleep(1)
            self.page_input_encoding_number(time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time())) + 'WLT自动新增编码')
            sleep(1)
            self.page_input_category_name(time.strftime("%H%M%S", time.localtime(time.time())) + '自动新增')
            sleep(1)
            self.page_click_item_classification_add_button()
            sleep(1)
            self.page_click_item_classification_checkbox()
            sleep(1)
            self.page_click_item_classification_edit_button()
            sleep(1)
            self.page_input_category_number(time.strftime("%m%d%H%M%S",time.localtime(time.time())))
            sleep(1)
            self.page_input_encoding_number(time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time())) + 'WLT自动编辑编码')
            sleep(1)
            self.page_input_category_name(time.strftime("%H%M%S", time.localtime(time.time())) + '自动编辑')
            sleep(1)
            self.page_click_item_classification_add_button()

        except Exception as e:
            print("page_item_classification_add_edit报错原因 % s" % e)
            self.base_get_image()
